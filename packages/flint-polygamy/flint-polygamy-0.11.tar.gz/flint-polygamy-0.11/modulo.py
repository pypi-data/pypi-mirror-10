

import exceptions
import numbers

import ring
import unicode_rendering

class ModularInverseError(exceptions.ArithmeticError):
    pass

class InverseOfZeroError(exceptions.ArithmeticError):
    pass

def multiplicative_inverse(r, n):
    '''Find the multiplicative inverse of r in the field of integers
    modulo n, ie an integer s such that s<n and s*r = 1 (mod n).'''
    if r == 0:
        raise InverseOfZeroError('cannot compute inverse of zero')
    gcd,a,b = ring.extended_gcd(r, n)
    if r*a % n != 1:
        raise ModularInverseError('%s has no inverse modulo %s' % (r,n))
    return a % n


class ModuloIntegerType(type):
    """The metaclass for the ModuloInteger class, which makes it
    possible to construct types like ModuloInteger[41]."""
    def __getitem__(cls, n):
        return make_modulo_type(n)


class IntegerRingType(ModuloIntegerType):
    """The metaclass for classes representing the ring of integers
    modulo some specific N."""
    def __unicode__(cls):
        return 'ModuloInteger[%d]' % cls._n
    def __str__(cls):
        return str(cls).encode('utf-8')
    def __repr__(cls):
        return str(cls)
    def __eq__(cls, rhs):
        return isinstance(rhs, IntegerRingType) and cls._n == rhs._n
    def __ne__(cls, rhs):
        return not (cls == rhs)
    def __instancecheck__(cls, x):
        return issubclass(type(x), ModuloInteger) and x.n == cls._n


def make_modulo_type(n):
    """Construct a type representing integers modulo n. Such types
    are are derived from ModuloInteger and have a constructor taking
    a single integer r."""
    def __init__(self, r):
        ModuloInteger.__init__(self, r, n)

    name = 'ModuloInteger_%d' % n
    bases = (ModuloInteger,)
    dict = {
        '__init__': __init__,
        '_n' : n
    }
    return IntegerRingType(name, bases, dict)


class ModuloInteger(object, metaclass=ModuloIntegerType):
    """Represents an element of the ring of integers modulo n."""

    _n = None  # For compatibility with specific integer rings

    def __init__(self, r, n):
        '''Construct the integer r (mod n).'''
        self._r = int(r) % int(n)
        self._n = int(n)

    @property
    def r(self):
        return self._r

    @property
    def n(self):
        return self._n

    @property
    def inverse(self):
        '''Return this object's multiplicative inverse, which is an
        integer s such that self*s = 1 (mod n).'''
        return ModuloInteger(multiplicative_inverse(self._r, self._n), self._n)

    def __add__(self, rhs):
        return ModuloInteger(self._r + int(rhs), self._n)
    def __radd__(self, lhs):
        return ModuloInteger(int(lhs) + self._r, self._n)

    def __sub__(self, rhs):
        return ModuloInteger(self._r - int(rhs), self._n)
    def __rsub__(self, lhs):
        return ModuloInteger(int(lhs) - self._r, self._n)

    def __neg__(self):
        return ModuloInteger(self._n - self._r, self._n)

    def __mul__(self, rhs):
        return ModuloInteger(self._r * int(rhs), self._n)
    def __rmul__(self, lhs):
        return ModuloInteger(int(lhs) * self._r, self._n)

    def __truediv__(self, rhs):
        return ModuloInteger(self._r * multiplicative_inverse(int(rhs), self._n), self._n)
    def __rtruediv__(self, lhs):
        return ModuloInteger(int(lhs) * multiplicative_inverse(self._r, self._n), self._n)

    def __div__(self, rhs):
        return ModuloInteger(self._r * multiplicative_inverse(int(rhs), self._n), self._n)
    def __rdiv__(self, lhs):
        return ModuloInteger(int(lhs) * multiplicative_inverse(self._r, self._n), self._n)

    def __floordiv__(self, rhs):
        return self / rhs
    def __rfloordiv__(self, lhs):
        return rhs / self

    def __int__(self):
        return int(self._r)
    def __long__(self):
        return int(self._r)
    def __float__(self):
        return float(self._r)

    def __cmp__(self, rhs):
        return cmp(self._r, int(rhs))
    def __bool__(self):
        return self._r != 0

    def __str__(self):
        return str(self._r)
    def __repr__(self):
        return '%s(%d,%d)' % (self.__class__.__name__, self._r, self._n)

    #
    # Implementation of numbers.Integral ABC
    #

    @property
    def real(self):
        return self._r

    @property
    def imag(self):
        return 0

    @property
    def numerator(self):
        return self._r

    @property
    def denominator(self):
        return 1

    def conjugate(self):
        return self


# Tell the numbers module that ModuloIntegers can be treated as integer-like.
# This means that:
#   isinstance(ModuloInteger(r,n), numbers.Integral) -> True
#   issubclass(ModuloInteger, numbers.Integral) -> True
numbers.Integral.register(ModuloInteger)
