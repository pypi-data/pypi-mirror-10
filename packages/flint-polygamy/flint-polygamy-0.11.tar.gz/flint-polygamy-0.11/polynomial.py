import abc
import numbers
import fractions
import itertools
import ast
import operator
import collections
from functools import reduce
import numpy as np

from . import unicode_rendering
from . import compilation

class OrderingError(Exception):
    pass


class DivisionError(Exception):
    pass


class VariableMismatchError(Exception):
    pass


class CoerceError(Exception):
    pass


class GrobnerBasisTooLargeError(Exception):
    pass


def type_rank(t):
    if not isinstance(t, type):
        return 4
    if issubclass(t, numbers.Integral):
        return 1
    elif issubclass(t, numbers.Rational):
        return 2
    elif issubclass(t, numbers.Real):
        return 3
    else:
        return 4


def result_type(*types):
    return max(types, key=lambda x: type_rank(x))


def product(xs):
    """Compute the product of the elements of XS."""
    return reduce(operator.mul, xs)


def compare_leftmost(A, B):
    assert len(A) == len(B)
    for a,b in zip(A, B):
        if a > b:
            return 1
        elif a < b:
            return -1
    return 0


def compare_rightmost(A, B):
    assert len(A) == len(B)
    for a,b in zip(A[::-1], B[::-1]):
        if a > b:
            return 1
        elif a < b:
            return -1
    return 0


def can_divide_monomial(A, B):
    """True if B divides A."""
    assert len(A) == len(B)
    for i in range(len(A)):
        if B[i] > A[i]:
            return False
    return True


def divide_monomial(A, B):
    """Divide the monomial A by the monomial B."""
    return tuple(A[i] - B[i] for i in range(len(A)))


def multiply_monomial(A, B):
    """Multiply the monomial A by the monomial B."""
    return tuple(A[i] + B[i] for i in range(len(A)))


def evaluate_monomial(m, x):
    """Evaluate the monomial m at x."""
    return product(xi**mi for mi, xi in zip(m, x))


def as_monomial(x):
    """Convert scalars, terms, or monomials to polynomials."""
    if isinstance(x, Monomial):
        # Interpret scalars as constant polynomials
        return x
    else:
        try:
            return Monomial(*x)
        except TypeError:
            raise TypeError('cannot convert %s to monomial' % type(x))


def as_term(x, num_vars):
    """Convert scalars, terms, or monomials to polynomials."""
    if isinstance(x, numbers.Real):
        # Interpret scalars as constant polynomials
        return Term(x, (0,)*num_vars)
    elif isinstance(x, tuple):
        # Interpret tuples as monomials
        return Term(1, x)
    elif isinstance(x, Term):
        # Interpret terms as length-1 polynomials
        return x
    else:
        raise CoerceError('cannot convert %s to term' % type(x))


def as_polynomial(x, num_vars=None, ctype=None):
    """Convert scalars, terms, or monomials to polynomials."""
    if isinstance(x, numbers.Real):
        # Interpret scalars as constant polynomials
        if num_vars is None:
            raise VariableMismatchError('when passing scalars you must specify num_vars')
        return Polynomial.constant(x, num_vars, ctype=ctype)

    elif isinstance(x, tuple):
        # Interpret tuples as monomials
        if num_vars is not None and len(x) != num_vars:
            raise VariableMismatchError('found %d vars but expected %d' % (len(x), num_vars))
        return Polynomial.from_monomial(x, ctype=ctype)

    elif isinstance(x, Term):
        # Interpret terms as length-1 polynomials
        if num_vars is not None and x.num_vars != num_vars:
            raise VariableMismatchError('found %d vars but expected %d' % (x.num_vars, num_vars))
        return Polynomial.from_term(x, ctype=ctype)

    elif isinstance(x, Polynomial):
        if num_vars is not None and x.num_vars != num_vars:
            raise VariableMismatchError('found %d vars but expected %d' % (x.num_vars, num_vars))
        return x

    else:
        raise CoerceError('cannot convert %s to polynomial' % type(x))


class MonomialOrdering(object, metaclass=abc.ABCMeta):
    """Represents an ordering over n-tuples of integers."""
    @abc.abstractmethod
    def __call__(self, a, b):
        "__Call__ two tuples and return -1, 0, or 1"
        pass


class LexOrdering(MonomialOrdering):
    """Implements "lex" monomial ordering."""
    def __call__(self, a, b):
        return compare_leftmost(a, b)


class GrlexOrdering(MonomialOrdering):
    """Implements "grlex" monomial ordering."""
    def __call__(self, a, b):
        if sum(a) > sum(b):
            return 1
        elif sum(a) < sum(b):
            return -1
        else:
            return compare_leftmost(a, b)


class GrevlexOrdering(MonomialOrdering):
    """Implements "grevlex" monomial ordering."""
    def __call__(self, a, b):
        if sum(a) > sum(b):
            return 1
        elif sum(a) < sum(b):
            return -1
        else:
            return compare_rightmost(b, a)  # yes this is (b,a) not (a,b)


class DegreeOrdering(MonomialOrdering):
    """Orders univariate monomials by their degree. This is not a true
    monomial ordering because it is only valid for univariate
    monomials."""
    def __call__(self, a, b):
        assert len(a) == 1
        assert len(b) == 1
        return cmp(a[0], b[0])


class VariableReordering(MonomialOrdering):
    def __init__(self, var_ordering, monomial_ordering):
        self._vars = var_ordering
        self._inner = monomial_ordering
    def __call__(self, a, b):
        aa = tuple(a[i] for i in self._vars)
        bb = tuple(b[i] for i in self._vars)
        return self._inner(aa, bb)


# TODO problems to solve:
#   the need to keep passing around ordering objects
#   class to represent polynomial systems
#   the need to keep managing num_vars
#   inability to construct polynomials with different vars independently


class Monomial(object):
    """Represents a multivariate monomial of the form
    x1^a1 * ... * xn^an."""

    def __init__(self, *exponents):
        """Initializes a monomial with the given exponent vector."""
        if not all(isinstance(a, numbers.Integral) for a in exponents):
            raise TypeError('monomial exponents must be integers')
        if not all(a >= 0 for a in exponents):
            raise TypeError('monomial exponents must be non-negative')
        self._exponents = tuple(exponents)

    @property
    def exponents(self):
        return self._exponents

    @property
    def total_degree(self):
        """Return the sum of the exponents in this term."""
        return sum(self)

    def __eq__(self, rhs):
        rhs = as_monomial(rhs)
        return self.exponents == rhs.exponents

    def __ne__(self, rhs):
        return not (self == rhs)

    def __hash__(self):
        """Returns the hash code for the underlying exponent tuple."""
        return hash(self.exponents)

    def __iter__(self):
        return iter(self.exponents)

    def __len__(self):
        return len(self.exponents)

    def __getitem__(self, index):
        return self.exponents[index]

    def __mul__(self, rhs):
        rhs = as_monomial(rhs)
        return Monomial(*(a+b for a, b in zip(self, rhs)))

    def __rmul__(self, rhs):
        return as_monomial(rhs) * self

    def __truediv__(self, rhs):
        rhs = as_monomial(rhs)
        assert rhs.divides(self)
        return Monomial(*(a-b for a, b in zip(self, rhs)))

    def __rtruediv__(self, rhs):
        return as_monomial(rhs) / self

    def __call__(self, *xs):
        """Evaluate this monomial at x."""
        assert len(xs) == len(self)
        return product(x**a for x, a in zip(xs, self))

    def divides(self, rhs):
        """Return true if each exponent in this term is greater or
        equal than the corresponding term in rhs."""
        rhs = as_term(rhs)
        assert len(rhs) == len(self)
        return all(a <= b for a, b in zip(self, rhs))

    def copy(self):
        """Return a copy of this term."""
        return Term(self.coef, self.monomial, self.ctype)

    def python_expression(self, varnames):
        """Construct a python expression string representing this polynomial."""
        assert len(varnames) == len(self)
        return '*'.join(['%s**%d' % (var, a)
                         for var, a in zip(varnames, self)
                         if a > 0])

    def format(self, use_superscripts=True):
        """Construct a string representation of this polynomial."""
        if self.total_degree == 0:
            return '1'
        strings = []
        for var_index, exponent in enumerate(self):
            if exponent >= 1:
                if len(self) <= 4:
                    var = 'xyzw'[var_index]
                elif use_superscripts:
                    var = 'x'+unicode_rendering.subscript(var_index)
                else:
                    var = 'x'+str(var_index)

                if exponent == 1:
                    strings.append(var)
                elif use_superscripts:
                    strings.append(var + unicode_rendering.superscript(exponent))
                else:
                    strings.append(var + '^' + str(exponent))

        if use_superscripts:
            return ''.join(strings)
        else:
            return '*'.join(strings)

    def __str__(self):
        return self.format()

    def __repr__(self):
        return str(self)


class Term(object):
    """Represents a multivariate polynomial term of the form
    c * x1^a1 * ... * xn^an."""

    @classmethod
    def from_monomial(cls, monomial):
        return Term(1, monomial)

    def __init__(self, coef, monomial, ctype=None):
        #if not all(isinstance(m, numbers.Integral) for m in monomial):
        #    raise ValueError('monomial exponents should be integers')
        self._monomial = tuple(monomial)
        self._ctype = ctype or type(coef)
        if ctype is not None and not isinstance(coef, ctype):
            self._coef = ctype(coef)
        else:
            self._coef = coef
        #assert isinstance(self._coef, numbers.Real), 'coef='+str(self._coef)
        #assert all(isinstance(exponent, numbers.Integral) for exponent in self._monomial)

    @property
    def coef(self):
        return self._coef

    @coef.setter
    def coef(self, value):
        if type(value) == self._ctype:
            self._coef = value
        else:
            self._coef = self._ctype(value)

    @property
    def monomial(self):
        return self._monomial

    @property
    def ctype(self):
        return self._ctype

    @property
    def num_vars(self):
        return len(self._monomial)

    def astype(self, ctype):
        """If ctype == self.ctype then return a reference to this
        object, otherwise return a copy of this term converted to the
        given type."""
        if ctype == self.ctype:
            return self
        else:
            return Term(self.coef, self.monomial, ctype=ctype)

    def __eq__(self, rhs):
        rhs = as_term(rhs, len(self.monomial))
        return self.coef == rhs.coef and self.monomial == rhs.monomial

    def __ne__(self, rhs):
        return not (self == rhs)

    def _multiply_by(self, rhs):
        rhs = as_term(rhs, self.num_vars)
        self.coef *= rhs.coef
        self._monomial = multiply_monomial(self.monomial, rhs.monomial)

    def _divide_by(self, rhs):
        rhs = as_term(rhs, self.num_vars)
        if not rhs.divides(self):
            raise DivisionError('Cannot divide %s by %s' % (self, rhs))
        self.coef /= rhs.coef
        self._monomial = divide_monomial(self.monomial, rhs.monomial)

    def _negate(self):
        self.coef = -self.coef

    def __mul__(self, rhs):
        rhs = as_term(rhs, len(self.monomial))
        result = self.copy()
        result._multiply_by(rhs)
        return result

    def __truediv__(self, rhs):
        rhs = as_term(rhs, len(self.monomial))
        result = self.copy()
        result._divide_by(rhs)
        return result

    def __neg__(self):
        return Term(-self.coef, self.monomial, self.ctype)

    def __call__(self, *xs):
        """Evaluate this term at x."""
        assert len(xs) == len(self.monomial)
        return self.coef * evaluate_monomial(self.monomial, xs)

    def evaluate_partial(self, var_index, value):
        """Create a new term with by evaluating this term at the given
        value for the given variable. The result formally contains the
        same number of variables but the evaluated variable always has
        an exponent of zero."""
        new_coef = self.coef * value**self.monomial[var_index]
        new_monomial = list(self.monomial)
        new_monomial[var_index] = 0
        return Term(new_coef, tuple(new_monomial), self.ctype)

    def divides(self, rhs):
        rhs = as_term(rhs, len(self.monomial))
        return can_divide_monomial(rhs.monomial, self.monomial)

    @property
    def total_degree(self):
        """Return the sum of the exponents in this term."""
        return sum(self.monomial)

    def copy(self):
        """Return a copy of this term."""
        return Term(self.coef, self.monomial, self.ctype)

    def python_expression(self, varnames):
        """Construct a python expression string representing this polynomial."""
        assert len(varnames) == len(self.monomial)
        return '*'.join([str(self.coef)] + ['%s**%d' % (var,exponent)
                                            for var,exponent in zip(varnames,self.monomial)
                                            if exponent>0])

    def format(self, use_superscripts=True):
        """Construct a string representation of this polynomial."""
        if self.total_degree == 0:
            return str(self.coef)
        prefix = ''
        strings = []
        if self.coef == -1:
            prefix = '-'
        elif self.coef != 1:
            strings.append(str(self.coef))
        for var_index, exponent in enumerate(self.monomial):
            if exponent >= 1:
                if len(self.monomial) <= 4:
                    var = 'xyzw'[var_index]
                elif use_superscripts:
                    var = 'x'+unicode_rendering.subscript(var_index)
                else:
                    var = 'x'+str(var_index)

                if exponent == 1:
                    strings.append(var)
                elif use_superscripts:
                    strings.append(var + unicode_rendering.superscript(exponent))
                else:
                    strings.append(var + '^' + str(exponent))
        if use_superscripts:
            return prefix + ''.join(strings)
        else:
            return prefix + '*'.join(strings)

    def __str__(self):
        return self.format()

    def __repr__(self):
        return str(self)


class ComparableTerm(object):
    @classmethod
    def factory(cls, ordering):
        def build(term):
            return ComparableTerm(ordering, term)
        return build
    def __init__(self, ordering, term):
        self._ordering = ordering
        self._term = term
    def __lt__(self, rhs):
        return self._ordering(self._term.monomial, rhs._term.monomial) == -1
    def __gt__(self, rhs):
        return self._ordering(self._term.monomial, rhs._term.monomial) == 1


class CoefficientView(object):
    """Represents a view into a monomial -> term dictionary."""
    def __init__(self, terms, num_vars, ctype):
        self._term_dict = terms
        self._num_vars = num_vars
        self._ctype = ctype

    def __len__(self):
        return len(self._term_dict)

    def __iter__(self):
        for term in self._term_dict.values():
            yield term.coef

    def __getitem__(self, monomial):
        """Get the coefficient of the given monomial in this
        polynomial, or zero if this polynomial does not contain the
        given monomial."""
        assert len(monomial) == self._num_vars
        term = self._term_dict.get(monomial, None)
        if term is None:
            return 0
        else:
            return term.coef

    def __setitem__(self, monomial, coef):
        """Get the coefficient of the given monomial in this
        polynomial, or zero if this polynomial does not contain the
        given monomial."""
        assert len(monomial) == self._num_vars
        term = self._term_dict.get(monomial, None)
        if term is None:
            term = Term(coef, monomial, self._ctype)
            self._term_dict[monomial] = term
        else:
            term.coef = coef
        if not term.coef:
            del self[monomial]

    def __delitem__(self, monomial):
        del self._term_dict[monomial]


class Polynomial(object):
    """Represents a polynomial in one or more variables."""
    def __init__(self, num_vars, ctype=None):
        self._num_vars = num_vars
        self._ctype = ctype or fractions.Fraction
        self._term_dict = {}
        self._coef_view = CoefficientView(self._term_dict, num_vars, ctype)

    @classmethod
    def create(cls, terms=[], num_vars=None, ctype=None):
        if num_vars is None:
            terms = list(terms)
            assert len(terms) > 0, 'to create an empty polynomial you must pass num_vars'
            num_vars = len(terms[0].monomial)

        if ctype is None:
            terms = list(terms)
            if len(terms) > 0:
                ctype = terms[0].ctype

        # there may be duplicate terms so add them one by one
        p = Polynomial(num_vars, ctype)
        p._add_terms(terms)
        return p

    @classmethod
    def constant(cls, c, num_vars, ctype=None):
        """Construct the constant polynomial p(x)=c."""
        return Polynomial.create([Term(c, (0,)*num_vars)], num_vars, ctype)

    @classmethod
    def coordinate(cls, var_index, num_vars, ctype=None):
        """Construct a polynomial corresponding to the i-th variable."""
        assert 0 <= var_index < num_vars
        return Polynomial.create([Term(1, tuple(int(i==var_index) for i in range(num_vars)))], num_vars, ctype)

    @classmethod
    def coordinates(cls, num_vars, ctype=None):
        """Construct a polynomial corresponding to the i-th variable."""
        return [Polynomial.coordinate(i, num_vars, ctype) for i in range(num_vars)]

    @classmethod
    def from_monomial(cls, monomial, coefficient=1, ctype=None):
        """Construct a polynomial from a single monomial."""
        return Polynomial.create([Term(coefficient, monomial)], len(monomial), ctype)

    @classmethod
    def from_term(cls, term, ctype=None):
        """Construct a polynomial from a single term."""
        return Polynomial.create([term], len(term.monomial), ctype)

    @property
    def num_vars(self):
        """Return the number of variables in the polynomial ring in
        which this polynomial resides."""
        return self._num_vars

    @property
    def ctype(self):
        return self._ctype

    @property
    def total_degree(self):
        """Return the sum of the exponents of the highest-degree term in this polynomial."""
        if len(self) == 0:
            return 0
        else:
            return max(term.total_degree for term in self)

    @property
    def monomials(self):
        return self._term_dict.keys()

    @property
    def coefficients(self):
        return self._coef_view

    def copy(self, ctype=None):
        """Return a copy of this polynomial."""
        return Polynomial.create((term.copy() for term in self),
                                 self.num_vars,
                                 ctype or self.ctype)

    def astype(self, ctype):
        """Return a copy of this polynomial in which each coefficient
        is cast to the given type."""
        if ctype == self.ctype:
            return self
        else:
            return Polynomial.create((term.astype(ctype) for term in self),
                                     self.num_vars,
                                     ctype)

    def sorted_terms(self, ordering=None, reverse=False):
        """Return a collection of Term objects representing terms in
        this polynomial, sorted by the given ordering (lowest ordered
        term first)."""
        return sorted(self,
                      key=ComparableTerm.factory(self._resolve_ordering(ordering)),
                      reverse=reverse)

    def leading_term(self, ordering=None):
        """Return a Term object representing the term in this
        polynomial that is sorted first by the given ordering."""
        return max(self,
                   key=ComparableTerm.factory(self._resolve_ordering(ordering)))

    def trailing_terms(self, ordering=None):
        """Return a polynomial consisting of all terms in this
        polynomial other than the leading term."""
        return Polynomial.create(self.sorted_terms(self._resolve_ordering(ordering))[:-1],
                                 self.num_vars,
                                 self.ctype)

    def divides(self, rhs, ordering=None):
        return any([ self.leading_term(ordering).divides(term) for term in rhs ])

    def can_divide_by(self, rhs, ordering=None):
        return rhs.divides(self)

    def divide_by(self, rhs, ordering=None):
        rhs = as_polynomial(rhs, self.num_vars)
        if rhs == 0:
            raise DivisionError('cannot divide by zero')
        if self.ctype == int or rhs.ctype == int:
            print('Warning: polynomial division with integer coefs will lead to unexpected round-off')

        self._assert_compatible(rhs)

        lt_rhs = rhs.leading_term(ordering)
        tt_rhs = rhs.trailing_terms(ordering)

        dividend = self.copy()
        remainder = Polynomial(self.num_vars, self.ctype)
        quotient = Polynomial(self.num_vars, self.ctype)

        while len(dividend) > 0:
            lt_dividend = dividend._pop_leading_term(ordering)
            if lt_rhs.divides(lt_dividend):
                factor = lt_dividend / lt_rhs
                quotient._add_term_unchecked(factor)
                dividend -= tt_rhs * factor
            else:
                remainder._add_term_unchecked(lt_dividend)

        return quotient, remainder

    def partial_derivative(self, var_index):
        """Return a polynomial representing the partial derivative of
        this polynomial with respect to the its i-th variable."""
        assert var_index >= 0
        assert var_index < self.num_vars

        result = Polynomial(self.num_vars, self.ctype)
        for term in self:
            if term.monomial[var_index] > 0:
                derivative_coef = term.coef * term.monomial[var_index]
                derivative_monomial = tuple(exponent - int(i==var_index)
                                            for i,exponent in enumerate(term.monomial))
                result.coefficients[derivative_monomial] += derivative_coef
        return result

    def partial_derivatives(self):
        return [self.partial_derivative(i) for i in range(self.num_vars)]

    def masked(self, mask):
        """Return a new polynomial formed by dropping each variable such
        that mask[i] evaluates to False."""
        result = Polynomial(sum(mask), self.ctype)
        for term in self:
            squeezed_monomial = tuple(v for i, v in enumerate(term.monomial) if mask[i])
            result.coefficients[squeezed_monomial] += term.coef
        return result

    def drop(self, var_index):
        """Return a new polynomial formed by dropping the i-th variable
         from all terms."""
        return self.masked([i != var_index for i in range(self.num_vars)])

    def squeezed(self):
        """Return a new polynomial with a (possibly) smaller number of
        variables formed by eliminating variables that do not appear
        in any term."""
        mask = [ any(term.monomial[i]>0 for term in self)
                 for i in range(self.num_vars) ]
        return self.masked(mask)

    def normalized(self, ordering=None):
        """Return a copy of this polynomial in which the leading coefficient is 1."""
        if len(self) == 0:
            return Polynomial(self.num_vars, self.ctype)  # return a copy, not a reference
        else:
            lt = self.leading_term(ordering)
            result = Polynomial(self.num_vars, self.ctype)
            result.coefficients[lt.monomial] = 1
            result._add_terms_unchecked(term/lt.coef for term in self if term is not lt)
            return result

    def _resolve_ordering(self, ordering=None):
        """If ordering is None and this is a univariate polynomial
        then return a DegreeOrdering instance. Otherwise, check that
        it is a valid monomial ordering for this polynomial and return
        it if so, or raise an exception if not."""
        if ordering is None:
            if self.num_vars == 1:
                return DegreeOrdering()
            else:
                raise OrderingError('you must provide a monomial ordering because this '+
                                    'polynomial is over more than one variable')
        else:
            if isinstance(ordering, collections.Callable):
                return ordering
            else:
                raise OrderingError('monomial orderings must be callable')

    def _pop_leading_term(self, ordering=None):
        return self._term_dict.pop(self.leading_term(ordering).monomial)

    def _assert_compatible(self, rhs):
        if rhs.num_vars != self.num_vars:
            raise VariableMismatchError('cannot add a term with %d variables '+
                                        'to a polynomial over %d variables' %
                                        (rhs.num_vars, self.num_vars))

    def _add_term(self, rhs):
        self._assert_compatible(rhs)
        self._add_term_unchecked(rhs.astype(self.ctype))

    def _add_term_unchecked(self, rhs):
        term = self._term_dict.get(rhs.monomial, None)
        if term is None:
            self._term_dict[rhs.monomial] = rhs  #.astype(self.ctype)
            term = rhs
        else:
            term.coef += rhs.coef
        if not term.coef:
            del self._term_dict[rhs.monomial]

    def _add_terms(self, terms):
        for term in terms:
            self._add_term(term)

    def _add_terms_unchecked(self, terms):
        for term in terms:
            self._add_term_unchecked(term)

    def _negate_terms(self):
        for term in self:
            term._negate()

    def _divide_terms_by(self, rhs):
        for term in self:
            term._divide_by(rhs)

    def __eq__(self, rhs):
        try:
            rhs = as_polynomial(rhs, self.num_vars)
            # dictionaries conveniently do an automatic deep comparison
            # including checking for missing elements
            return rhs._term_dict == self._term_dict
        except CoerceError:
            return NotImplemented

    def __ne__(self, rhs):
        return not (self == rhs)

    def __add__(self, rhs):
        try:
            rhs = as_polynomial(rhs, self.num_vars)
            self._assert_compatible(rhs)
            result = self.copy(result_type(self.ctype, rhs.ctype))
            result._add_terms_unchecked(rhs)
            return result
        except CoerceError:
            return NotImplemented

    def __sub__(self, rhs):
        try:
            rhs = as_polynomial(rhs, self.num_vars)
            self._assert_compatible(rhs)
            result = rhs.copy(result_type(self.ctype, rhs.ctype))
            result._negate_terms()
            result._add_terms_unchecked(self)
            return result
        except CoerceError:
            return NotImplemented

    def __mul__(self, rhs):
        try:
            rhs = as_polynomial(rhs, self.num_vars)
            self._assert_compatible(rhs)
            result = Polynomial(self.num_vars, result_type(self.ctype, rhs.ctype))
            for lterm, rterm in itertools.product(self, rhs):
                result._add_term_unchecked(lterm*rterm)
            return result
        except CoerceError:
            return NotImplemented

    def __pow__(self, rhs):
        if not isinstance(rhs, numbers.Integral) or rhs < 0:
            return NotImplemented
        elif rhs == 0:
            return Polynomial.constant(1, self.num_vars, self.ctype)
        else:
            result = Polynomial(self.num_vars, self.ctype)
            for terms in itertools.product(self, repeat=rhs):
                result._add_term_unchecked(product(terms))
            return result

    def __truediv__(self, rhs):
        """We only support division by a single terms. To perform polynomial
        division, use f%g to compute the remainder, f//g to compute
        the quotient, or divide_by() to compute both."""
        try:
            rhs = as_term(rhs, self.num_vars)
        except CoerceError:
            return NotImplemented
        result = self.copy(result_type(self.ctype, rhs.ctype))
        result._divide_terms_by(rhs)
        return result


    def __floordiv__(self, rhs):
        # TODO: avoid putting a default in here - an OrderedPolynomial class perhaps?
        try:
            rhs = as_polynomial(rhs, self.num_vars)
            quotient, remainder = self.divide_by(rhs, GrevlexOrdering())
            return quotient
        except CoerceError:
            return NotImplemented

    def __neg__(self):
        result = self.copy()
        result._negate_terms()
        return result

    def __mod__(self, rhs):
        # TODO: avoid putting a default in here - an OrderedPolynomial class perhaps?
        try:
            rhs = as_polynomial(rhs, self.num_vars)
            quotient,remainder = self.divide_by(rhs, GrevlexOrdering())
            return remainder
        except CoerceError:
            return NotImplemented

    def __rmul__(self, lhs):
        try:
            return as_polynomial(lhs, self.num_vars) * self
        except CoerceError:
            return NotImplemented

    def __radd__(self, lhs):
        try:
            return as_polynomial(lhs, self.num_vars) + self
        except CoerceError:
            return NotImplemented

    def __rsub__(self, lhs):
        try:
            return as_polynomial(lhs, self.num_vars) - self
        except CoerceError:
            return NotImplemented

    def __rmod__(self, lhs):
        try:
            return as_polynomial(lhs, self.num_vars) % self
        except CoerceError:
            return NotImplemented

    def __rfloordiv__(self, lhs):
        try:
            return as_polynomial(lhs, self.num_vars) // self
        except CoerceError:
            return NotImplemented

    def __call__(self, *x):
        """Return this polynomial evaluated at x, which should be an
        iterable of length num_vars."""
        assert len(x) == self.num_vars
        return sum(term(*x) for term in self)

    def __bool__(self):
        return len(self) > 0

    def __len__(self):
        """Return the number of terms in this polynomial."""
        return len(self._term_dict)

    def __iter__(self):
        """Return an iterator over the terms in this polynomial, in an
        arbitrary order. For predictable ordering, use
        polynomial.sorted_terms(...)."""
        return iter(self._term_dict.values())

    def __contains__(self, monomial):
        """Return true if this polynomial contains a non-zero term
        with the given monomial."""
        return monomial in self._term_dict

    def __delitem__(self, monomial):
        """Delete the term containing the given monomial from this polynomial."""
        del self._term_dict[monomial]

    def evaluate_partial(self, var, value):
        """Evaluate this polynomial given a variable index and a value
        for that variable.  The result of this operation is always a
        new polynomial in the same number of variables, although the
        evaluated variable will not appear in any term."""
        return Polynomial.create((term.evaluate_partial(var,value) for term in self),
                                 self.num_vars,
                                 self.ctype)

    def sign_at_infinity(self):
        """Compute the limiting value of this polynomial as x tends to
        infinity."""
        assert self.num_vars == 1
        if len(self) == 0:
            return 0
        else:
            return cmp(self.leading_term().coef, 0)

    def sign_at_minus_infinity(self):
        """Compute the limiting value of this polynomial as x tends to
        minus infinity."""
        assert self.num_vars == 1
        if len(self) == 0:
            return 0
        else:
            lt = self.leading_term()
            return cmp(lt.coef, 0) * (-1 if lt.monomial[0]%2 else 1)

    def as_term(self):
        """If this polynomial consists of just one term then return it, otherwise raise TypeError."""
        if len(self) != 1:
            raise TypeError("cannot convert a polynomial with %d terms to a single term" % len(self))
        return list(self._term_dict.values())[0]

    def as_monomial(self):
        """If this polynomial consists of just one term and that term has a coefficient of 1 then return its monomial,
        otherwise raise TypeError."""
        if len(self) != 1:
            raise TypeError("cannot convert a polynomial with %d terms to a single monomial" % len(self))
        term = list(self._term_dict.values())[0]
        if term.coef != 1:
            raise TypeError("cannot convert a term with coef %s to a monomial" % term.coef)
        return term.monomial

    def compile(self):
        """Return a python function that can be used to evaluate this
        polynomial quickly."""
        varnames = tuple('x'+str(i) for i in range(self.num_vars))
        expr = self.python_expression(varnames)
        return compilation.function_from_expression(expr, varnames)

    def python_expression(self, varnames=None):
        """Construct a representation of this polynomial as a python
        expression string."""
        if varnames is None:
            varnames = tuple('x'+str(i) for i in range(self.num_vars))
        if len(self) == 0:
            return '0'
        else:
            return ' + '.join(term.python_expression(varnames) for term in self)

    def format(self, ordering=GrevlexOrdering(), use_superscripts=True, compact=False):
        """Construct a string representation of this polynomial."""
        if len(self) == 0:
            return '0'
        else:
            parts = []
            plus = '+' if compact else ' + '
            minus = '-' if compact else ' - '
            for term in self.sorted_terms(ordering, reverse=True):
                if term.coef < 0:
                    if len(parts) == 0:
                        parts.append('-')
                    else:
                        parts.append(minus)
                    term = -term
                else:
                    if len(parts) != 0:
                        parts.append(plus)
                parts.append(term.format(use_superscripts))
            return ''.join(parts)

    def __str__(self):
        return self.format()

    def __repr__(self):
        return str(self)


#
# Utilities
#

def map_coefficients(f, polynomial):
    """Return a new polynomial formed by replacing each coefficient in
    the given polynomial with f(coefficient)."""
    result = Polynomial.create(polynomial.num_vars, polynomial.ctype)
    for term in polynomial:
        result[term.monomial] = f(term.coef)
    return result


def polynomial_vector(polynomials):
    fs = [ p.compile() for p in polynomials ]
    return lambda *x: np.array([ f(*x) for f in fs ])


def polynomial_gradient(polynomial):
    return polynomial_vector(polynomial.partial_derivative(i) for i in range(polynomial.num_vars))


def polynomial_jacobian(polynomials):
    gradients = [ polynomial_gradient(p) for p in polynomials ]
    return lambda *x: np.array([ gradient(*x) for gradient in gradients ])


#
# Operations for systems of equations
#

def remainder(f, H, ordering=None):
    """Compute the remainder of f on division by <H1,...,Hn> (the ideal generated by H)."""
    quotients = [ Polynomial(h.num_vars, h.ctype) for h in H ]
    remainder = f.copy()
    i = 0
    while i < len(H):
        if H[i].divides(remainder, ordering):
            old = remainder
            quotient, remainder = remainder.divide_by(H[i], ordering)
            quotients[i] += quotient
            i = 0
        else:
            i += 1
    return remainder


def matrix_form(fs, ordering=None):
    """Put the system of equations (f1=0,...,fn=0) into matrix form as
    C * X = 0, where C is a matrix of coefficients and X is a matrix
    of monomials."""
    monomials = list(set(term.monomial for f in fs for term in f))
    if isinstance(ordering, MonomialOrdering):
        monomials = sorted(monomials, key=lambda m: ComparableTerm(ordering, Term(1, m)))
    elif ordering is not None:
        assert all(isinstance(x, tuple) for x in ordering), 'ordering should be a list of tuples'
        monomials = ordering

    column_map = {monomial: index for index, monomial in enumerate(monomials)}
    x = [as_polynomial(monomial, fs[0].num_vars) for monomial in monomials]
    c = np.zeros((len(fs), len(monomials)))
    for row, f in enumerate(fs):
        for term in f:
            column = column_map.get(term.monomial, None)
            if column is not None:
                c[row, column] = term.coef

    return c, x


def quadratic_form(polynomial):
    """Construct a matrix A, a vector c, and a constant k such that
    p(x) = x'*A*x + c'*x + k"""
    assert polynomial.total_degree <= 2
    nv = polynomial.num_vars

    A = np.zeros((nv, nv))
    c = np.zeros(nv)
    k = polynomial.coefficients[(0,)*nv]

    for i in range(nv):
        xi = tuple(int(k==i) for k in range(nv))
        xixi = tuple(int(k==i)*2 for k in range(nv))
        c[i] = polynomial.coefficients[xi]
        A[i,i] = polynomial.coefficients[xixi]
        for j in range(i):
            xixj = tuple(int(k==i or k==j) for k in range(nv))
            A[i,j] = A[j,i] = polynomial.coefficients[xixj] * .5

    return A, c, k


#
# Operations for ideals
#

def ideal_intersection(*fs):
    return [f for F in fs for f in F]


def ideal_union(*fs):
    return [product(F) for F in itertools.product(*fs)]


def ideal_from_zero(zero, ctype=None):
    """Construct an ideal that vanishes at the given zero."""
    return [Polynomial.coordinate(i, len(zero), ctype) - zi for i, zi in enumerate(zero)]


def ideal_from_variety(zeros, ctype=None):
    """Construct an ideal from a finite variety."""
    return ideal_union(*(ideal_from_zero(zero, ctype) for zero in zeros))




#
# Grobner basis computations
#

def lcm(A, B):
    assert len(A) == len(B)
    return tuple(max(A[i],B[i]) for i in range(len(A)))


def s_poly(f, g, ordering):
    assert f.num_vars == g.num_vars
    assert f.ctype == g.ctype
    ltf = f.leading_term(ordering)
    ltg = g.leading_term(ordering)
    common = Polynomial.from_monomial(lcm(ltf.monomial, ltg.monomial), ctype=f.ctype)
    return (common/ltf) * f - (common/ltg) * g


def gbasis(F, ordering, limit=None):
    """Compute the Grobner basis for the ideal generated by F.
    If the limit parameter is given then an exception will be
    thrown if the size of the basis exceeds that number of equations."""

    # Check that none of the polynomials are zero
    if any(len(f) == 0 for f in F):
        raise Exception('cannot compute grobner basis of a system containing the zero polynomial')

    # Initialize the grobner basis to a copy of F
    G = [ f.copy() for f in F ]

    # Keep adding s-polynomials
    updated = True
    while updated:
        if limit is not None and len(G) > limit:
            raise GrobnerBasisTooLargeError('Grobner basis reached %d elements' % len(G))
        updated = False
        for gi, gj in itertools.combinations(G, 2):
            s = s_poly(gi, gj, ordering)
            r = remainder(s, G, ordering)
            if r != 0:
                G.append(r)
                updated = True
                break

    # Now we have a basis
    return G


def is_grobner_basis(G, ordering):
    for i, gi in enumerate(G):
        for j, gj in enumerate(G[:i]):
            lt_gi = gi.leading_term(ordering)
            tt_gi = gi.trailing_terms(ordering)
            lt_gj = gj.leading_term(ordering)
            tt_gj = gj.trailing_terms(ordering)
            lcm = Polynomial.from_monomial([max(a, b)
                                            for a, b in zip(lt_gi.monomial, lt_gj.monomial)])
            s = (tt_gi * lcm) // lt_gi - (tt_gj * lcm) // lt_gj
            ss = (gi * lcm) // lt_gi - (gj * lcm) // lt_gj
            assert s == ss
            if remainder(s, G, ordering) != 0:
                return False
    return True


#
# Parsing polynomials from strings
#

def extract_symbols(module):
    return {node.id for node in ast.walk(module) if isinstance(node, ast.Name)}


def parse(*exprs, **kwargs):
    # Get symbols
    symbols = set.union(*[extract_symbols(ast.parse(expr.strip())) for expr in exprs])

    # Check variable order
    variable_order = kwargs.get('variable_order', None)
    if variable_order is None:
        variable_order = sorted(symbols)
    else:
        assert symbols.issubset(variable_order), 'variable_order contained the wrong symbols'

    # Construct polynomials corresponding to each variable
    ctype = kwargs.get('ctype', None)
    variables = {var: Polynomial.coordinate(i, len(variable_order), ctype=ctype)
                 for i, var in enumerate(variable_order)}

    # Evaluate
    polynomials = tuple(eval(expr, variables) for expr in exprs)

    # Cast to singleton if necessary
    if len(exprs) == 1:
        return polynomials[0]
    else:
        return polynomials
