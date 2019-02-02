#!/usr/bin/python


###########################################
# module: tof.py
# Your Name
# Your A#
###########################################

from var import var
from const import const
from pwr import pwr
from prod import prod
from plus import plus
import math

def tof(expr):
    if isinstance(expr, const):
        return const_tof(expr)
    elif isinstance(expr, pwr):
        return pwr_tof(expr)
    elif isinstance(expr, prod):
        return prod_tof(expr)
    elif isinstance(expr, plus):
        return plus_tof(expr)
    else:
        raise Exception('tof: ' + str(expr))

## here is how you can implement converting
## a constant to a function.
def const_tof(c):
    assert isinstance(c, const)
    def f(x):
        return c.get_val()
    return f

def pwr_tof(expr):
    assert isinstance(expr, pwr)
    expb = expr.get_base()
    d = expr.get_deg()
    if isinstance(expb, const):
        # your code here
        pass
    elif isinstance(expb, var):
        if isinstance(d, const):
            # your code here
            pass
        else:
            raise Exception('pw_tof: case 1:' + str(expr))
    elif isinstance(expb, plus):
        if isinstance(d, const):
            # your code here
            pass
        else:
            raise Exception('pw_tof: case 2:' + str(expr))
    elif isinstance(expb, pwr):
        if isinstance(d, const):
            # your code here
            pass
        else:
            raise Exception('pw_tof: case 3:' + str(expr))
    elif isinstance(expb, prod):
        if isinstance(d, const):
            # your code here
            pass
        else:
            raise Exception('pw_tof: case 4:' + str(expr))
    else:
        raise Exception('pw_tof: case 5:' + str(expr))

def prod_tof(expr):
    # your code here
    pass

def plus_tof(expr):
    # your code here
    pass


    
