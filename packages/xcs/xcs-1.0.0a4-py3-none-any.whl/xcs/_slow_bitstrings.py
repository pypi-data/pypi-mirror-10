# -------------------------------------------------------------------------------
# Name:     xcs._slow_bitstrings
# Purpose:  Slow bit-string and bit-condition classes, implemented using standard
#           Python data types.
#
# Author:       Aaron Hosford
#
# Created:      5/9/2015
# Copyright:    (c) Aaron Hosford 2015, all rights reserved
# Licence:      Revised (3 Clause) BSD License
# -------------------------------------------------------------------------------

"""
xcs/_slow_bitstrings.py
(c) Aaron Hosford 2015, all rights reserved
Revised BSD License

Slow bit-string and bit-condition classes, implemented using standard Python
data types.

This file is part of the xcs package.
"""

__author__ = 'Aaron Hosford'
__all__ = [
    'BitString',
]


class BitString:
    """A hashable, immutable sequence of bits (Boolean values). This is the slower, Python-only implementation that
    doesn't depend on numpy.

    In addition to operations for indexing and iteration, implements standard bitwise operations, including & (bitwise
    and), | (bitwise or), ^ (bitwise xor), and ~ (bitwise not). Also implements the + operator, which acts like string
    concatenation.

    A bit string can also be cast as an integer or an ordinary string.
    """

    @classmethod
    def from_int(cls, value, length=None):
        """Create a bit string from an integer value. If the length parameter is provided, it determines the number of
        bits in the bit string. Otherwise, the minimum length required to represent the value is used."""

        # Progressively chop off low-end bits from the int, adding them to the bits list,
        # until we have reached the given length (if provided) or no more non-zero bits
        # remain (if length was not specified).
        bits = []
        while value:
            if length is not None and len(bits) >= length:
                break
            bits.append(value % 2)
            value >>= 1

        # Ensure that if length was provided, we have the correct number of bits in our list.
        if length:
            if len(bits) < length:
                bits.extend([0] * (length - len(bits)))
            elif len(bits) > length:
                bits = bits[:length]

        # Reverse the order of the bits, so the high-order bits go on the left and the low-
        # order bits go on the right, just as a person would expect when looking at the
        # number written out in binary.
        bits.reverse()

        return cls(bits)

    def __init__(self, bits):
        if isinstance(bits, int):
            self._bits = (False,) * bits
        elif isinstance(bits, BitString):
            # No need to make a copy because we use immutable bit arrays
            self._bits = bits._bits
        elif isinstance(bits, tuple) and all(isinstance(value, bool) for value in bits):
            self._bits = bits
        else:
            self._bits = tuple(bool(value) for value in bits)

        self._hash = None

    def any(self):
        """Returns True iff at least one bit is set."""
        return any(self._bits)

    def count(self):
        """Returns the number of bits set to True in the bit string."""
        return sum(self._bits)

    def __str__(self):
        # Overloads str(bitstring)
        return ''.join('1' if bit else '0' for bit in self._bits)

    def __repr__(self):
        # Overloads repr(bitstring)
        return type(self).__name__ + '(' + repr([int(bit) for bit in self._bits]) + ')'

    def __int__(self):
        # Overloads int(bitstring)
        value = 0
        for bit in self._bits:
            value <<= 1
            value += int(bit)
        return value

    def __len__(self):
        # Overloads len(bitstring)
        return len(self._bits)

    def __iter__(self):
        # Overloads iter(bitstring), and also, for bit in bitstring
        return iter(self._bits)

    def __getitem__(self, index):
        # Overloads bitstring[index]
        return self._bits[index]

    def __hash__(self):
        # Overloads hash(bitstring)
        if self._hash is None:
            self._hash = hash(self._bits)
        return self._hash

    def __eq__(self, other):
        # Overloads ==
        # noinspection PyProtectedMember
        return isinstance(other, BitString) and self._bits == other._bits

    def __ne__(self, other):
        # Overloads !=
        return not self == other

    def __and__(self, other):
        # Overloads &
        if isinstance(other, int):
            other = BitString.from_int(other, len(self._bits))
        elif not isinstance(other, BitString):
            other = BitString(other)
        bits = tuple(my_bit and other_bit for my_bit, other_bit in zip(self._bits, other._bits))
        return type(self)(bits)

    def __or__(self, other):
        # Overloads |
        if isinstance(other, int):
            other = BitString.from_int(other, len(self._bits))
        elif not isinstance(other, BitString):
            other = BitString(other)
        bits = tuple(my_bit or other_bit for my_bit, other_bit in zip(self._bits, other._bits))
        return type(self)(bits)

    def __xor__(self, other):
        # Overloads ^
        if isinstance(other, int):
            other = BitString.from_int(other, len(self._bits))
        elif not isinstance(other, BitString):
            other = BitString(other)
        bits = tuple(my_bit != other_bit for my_bit, other_bit in zip(self._bits, other._bits))
        return type(self)(bits)

    def __invert__(self):
        # Overloads unary ~
        bits = tuple(not bit for bit in self._bits)
        return type(self)(bits)

    def __add__(self, other):
        # Overloads +
        if isinstance(other, int):
            other = BitString.from_int(other, len(self._bits))
        elif not isinstance(other, BitString):
            other = BitString(other)
        bits = self._bits + other._bits
        return type(self)(bits)




