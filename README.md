# sympy_extensions
Some extensions to the official [SymPy][sympy] 1.0 package

# WARNING
This is a [monkey patch][monkey-patching].
Please observe caution while on the monkey island.

# Contents

1. Function Expressions

   Some computations in SymPy are carried out immediately, e.g.,
   `lcm`, `gcd`, and `prime`.
   There is no chance for substitution and delayed computations.
   Suppose we need to calculate the L.C.M. (least common divisor) of x and y,
   but can only substitute their actual values at a later time,
   this is not achievable in the SymPy proper:

   ```python
   >>> lcm(x, y)
   x⋅y
   >>> lcm(x, y).subs({x:6, y:9})
   54
   >>> lcm(6, 9)
   18
   ```

   The function expressions of these computations
   are named `Lcm`, `Gcd`, and `Prime` respectively.
   They allow for delayed computation and substitution.
   They currently only support `subs` and `evalf` methods:

   ```python
   >>> from sympy_extensions import Lcm
   >>> Lcm(x, y)
   Lcm(y, x)
   >>> Lcm(x, y).subs({x:6, y:9})
   Lcm(6, 9)
   >>> Lcm(x, y).evalf(subs={x:6, y:9})
   18.0000000000000
   ```

[sympy]: https://github.com/sympy/sympy
[monkey-patching]: https://en.wikipedia.org/wiki/Monkey_patch
