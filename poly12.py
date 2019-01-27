#!/usr/bin/python

############################################
# module: poly12.py
# Krista Gurney
# A01671888
############################################

from prod import prod
from const import const
from pwr import pwr
from plus import plus
from var import var
from deriv import deriv
from tof import tof
from maker import make_prod, make_const, make_pwr, make_plus
import math

def find_poly_1_zeros(expr):
    constant = expr.get_elt2()
    value1 = const(constant.get_val() if constant.get_val() < 0 else constant.get_val() * (-1))
    value2 = expr.get_elt1().get_mult1()

    result = value1.get_val() / value2.get_val()
    return result

def find_poly_2_zeros(expr):

    a = expr.get_elt1().get_elt1().get_mult1().get_val()
    b = expr.get_elt1().get_elt2().get_mult1().get_val()
    c = expr.get_elt2().get_val()

    top1 = b*(-1)
    top2 = (b*b) -(4*a*c)
    root = math.sqrt(top2)

    topPos = top1 + root
    topNeg = top1 - root

    bottom = 2*a
    result1 = topPos / bottom
    result2 = topNeg / bottom

    return (result1, result2)

def test1():
    f1 = make_prod(make_const(3.0), make_pwr('x', 1.0))
    f2 = make_plus(f1, make_const(100.0))
    print(f2)
    print(find_poly_1_zeros(f2))

def test2():
    f0 = make_prod(make_const(0.5), make_pwr('x', 2.0))
    f1 = make_prod(make_const(6.0), make_pwr('x', 1.0))
    f2 = make_plus(f0, f1)
    poly = make_plus(f2, make_const(0.0))
    print(poly)
    zeros = find_poly_2_zeros(poly)
    print(zeros)
    # for c in zeros: print
    # c
    # pf = tof(poly)
    # for c in zeros: assert abs(pf(c.get_val()) - 0.0) <= 0.0001
    
if __name__ =='__main__':
    test2()
    




