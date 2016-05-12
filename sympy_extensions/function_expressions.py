"""
SymPy extensions - function expressions:

This extension module implements SymPy computation functions as expressions,
to support delayed computation and substitution.

Currently implemented function expressions include:

    - ``Lcm``, and ``Gcd``, as associative operations and expressions.
    - ``Prime``, which allows only one args.
"""
__all__ = ['Lcm', 'Gcd', 'Prime']

import sympy


class Lcm(sympy.Expr, sympy.operations.AssocOp):

    identity = 1

    def subs(self, *args, **kwargs):
        return Lcm(*(x.subs(*args, **kwargs) for x in self.args))

    def _eval_evalf(self, *args, **kwargs):
        return sympy.Number(sympy.lcm_list(self.args)).evalf(*args, **kwargs)


class Gcd(sympy.Expr, sympy.operations.AssocOp):

    identity = 0

    def subs(self, *args, **kwargs):
        return Gcd(*(x.subs(*args, **kwargs) for x in self.args))

    def _eval_evalf(self, *args, **kwargs):
        return sympy.Number(sympy.gcd_list(self.args)).evalf(*args, **kwargs)


class Prime(sympy.Expr):

    # only allowing one argument
    def __init__(self, n):
        sympy.Expr(self, n)

    def subs(self, *args, **kwargs):
        return Prime(self.args[0].subs(*args, **kwargs))

    def _eval_evalf(self, *args, **kwargs):
        return sympy.Number(sympy.prime(self.args[0])).evalf(*args, **kwargs)
