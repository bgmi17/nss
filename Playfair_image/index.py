"""
BINARY POLYNOMIAL ARITHMETIC

These functions operate on binary polynomials (Z/2Z[x]), expressed as coefficient bitmasks, etc:
  0b100111 -> x^5 + x^2 + x + 1
As an implied precondition, parameters are assumed to be *nonnegative* integers unless otherwise noted.
This code is time-sensitive and thus NOT safe to use for online cryptography.
"""

from typing import Tuple

# descriptive aliases (assumed not to be negative)
Natural = int
BPolynomial = int


def p_mul(a: BPolynomial, b: BPolynomial) -> BPolynomial:
    """ Binary polynomial multiplication (peasant). """
    result = 0
    while a and b:
        if a & 1:
            result ^= b
        a >>= 1
        b <<= 1
    return result


def p_mod(a: BPolynomial, b: BPolynomial) -> BPolynomial:
    """ Binary polynomial remainder / modulus.
        Divides a by b and returns resulting remainder polynomial.
        Precondition: b != 0 """
    bl = b.bit_length()
    while True:
        shift = a.bit_length() - bl
        if shift < 0:
            return a
        a ^= b << shift


def p_divmod(a: BPolynomial, b: BPolynomial) -> Tuple[BPolynomial, BPolynomial]:
    """ Binary polynomial division.
        Divides a by b and returns resulting (quotient, remainder) polynomials.
        Precondition: b != 0 """
    q = 0
    bl = b.bit_length()
    while True:
        shift = a.bit_length() - bl
        if shift < 0:
            return (q, a)
        q ^= 1 << shift
        a ^= b << shift


def p_mod_mul(a: BPolynomial, b: BPolynomial, modulus: BPolynomial) -> BPolynomial:
    """ Binary polynomial modular multiplication (peasant).
        Returns p_mod(p_mul(a, b), modulus)
        Precondition: modulus != 0 and b < modulus """
    result = 0
    deg = p_degree(modulus)
    assert p_degree(b) < deg
    while a and b:
        if a & 1:
            result ^= b
        a >>= 1
        b <<= 1
        if (b >> deg) & 1:
            b ^= modulus
    return result


def p_exp(a: BPolynomial, exponent: Natural) -> BPolynomial:
    """ Binary polynomial exponentiation by squaring (iterative).
        Returns polynomial `a` multiplied by itself `exponent` times.
        Precondition: not (x == 0 and exponent == 0) """
    factor = a
    result = 1
    while exponent:
        if exponent & 1:
            result = p_mul(result, factor)
        factor = p_mul(factor, factor)
        exponent >>= 1
    return result


def p_gcd(a: BPolynomial, b: BPolynomial) -> BPolynomial:
    """ Binary polynomial euclidean algorithm (iterative).
        Returns the Greatest Common Divisor of polynomials a and b. """
    while b:
        a, b = b, p_mod(a, b)
    return a


def p_egcd(a: BPolynomial, b: BPolynomial) -> tuple[BPolynomial, BPolynomial, BPolynomial]:
    """ Binary polynomial Extended Euclidean algorithm (iterative).
        Returns (d, x, y) where d is the Greatest Common Divisor of polynomials a and b.
        x, y are polynomials that satisfy: p_mul(a,x) ^ p_mul(b,y) = d
        Precondition: b != 0
        Postcondition: x <= p_div(b,d) and y <= p_div(a,d) """
    a = (a, 1, 0)
    b = (b, 0, 1)
    while True:
        q, r = p_divmod(a[0], b[0])
        if not r:
            return b
        a, b = b, (r, a[1] ^ p_mul(q, b[1]), a[2] ^ p_mul(q, b[2]))


def p_mod_inv(a: BPolynomial, modulus: BPolynomial) -> BPolynomial:
    """ Binary polynomial modular multiplicative inverse.
        Returns b so that: p_mod(p_mul(a, b), modulus) == 1
        Precondition: modulus != 0 and p_coprime(a, modulus)
        Postcondition: b < modulus """
    d, x, y = p_egcd(a, modulus)
    assert d == 1  # inverse exists
    return x


def p_mod_pow(x: BPolynomial, exponent: Natural, modulus: BPolynomial) -> BPolynomial:
    """ Binary polynomial modular exponentiation by squaring (iterative).
        Returns: p_mod(p_exp(x, exponent), modulus)
        Precondition: modulus > 0
        Precondition: not (x == 0 and exponent == 0) """
    factor = x = p_mod(x, modulus)
    result = 1
    while exponent:
        if exponent & 1:
            result = p_mod_mul(result, factor, modulus)
        factor = p_mod_mul(factor, factor, modulus)
        exponent >>= 1
    return result


def p_degree(a: BPolynomial) -> int:
    """ Returns degree of a. """
    return a.bit_length() - 1


def p_congruent(a: BPolynomial, b: BPolynomial, modulus: BPolynomial) -> bool:
    """ Checks if a is congruent with b under modulus.
        Precondition: modulus > 0 """
    return p_mod(a ^ b, modulus) == 0


def p_coprime(a: BPolynomial, b: BPolynomial) -> bool:
    """ Checks if a and b are coprime. """
    return p_gcd(a, b) == 1
