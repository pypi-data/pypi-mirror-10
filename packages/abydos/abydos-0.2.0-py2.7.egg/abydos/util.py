# -*- coding: utf-8 -*-

# Copyright 2014-2015 by Christopher C. Little.
# This file is part of Abydos.
#
# Abydos is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Abydos is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Abydos. If not, see <http://www.gnu.org/licenses/>.

"""abydos.util

The util module defines various utility functions for other modules within
Abydos, including:

    - prod -- computes the product of a collection of numbers (akin to sum)
    - jitter -- adds small random noise to each member of a list of numbers
        (ported from R's jitter function)
    - Rational -- a rational number class
"""
from __future__ import unicode_literals
from __future__ import division
import sys
import random
import numpy
import math
from ._compat import _unicode, _range, numeric_type, _long
if sys.version_info[0] == 3:
    # pylint: disable=redefined-builtin
    from functools import reduce    # pragma: no cover
    # pylint: enable=redefined-builtin


def prod(nums):
    """Product

    The product is Π(nums).

    Cf. https://en.wikipedia.org/wiki/Product_(mathematics)

    :param nums: a collection (list, tuple, set, etc.) of numbers
    :returns: the product of a nums
    """
    return reduce(lambda x, y: x*y, nums, 1)


def jitter(nums, factor=1, amount=None, min_val=None, max_val=None,
           rfunc='normal'):
    """Jitter

    Adapted from R documentation as this is ported directly from the R code:

    The result, say r, is r = x + numpy.random.uniform(-a, a) where n = len(x)
    and a is the amount argument (if specified).

    Let z = max(x) - min(x) (assuming the usual case). The amount a to be added
    is either provided as positive argument amount or otherwise computed from
    z, as follows:

    If amount == 0, we set a = factor * z/50 (same as S).

    If amount is None (default), we set a = factor * d/5 where d is the
    smallest difference between adjacent unique x values.

    Based on:
    http://svn.r-project.org/R/trunk/src/library/base/R/jitter.R

    :param x:  numeric collection to which jitter should be added
    :param factor:  numeric
    :param amount:  numeric; if positive, used as amount (see below),
        otherwise, if = 0 the default is factor * z/50.
        Default (NULL): factor * d/5 where d is about the smallest difference
        between x values.
    :param min_val: the minimum permitted value in the returned list
    :param max_val: the maximum permitted value in the returned list
    :param rand: a string or function to indicate the random distribution used:
        'normal' (default), 'uniform' (standard in the R version),
        or 'laplace' (requires Numpy)
        If a function is supplied, it should take one argument (the value
        passed as amount).
    :returns: a list of numbers with random noise added, according to the R
        jitter function
    """
    if isinstance(nums, numeric_type):
        return jitter([nums])[0]
    if len(nums) == 0:
        return []
    if sum([isinstance(i, numeric_type) for i in nums]) != len(nums):
        raise AttributeError('All members of nums must be numeric.')

    rng = (min(nums), max(nums))
    diff = rng[1]-rng[0]
    if diff == 0:
        diff = abs(rng[0])
    if diff == 0:
        diff = 1

    if min_val is None:
        min_val = rng[0]-diff
    elif rng[0] < min_val:
        raise AttributeError('Minimum of nums is less than min_val.')

    if max_val is None:
        max_val = rng[1]+diff
    elif rng[1] > max_val:
        raise AttributeError('Maximum of nums is greater than max_val.')

    if amount is None:
        ndigits = int(3 - math.floor(math.log10(diff)))
        snums = sorted(set([round(i, ndigits) for i in nums]))
        if len(snums) == 1:
            if snums[0] != 0:
                scaler = snums[0]/10
            else:
                scaler = diff/10
        else:
            scaler = min([j - snums[i - 1] for i, j in enumerate(snums)
                          if i > 0])
        amount = factor/5 * abs(scaler)
    elif amount == 0:
        amount = factor * (diff/50)

    amount = abs(amount)

    def _rand_uniform():
        """Uniform distribution RNG

        :returns: random number
        :rtype: float
        """
        return random.uniform(-amount, amount)

    def _rand_laplace():
        """Laplace distribution RNG

        :returns: random number
        :rtype: float
        """
        # pylint: disable=no-member
        return numpy.random.laplace(0, amount)
        # pylint: enable=no-member

    def _rand_normal():
        """Normal distribution RNG

        :returns: random number
        :rtype: float
        """
        return random.normalvariate(0, amount)

    def _rand_user():
        """User-defined RNG

        :returns: random number
        :rtype: float
        """
        return rfunc(amount)

    if callable(rfunc):
        _rand = _rand_user
    elif rfunc == 'uniform':
        _rand = _rand_uniform
    elif rfunc == 'laplace':
        _rand = _rand_laplace
    else:
        _rand = _rand_normal

    newnums = [i + _rand() for i in nums]

    # Check that we haven't introduced values that exceed specified bounds
    # and aren't too far outside of normal
    # (This is an addition to the standard R algorithm)
    for i in _range(len(newnums)):
        while newnums[i] < min_val or newnums[i] > max_val:
            newnums[i] = (newnums[i] + _rand())  # pragma: no cover

    # In the unlikely event that two equal values are in the list, try again
    if len(newnums) != len(set(newnums)):
        newnums = jitter(nums, factor, amount,
                         min_val, max_val)  # pragma: no cover

    return newnums


class Rational(object):
    """Rational number object supporting arithmetic and comparison operations
    """

    # pylint: disable=invalid-name
    p = _long(0)
    q = _long(1)

    def __init__(self, p=0, q=1):
        """Construct a Rational object from p (the numerator) and q (the
        denominator

        A Rational object can be constructed with:
        - ints: Rational(p, q), where p is the numerator and q the denominator
        - a float: Rational(1.25) or Rational(1, 1.25)
        - a string: Rational('1/4') or Rational('1.25')
        - a single int/long: Rational(1) or Rational(12)

        :params p: numerator (or a string or float)
        :params q: denominator
        """
        # First try to interpret a string as a numeric value
        if isinstance(p, (_unicode, str)):
            # pylint: disable=maybe-no-member
            p = p.replace(' ', '')
            if '/' in p:
                p, q = p.split('/', 1)
                if '.' in q:
                    q = float(q)
                else:
                    q = _long(q)
            if '.' in p:
                p = float(p)
            else:
                p = _long(p)

        # Then divide determine numeric values for p & q
        if isinstance(p, (int, _long)) and isinstance(q, (int, _long)):
            self.p = _long(p)
            self.q = _long(q)
        elif isinstance(p, float) and isinstance(q, (int, _long)):
            pfloat_p, pfloat_q = p.as_integer_ratio()
            self.p = _long(pfloat_p)
            self.q = _long(pfloat_q) * _long(q)
        elif isinstance(p, (int, _long)) and isinstance(q, float):
            qfloat_p, qfloat_q = q.as_integer_ratio()
            self.p = _long(p) * _long(qfloat_q)
            self.q = _long(qfloat_p)
        elif isinstance(p, float) and isinstance(q, float):
            pfloat_p, pfloat_q = p.as_integer_ratio()
            qfloat_p, qfloat_q = q.as_integer_ratio()
            self.p = _long(pfloat_p) * _long(qfloat_q)
            self.q = _long(pfloat_q) * _long(qfloat_p)
        else:
            raise AttributeError('Unsupported values, both p and q must be ' +
                                 'of type int, long, or float or p must be ' +
                                 'a string representation of a fraction')

        # Finally, simplify by reducing with the GCD
        self._simplify()

    def numerator(self):
        """Get the numerator (p)

        :returns: the numerator p
        :rtype: int
        """
        return self.p

    def denominator(self):
        """Get the denominator (q)

        :returns: the denominator q
        :rtype: int
        """
        return self.q

    def _gcd(self, p=None, q=None):
        """Greatest common denominator (GCD)

        By default, this computes the GCD of the Rational's current
        numerator & denominator, but can also accept p and/or q values and
        calculate their GCD.

        :param p: the numerator
        :param q: the denominator
        :returns: the greatest common denominator GCD of integers p and q
        :rtype: int
        """
        if not p:
            p = self.p
        if not q:
            q = self.q
        while q != 0:
            p, q = q, p % q
        return p

    def _simplify(self):
        """Update p and q by dividing both by their GCD

        :returns: None
        """
        gcd = self._gcd(self.p, self.q)
        self.p //= gcd
        self.q //= gcd

    def __eq__(self, other):
        """equals operator (==)

        :returns: True if self == other (numerically)
        :rtype: bool
        """
        if not isinstance(other, Rational):
            other = Rational(other)
        if self.p == other.p and self.q == other.q:
            return True
        else:
            return False

    def __ne__(self, other):
        """not-equal operator (!=)

        :returns: True if self != other
        :rtype: bool
        """
        return not self == other

    def __lt__(self, other):
        """less-than operator (<)

        :returns: True if self < other
        :rtype: bool
        """
        if not isinstance(other, Rational):
            other = Rational(other)
        return self.p*other.q < self.q*other.p

    def __le__(self, other):
        """less-than or equal operator (<=)

        :returns: True if self <= other
        :rtype: bool
        """
        if not isinstance(other, Rational):
            other = Rational(other)
        return self.p*other.q <= self.q*other.p

    def __gt__(self, other):
        """greater than operator (>)

        :returns: True if self > other
        :rtype: bool
        """
        if not isinstance(other, Rational):
            other = Rational(other)
        return self.p*other.q > self.q*other.p

    def __ge__(self, other):
        """greater-than or equal operator (>=)

        :returns: True if self >= other
        :rtype: bool
        """
        if not isinstance(other, Rational):
            other = Rational(other)
        return self.p*other.q >= self.q*other.p

    def __neg__(self):
        """negation operator (-)

        :returns: a Rational object after negating the numerator
        :rtype: Rational
        """
        return Rational(-self.p, self.q)

    def __add__(self, other):
        """addition operator (+)

        :returns: a Rational object after adding other to self
        :rtype: Rational
        """
        if not isinstance(other, Rational):
            other = Rational(other)
        if self.q == other.q:
            p = self.p + other.p
            q = self.q
        else:
            p = self.p * other.q + other.p * self.q
            q = self.q * other.q
        return Rational(p, q)

    def __radd__(self, other):
        """right addition operator (+)

        :returns: a Rational object after adding self to other
        :rtype: Rational
        """
        return self + other

    def __sub__(self, other):
        """subtraction operator (-)

        :returns: a Rational object after subtracting other from self
        :rtype: Rational
        """
        if not isinstance(other, Rational):
            other = Rational(other)
        if self.q == other.q:
            p = self.p - other.p
            q = self.q
        else:
            p = self.p * other.q - other.p * self.q
            q = self.q * other.q
        return Rational(p, q)

    def __rsub__(self, other):
        """right subtraction operator (-)

        :returns: a Rational object after subtracting self from other
        :rtype: Rational
        """
        return -self + other

    def __mul__(self, other):
        """multiplication operator (*)

        :returns: a Rational object after multiplying self by other
        :rtype: Rational
        """
        if not isinstance(other, Rational):
            other = Rational(other)
        p = self.p * other.p
        q = self.q * other.q
        return Rational(p, q)

    def __rmul__(self, other):
        """right multiplication operator (*)

        :returns: a Rational object after multiplying other by self
        :rtype: Rational
        """
        return self * other

    def __div__(self, other):
        """division operator (/)

        :returns: a Rational object after dividing self by other
        :rtype: Rational
        """
        return self.__truediv__(other)

    def __rdiv__(self, other):
        """right division operator (/)

        :returns: a Rational object after dividing other by self
        :rtype: Rational
        """
        return Rational(other).__div__(self)

    def __truediv__(self, other):
        """true division operator (/ when __future__.division)

        :returns: a Rational object after dividing self by other
        :rtype: Rational
        """
        if not isinstance(other, Rational):
            other = Rational(other)
        p = self.p * other.q
        q = self.q * other.p
        return Rational(p, q)

    def __rtruediv__(self, other):
        """right true division operator (/ when __future__.division)

        :returns: a Rational object after dividing other by self
        :rtype: Rational
        """
        return Rational(other).__truediv__(self)

    def __pow__(self, exponent):
        """exponentiation operator (**)

        :returns: a Rational object after raising self to the power of exponent
        :rtype: Rational
        """
        if isinstance(exponent, Rational):
            exponent = float(exponent)
        return Rational(self.p**exponent, self.q**exponent)

    def __rpow__(self, base):
        """right exponentiation operator (**)

        :returns: a Rational object after raising base to the power of self
        :rtype: Rational
        """
        exponent = float(self)
        return Rational(base**exponent)

    def __lshift__(self, shift):
        """left shift operator (<<)

        This is equivalent to left bit-shifting the numerator only or
        right-bit-shifting the denominator only.

        :returns: a Rational object after left bit shifting the numerator
        :rtype: Rational
        """
        p = self.p << shift
        q = self.q
        return Rational(p, q)

    def __rshift__(self, shift):
        """right shift operator (>>)

        This is equivalent to right bit-shifting the numerator only or
        left bit-shifting the denominator only.

        :returns: a Rational object after left bit shifting the denominator
        :rtype: Rational
        """
        p = self.p
        q = self.q << shift
        return Rational(p, q)

    def __int__(self):
        """cast to int

        :returns: an int of the Rational, after calculating its floor
        :rtype: int
        """
        return int(self.p//self.q)

    def __float__(self):
        """cast to float

        :returns: a float approximation of the Rational
        :rtype: float
        """
        return float(self.p/self.q)

    def __str__(self):
        """cast to str

        :returns: a string representation of the Rational
        :rtype: str
        """
        if self.q == 1:
            return str(self.p)
        else:
            return '{}/{}'.format(self.p, self.q)

    def __repr__(self):
        """cast to a str representation

        :returns: a string representation of the Rational
        :rtype: str
        """
        return self.__str__()
