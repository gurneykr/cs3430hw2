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
    ## your code here
    pass

def test1():
    f1 = make_prod(make_const(3.0), make_pwr('x', 1.0))
    f2 = make_plus(f1, make_const(100.0))
    print(f2)
    print(find_poly_1_zeros(f2))
    
if __name__ =='__main__':
    test1()
    




