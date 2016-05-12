#!/usr/bin/env python

from __future__ import print_function

if __name__ == '__main__':

    import sys, os
    p = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, p)

    from sympy import lcm_list, gcd_list, prime, Number
    from sympy.abc import x, y, z
    from sympy_extensions import *

    test_values = {
            x: 6,
            y: 10,
            z: 14,
    }

    # test Lcm
    lhs = Lcm(x, y, z).subs(test_values)
    rhs = Lcm(*(v for k,v in test_values.items()))
    largs = list(lhs.args).sort()
    rargs = list(rhs.args).sort()
    assert largs == rargs
    assert \
            Lcm(x, y, z).subs(test_values).evalf() == \
            lcm_list(tuple(v for k,v in test_values.items())).evalf()
    assert \
            Lcm(x, y, z).evalf(subs=test_values) == \
            lcm_list(tuple(v for k,v in test_values.items())).evalf()

    # test Gcd
    lhs = Gcd(x, y, z).subs(test_values)
    rhs = Gcd(*(v for k,v in test_values.items()))
    largs = list(lhs.args).sort()
    rargs = list(rhs.args).sort()
    assert largs == rargs
    assert \
            Gcd(x, y, z).subs(test_values).evalf() == \
            gcd_list(tuple(v for k,v in test_values.items())).evalf()
    assert \
            Gcd(x, y, z).evalf(subs=test_values) == \
            gcd_list(tuple(v for k,v in test_values.items())).evalf()

    # test Prime
    assert \
            Prime(x).subs({x:4}) == \
            Prime(4)
    assert \
            Prime(x).subs({x:5}).evalf() == \
            Number(prime(5)).evalf()
    assert \
            Prime(x).evalf(subs={x:6}) == \
            Number(prime(6)).evalf()

    print("All tests successfully passed")

else:

    print(
            "The test script must be run from an interpreter, "
            "instead of imported as a module."
    )
