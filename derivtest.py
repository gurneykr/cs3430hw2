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
from tof import tof
from deriv import deriv
from maker import make_const, make_prod, make_pwr, make_plus

def findDegree(expr):
    return evalExpr(expr)

def evalExpr(expr):
    if isinstance(expr, plus):
        results = evalExpr(expr.get_elt1())
        if results > -1:
            return results

        results = evalExpr(expr.get_elt2())
        if results >= 0:
            return results
    elif isinstance(expr, pwr):
        theFn = tof(expr.get_deg())
        return theFn(0)
    elif isinstance(expr, prod):
        results = evalExpr(expr.get_mult1())
        if results > -1:
            return results
        results = evalExpr(expr.get_mult2())
        if results > -1:
            return results
    elif isinstance(expr, const) or isinstance(expr, var):
        return -1
    else:
        raise Exception('Exception Found: ', type(expr))

    return -2

def loc_xtrm_1st_drv_test(expr):
    derivativeExpr = deriv(expr)
    derivfun = tof(derivativeExpr)

    degree = findDegree(derivativeExpr)

    if degree == 2:
        print("it's a second degree polynomial")
    else:
        print("it's a first degree polynomial")


def loc_xtrm_2nd_drv_test(expr):
    ## your code here
    pass

def test_03():
    # 1/3x^3 - 2x^2 + 3x + 1
    # x^2 - 4x + 3     (((((0.3333333333333333*3.0)*(x^(3.0+-1)))+((-2.0*2.0)*(x^(2.0+-1))))+((3.0*1.0)*(x^(1.0+-1))))+0.0)
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


def test_01():
    # 2x^2 + 3x + 1
    f2 = make_prod(make_const(-2.0), make_pwr('x', 2.0))
    f3 = make_prod(make_const(3.0), make_pwr('x', 1.0))
    f4 = make_plus(f2, f3)
    poly = make_plus(f4, make_const(1.0))
    loc_xtrm_1st_drv_test(poly)

if __name__ == '__main__':
    test_03()
