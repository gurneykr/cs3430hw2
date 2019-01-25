#!/usr/bin/python

#########################################
# module: derivtest.py
#Krista Gurney
# A01671888
#########################################

from var import var
from const import const
from pwr import pwr
from prod import prod
from plus import plus
from poly12 import find_poly_1_zeros
from poly12 import find_poly_2_zeros
from tof import tof
from point2d import point2d
from deriv import deriv
from maker import make_const, make_prod, make_pwr, make_plus

def findDegree(expr):#return a 2 or 1 for its degree
    degreeExpr = make_const(1.0)
    try:
        if isinstance(expr, plus):
            if isinstance(expr.get_elt1(), plus):#2x^2 + x^1 +4
                if isinstance(expr.get_elt1().get_elt1(), prod):#3x^2
                    degreeExpr = expr.get_elt1().get_elt1().get_mult2().get_deg()
                elif isinstance(expr.get_elt1().get_elt1(), pwr):#x^2
                    degreeExpr = expr.get_elt1().get_elt1().get_deg()
                else:
                    raise Exception("Unexpected expression found in 1: ", type(expr.get_elt1().get_elt1()))
            elif isinstance(expr.get_elt1(), prod):#2x^1 + 3
                degreeExpr = expr.get_elt1().get_mult2().get_deg()
            else:
                raise Exception("Unexpected expression found in 2: ", type(expr.get_elt1()))
        else:
            raise Exception("Initial expression is not a plus: ", type(expr))
    except:
        print("error: ", type(expr) )

    degreeFn = tof(degreeExpr)
    degreeVal = degreeFn(0)
    return degreeVal

    #((((0.3333333333333333*(x^2.0))+(-2.0*(x^1.0)))+1.0)
    #(-2.0*(x^1.0)))+1.0)

    print("function: ", function)


def loc_xtrm_1st_drv_test(expr):
    derivativeExpr = deriv(expr)
    derivfun = tof(derivativeExpr)
    print("f(x)= ", derivativeExpr)

    degree = findDegree(derivativeExpr)

    if degree == 2:
        print("it's a second degree polynomial")
    else:
        print("it's a first degree polynomial")


def loc_xtrm_2nd_drv_test(expr):
    ## your code here
    pass

def test_03():
    f1 = make_prod(make_const(1.0/3.0), make_pwr('x', 3.0))
    f2 = make_prod(make_const(-2.0), make_pwr('x', 2.0))
    f3 = make_prod(make_const(3.0), make_pwr('x', 1.0))
    f4 = make_plus(f1, f2)
    f5 = make_plus(f4, f3)
    poly = make_plus(f5, make_const(1.0))
   # print('f(x) = ', poly)
    xtrma = loc_xtrm_1st_drv_test(poly)
    # for i, j in xtrma:
    #     print(i, str(j))

if __name__ == '__main__':
    test_03()