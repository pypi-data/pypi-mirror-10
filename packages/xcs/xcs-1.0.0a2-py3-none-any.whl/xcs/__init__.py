# -------------------------------------------------------------------------------
# Name:     xcs
# Purpose:  Implements the XCS (Accuracy-based Classifier System) algorithm,
#           roughly according to the description provided in the paper, "An
#           Algorithmic Description of XCS," by Martin Butz and Stewart Wilson.
#
# Butz, M. and Wilson, S. (2001). An algorithmic description of XCS. In Lanzi, P., 
#   Stolzmann, W., and Wilson, S., editors, Advances in Learning Classifier Systems:
#   Proceedings of the Third International Workshop, volume 1996 of Lecture Notes in 
#   Artificial Intelligence, pages 253–272. Springer-Verlag Berlin Heidelberg.
#
# Author:       Aaron Hosford
#
# Created:      5/5/2015
# Copyright:    (c) Aaron Hosford 2015, all rights reserved
# Licence:      Revised (3 Clause) BSD License
# -------------------------------------------------------------------------------

"""
xcs/__init__.py
(c) Aaron Hosford 2015, all rights reserved
Revised BSD License

Implements the XCS (Accuracy-based Classifier System) algorithm,
roughly according to the description provided in the paper, "An
Algorithmic Description of XCS," by Martin Butz and Stewart Wilson.

Butz, M. and Wilson, S. (2001). An algorithmic description of XCS. In Lanzi, P.,
    Stolzmann, W., and Wilson, S., editors, Advances in Learning Classifier Systems:
    Proceedings of the Third International Workshop, volume 1996 of Lecture Notes in
    Artificial Intelligence, pages 253–272. Springer-Verlag Berlin Heidelberg.

This file is part of the public API of the xcs package.
"""

__author__ = 'Aaron Hosford'
__all__ = [
    'RuleMetadata',
    'ActionSet',
    'MatchSet',
    'ClassifierSetParameters',
    'Population',
    'XCS',
    'test',
]

import random

# noinspection PyUnresolvedReferences
from xcs.bitstrings import BitString, BitCondition
from xcs.problems import MUXProblem, ObservedOnLineProblem


class RuleMetadata:
    """Metadata used by the XCS algorithm to track the rules (classifiers) in a population."""

    def __init__(self, time_stamp, parameters):
        self.time_stamp = time_stamp
        self.prediction = parameters.initial_prediction
        self.error = parameters.initial_error
        self.fitness = parameters.initial_fitness
        self.experience = 0
        self.action_set_size = 1
        self.numerosity = 1

    def __iadd__(self, other):
        self.numerosity += other.numerosity
        return self


class ActionSet:
    """A set of rules (classifiers) with the same action that matched the same situation."""

    def __init__(self, action, rules, population):
        self._action = action
        self._rules = rules  # {condition : metadata}
        self._prediction = None
        self._population = population
        self._parameters = population.parameters

    @property
    def action(self):
        """The action shared by the matching rules."""
        return self._action

    @property
    def population(self):
        """The population from which the action set was taken."""
        return self._population

    @property
    def prediction(self):
        """The predicted payoff for this action set."""
        if self._prediction is None:
            total_fitness = 0
            total_prediction = 0
            for metadata in self._rules.values():
                total_fitness += metadata.fitness
                total_prediction += metadata.prediction * metadata.fitness
            self._prediction = total_prediction / (total_fitness or 1)
        return self._prediction

    def _update_fitness(self):
        """Update the fitness of the rules belonging to this action set."""
        total_accuracy = 0
        accuracies = {}
        for condition, metadata in self._rules.items():
            if metadata.error < self._parameters.error_threshold:
                accuracy = 1
            else:
                accuracy = (
                    self._parameters.accuracy_coefficient *
                    (metadata.error / self._parameters.error_threshold) ** -self._parameters.accuracy_power
                )
            accuracies[condition] = accuracy
            total_accuracy += accuracy * metadata.numerosity
        for condition, metadata in self._rules.items():
            accuracy = accuracies[condition]
            metadata.fitness += (
                self._parameters.learning_rate *
                (accuracy * metadata.numerosity / total_accuracy - metadata.fitness)
            )

    def _action_set_subsumption(self):
        """Perform action set subsumption."""
        selected_condition = None
        selected_bit_count = None
        for condition, metadata in self._rules.items():
            if not (metadata.experience > self._parameters.subsumption_threshold and
                    metadata.error < self._parameters.error_threshold):
                continue
            bit_count = condition.count()
            if (selected_condition is None or
                    bit_count > selected_bit_count or
                    (bit_count == selected_bit_count and random.randrange(2))):
                selected_condition = condition
                selected_bit_count = bit_count

        if selected_condition is None:
            return

        selected_metadata = self._rules[selected_condition]

        to_remove = []
        for condition, metadata in self._rules.items():
            if selected_condition is not condition and selected_condition(condition):
                selected_metadata.numerosity += metadata.numerosity
                self._population.remove(condition, self._action, metadata.numerosity)
                to_remove.append(condition)

        for condition in to_remove:
            del self._rules[condition]

    def update(self, payoff):
        """Update the rule metadata for the rules belonging to this action set, based on the payoff received."""
        action_set_size = sum(metadata.numerosity for metadata in self._rules.values())

        for metadata in self._rules.values():
            metadata.experience += 1

            update_rate = max(self._parameters.learning_rate, 1 / metadata.experience)

            metadata.prediction += (payoff - metadata.prediction) * update_rate
            metadata.error += (abs(payoff - metadata.prediction) - metadata.error) * update_rate
            metadata.action_set_size += (action_set_size - metadata.action_set_size) * update_rate

        self._update_fitness()

        if self._parameters.do_action_set_subsumption:
            self._action_set_subsumption()

    def get_average_time_stamp(self):
        """Return the average time stamp for the rules in this action set."""
        return (
            sum(metadata.time_stamp * metadata.numerosity for metadata in self._rules.values()) /
            sum(metadata.numerosity for metadata in self._rules.values())
        )

    def set_timestamps(self, time_stamp):
        """Set the time stamp of each rule in this action set to the given value."""
        for metadata in self._rules.values():
            metadata.time_stamp = time_stamp

    def select_parent(self):
        """Select a rule from this action set, with probability proportionate to its fitness, to act as a parent for a
        new rule in the population. Return its bit condition."""
        total_fitness = sum(metadata.fitness for metadata in self._rules.values())
        selector = random.uniform(0, total_fitness)
        for condition, metadata in self._rules.items():
            selector -= metadata.fitness
            if selector <= 0:
                return condition
        return random.choice(list(self._rules))


class MatchSet:
    """A collection of coincident action sets."""

    def __init__(self, action_sets):
        self._action_sets = {action_set.action: action_set for action_set in action_sets}

    def select_action_set(self, explore=False):
        """Select an action set from among those belonging to this match set. If the explore parameter is provided, it
        is used as the probability of exploration, i.e. uniform action set selection. Otherwise the action set with the
        best predicted payoff is selected with probability 1."""

        if explore and (explore >= 1 or random.random() < explore):
            return random.choice(list(self._action_sets.values()))
        best_prediction = max(action_set.prediction for action_set in self._action_sets.values())
        best_action_sets = [
            action_set
            for action_set in self._action_sets.values()
            if action_set.prediction >= best_prediction
        ]
        if len(best_action_sets) == 1:
            return best_action_sets[0]
        return random.choice(best_action_sets)


class ClassifierSetParameters:
    """The parameters used by the XCS algorithm. For a detailed explanation of each parameter, please see the original
    paper by Martin Butz and Stewart Wilson."""

    max_population_size = 200                   # N
    learning_rate = .15                         # beta
    accuracy_coefficient = .1                   # alpha
    error_threshold = .01                       # epsilon_0
    accuracy_power = 5                          # nu
    discount_factor = .71                       # gamma
    GA_threshold = 35                           # theta_GA
    crossover_probability = .75                 # chi
    mutation_probability = .03                  # mu
    deletion_threshold = 20                     # theta_del
    fitness_threshold = .1                      # delta
    subsumption_threshold = 20                  # theta_sub
    wildcard_probability = .33                  # P_#
    initial_prediction = .00001                 # p_I
    initial_error = .00001                      # epsilon_I
    initial_fitness = .00001                    # F_I
    exploration_probability = .5                # p_explr
    minimum_actions = 2                         # theta_mna
    do_GA_subsumption = False                   # doGASubsumption
    do_action_set_subsumption = False           # doActionSetSubsumption

    def __init__(self, possible_actions):
        self.possible_actions = frozenset(possible_actions)
        self.minimum_actions = len(self.possible_actions)


class Population:
    """A set of rules (classifiers), together with their associated metadata."""

    def __init__(self, parameters):
        self._population = {}
        self._parameters = parameters
        self._time_stamp = 0

    @property
    def parameters(self):
        """The parameter settings used by this population."""
        return self._parameters

    def get_match_set(self, situation):
        """Accept a situation, encoded as a bit string. Return the set of matching rules (classifiers) for the given
        situation."""

        if not isinstance(situation, (BitString, BitCondition)):
            raise TypeError(situation)

        by_action = {}
        while not by_action:
            for condition, actions in self._population.items():
                if not condition(situation):
                    continue
                for action, rule_metadata in actions.items():
                    if action in by_action:
                        by_action[action][condition] = rule_metadata
                    else:
                        by_action[action] = {condition: rule_metadata}
            if len(by_action) < self._parameters.minimum_actions:
                condition, action, metadata = self.cover(situation, by_action)
                assert condition(situation)
                self.add(condition, action, metadata)
                self.prune()
                by_action.clear()

        return MatchSet(ActionSet(action, rules, self) for action, rules in by_action.items())

    def add(self, condition, action, metadata):
        """Add a new rule to the population."""
        if condition not in self._population:
            self._population[condition] = {}
        if action in self._population[condition]:
            self._population[condition][action] += metadata
        else:
            self._population[condition][action] = metadata

    def remove(self, condition, action, count=1):
        """Remove one or more instances of a rule in the population."""
        metadata = self.get_metadata(condition, action)
        if metadata is None:
            return

        metadata.numerosity -= count
        if metadata.numerosity <= 0:
            del self._population[condition][action]
            if not self._population[condition]:
                del self._population[condition]

    def cover(self, situation, existing_actions):
        """Create a new rule that matches the given situation and return it. Preferentially choose an action that is
        not present in the existing actions, if possible."""

        condition = BitCondition.cover(situation, self._parameters.wildcard_probability)
        action_candidates = ((set(existing_actions) - self._parameters.possible_actions) or
                             self._parameters.possible_actions)
        action = random.choice(list(action_candidates))
        metadata = RuleMetadata(self._time_stamp, self._parameters)
        return condition, action, metadata

    def mutate(self, condition, situation):
        """Create a new condition from the given one by probabilistically applying point-wise mutations. Bits that were
        originally wildcarded in the parent condition acquire their values from the provided situation, to ensure the
        child condition continues to match it."""

        # TODO: Revamp to take advantage of numpy array speeds

        bits = []
        mask = []
        for index, value in enumerate(condition):
            if random.random() < self._parameters.mutation_probability:
                if value is None:
                    value = situation[index]
                else:
                    value = None
            if value is None:
                bits.append(False)
                mask.append(False)
            else:
                bits.append(value)
                mask.append(True)

        return BitCondition(bits, mask)

    def get_metadata(self, condition, action):
        """Return the metadata associated with the given rule (classifier)."""

        if condition not in self._population or action not in self._population[condition]:
            return None
        return self._population[condition][action]

    def run_ga(self, action_set, situation):
        """Update the time stamp. If sufficient time has passed, apply the genetic algorithm's operators to update the
         population."""

        self._time_stamp += 1
        if self._time_stamp - action_set.get_average_time_stamp() <= self._parameters.GA_threshold:
            return

        action_set.set_timestamps(self._time_stamp)

        parent1 = action_set.select_parent()
        parent2 = action_set.select_parent()

        parent1_metadata = (self.get_metadata(parent1, action_set.action) or
                            RuleMetadata(self._time_stamp, self._parameters))
        parent2_metadata = (self.get_metadata(parent1, action_set.action) or
                            RuleMetadata(self._time_stamp, self._parameters))

        if random.random() < self._parameters.crossover_probability:
            child1, child2 = parent1.crossover_with(parent2)
        else:
            child1, child2 = parent1, parent2

        child1 = self.mutate(child1, situation)
        child2 = self.mutate(child2, situation)

        new_children = []
        for child in child1, child2:
            if self._parameters.do_GA_subsumption:
                subsumed = False
                for parent, metadata in (parent1, parent1_metadata), (parent2, parent2_metadata):
                    if (metadata.experience > self._parameters.subsumption_threshold and
                            metadata.error < self._parameters.error_threshold and
                            parent(child)):
                        # print(parent, child)
                        self._population[parent][action_set.action].numerosity += 1
                        subsumed = True
                        break
                if subsumed:
                    continue

            if child in self._population:
                if action_set.action in self._population[child]:
                    self._population[child][action_set.action].numerosity += 1
                    continue
            else:
                self._population[child] = {}

            new_children.append(child)

        if new_children:
            prediction = (parent1_metadata.prediction + parent2_metadata.prediction) / 2
            error = (parent1_metadata.error + parent2_metadata.error) / 2
            fitness = (parent1_metadata.fitness + parent2_metadata.fitness) / 2 * .1

            for child in new_children:
                metadata = RuleMetadata(self._time_stamp, self._parameters)
                metadata.prediction = prediction
                metadata.error = error
                metadata.fitness = fitness
                self.add(child, action_set.action, metadata)

        self.prune()

    def prune(self):
        """Reduce the population size, if necessary, to ensure that it does not exceed the maximum population size set
        out in the parameters."""

        total_numerosity = sum(
            metadata.numerosity
            for actions in self._population.values()
            for metadata in actions.values()
        )
        if total_numerosity <= self._parameters.max_population_size:
            return

        total_fitness = sum(metadata.fitness for actions in self._population.values() for metadata in actions.values())
        average_fitness = total_fitness / total_numerosity

        total_votes = 0
        deletion_votes = {}
        for condition, pop_by_action in self._population.items():
            votes_by_action = {}
            deletion_votes[condition] = votes_by_action
            for action, metadata in pop_by_action.items():
                vote = metadata.action_set_size * metadata.numerosity
                if (metadata.experience > self._parameters.deletion_threshold and
                        metadata.fitness / metadata.numerosity < self._parameters.fitness_threshold * average_fitness):
                    vote *= average_fitness / (metadata.fitness / metadata.numerosity)
                votes_by_action[action] = vote
                total_votes += vote

        selector = random.uniform(0, total_votes)
        for condition, votes_by_action in deletion_votes.items():
            for action, vote in votes_by_action.items():
                selector -= vote
                if selector <= 0:
                    metadata = self._population[condition][action]
                    if metadata.numerosity > 1:
                        metadata.numerosity -= 1
                    else:
                        del self._population[condition][action]
                        if not self._population[condition]:
                            del self._population[condition]
                    return


class XCS:
    """The XCS algorithm. Create the parameters and (optionally) a population, passing them in to initialize the XCS
    algorithm. Then create a problem instance and pass it to drive()."""

    def __init__(self, parameters, population=None):
        self._parameters = parameters
        self._population = population or Population(parameters)

    @property
    def parameters(self):
        """The parameter settings used by this instance of the XCS algorithm."""
        return self._parameters

    @property
    def population(self):
        """The population used by this instance of the XCS algorithm."""
        return self._population

    def drive(self, problem):
        """The main loop/entry point of the XCS algorithm. Create a problem instance and pass it in to this method to
        perform the algorithm and optimize the rule set. Problem instances must implement the OnLineProblem interface.
        """
        previous_situation = None
        previous_reward = 0
        previous_action_set = None
        while problem.more():
            situation = problem.sense()
            match_set = self._population.get_match_set(situation)
            action_set = match_set.select_action_set(self._parameters.exploration_probability)
            reward = problem.execute(action_set.action)
            if previous_action_set:
                payoff = previous_reward + self._parameters.discount_factor * action_set.prediction
                previous_action_set.update(payoff)
                self._population.run_ga(previous_action_set, previous_situation)
            previous_situation = situation
            previous_reward = reward
            previous_action_set = action_set
        if previous_action_set:
            previous_action_set.update(previous_reward)
            self._population.run_ga(previous_action_set, previous_situation)


def test():
    """A quick test of the XCS algorithm, demonstrating how to use it in client code."""
    import time

    problem = MUXProblem(10000)
    problem = ObservedOnLineProblem(problem)
    parameters = ClassifierSetParameters(problem.get_possible_actions())
    parameters.exploration_probability = .1
    parameters.do_GA_subsumption = True
    parameters.do_action_set_subsumption = True
    xcs = XCS(parameters)

    start_time = time.time()

    xcs.drive(problem)

    end_time = time.time()
    print("Total time:", end_time - start_time, "seconds")

