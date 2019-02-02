# #!/usr/bin/python
# # -*- coding: utf-8 -*-
#
# #############################################################
# # module: unit_tests.py
# # description: unit tests for CS 3430: S19: Assignment 01
# # bugs to vladimir kulyukin via canvas
# ##############################################################
#
# from __future__ import print_function
# import unittest
# from prod import prod
# from maker import make_const, make_pwr
# from plus import plus
# from tof import tof
# from deriv import deriv
#
# class Assign01UnitTests(unittest.TestCase):
#
#     def test_assgn_01_ut_01(self):
#         print('\n***** Assign 01: Unit Test 01 ************')
#         fex = prod(mult1=make_const(6.0),
#                    mult2=make_pwr('x', 3.0))
#         drv = deriv(fex)
#         assert not drv is None
#         drvf = tof(drv)
#         assert not drvf is None
#         gt = lambda x: 18*(x**2)
#         err = 0.00001
#         for i in range(1, 100):
#             assert abs(drvf(i) - gt(i)) <= err
#         print('Assign 01: Unit Test 01: pass')
#
#     def test_assgn_01_ut_02(self):
#         print('\n***** Assign 01: Unit Test 02 ************')
#         fex = prod(mult1=make_const(3.0),
#                    mult2=make_pwr('x', 1.0/3.0))
#         drv = deriv(fex)
#         assert not drv is None
#         drvf = tof(drv)
#         assert not drvf is None
#         gt = lambda x: (x**(-2.0/3.0))
#         err = 0.00001
#         for i in range(1, 100):
#             assert abs(drvf(i) - gt(i)) <= err
#         print('Assign 01: Unit Test 02: pass')
#
#     def test_assgn_01_ut_03(self):
#         print('\n***** Assign 01: Unit Test 03 ************')
#         prd = prod(mult1=make_const(2.0), mult2=make_pwr('x', 5.0))
#         drv = deriv(prd)
#         assert not drv is None
#         drvf = tof(drv)
#         assert not drvf is None
#         gt = lambda x: 10*x**4
#         err = 0.00001
#         for i in range(-100, 100):
#             assert abs(drvf(i) - gt(i)) <= err
#         print('Assign 01: Unit Test 03: pass')
#
#     def test_assgn_01_ut_04(self):
#         print('\n***** Assign 01: Unit Test 04 ************')
#         prd = prod(mult1=make_const(-3.0), mult2=make_pwr('x', -1.0))
#         drv = deriv(prd)
#         assert not drv is None
#         drvf = tof(drv)
#         assert not drvf is None
#         gt = lambda x: 3.0*(x**(-2))
#         err = 0.00001
#         for i in range(-100, 0):
#             assert abs(drvf(i) - gt(i)) <= err
#         for i in range(1, 100):
#             assert abs(drvf(i) - gt(i)) <= err
#         print('Assign 01: Unit Test 04: pass')
#
#     def test_assgn_01_ut_05(self):
#         print('\n***** Debug ************')
#         fex1 = make_pwr('x', 3.0)  # x^3 +5x
#         drv = deriv(fex1)
#         print(drv)
#         assert not drv is None
#         drvf = tof(drv)
#         assert not drvf is None
#         gt = lambda x: 3.0 * (x ** 2)
#         err = 0.00001
#         print('drvf(1): ',drvf(1))
#         print('gt(1):',gt(1))
#         for i in range(-100, 100):
#             assert abs(drvf(i) - gt(i)) <= err
#         print('Assign 01: Unit Test 05: pass')
#
#     def test_assgn_01_ut_05(self):
#         print('\n***** Assign 01: Unit Test 05 ************')
#         fex1 = make_pwr('x', 3.0)#x^3 +5x
#         fex2 = prod(mult1=make_const(5.0),
#                     mult2=make_pwr('x', 1.0))
#         p = plus(elt1=fex1, elt2=fex2)
#         drv = deriv(p)
#         print(drv)
#         assert not drv is None
#         drvf = tof(drv)
#         assert not drvf is None
#         gt = lambda x: 3.0*(x**2) + 5.0
#         err = 0.00001
#         print(drvf(1))
#         for i in range(-100, 100):
#             assert abs(drvf(i) - gt(i)) <= err
#         print('Assign 01: Unit Test 05: pass')
#
#     def test_assgn_01_ut_06(self):
#         print('\n***** Assign 01: Unit Test 06 ************')
#         fex1 = prod(mult1=make_const(2.0),
#                     mult2=make_pwr('x', 7.0))
#         fex2 = plus(elt1=prod(mult1=make_const(-1.0),
#                               mult2=make_pwr('x', 5.0)),
#                     elt2=make_const(8.0))
#         p = plus(elt1=fex1, elt2=fex2)
#         drv = deriv(p)
#         assert not drv is None
#         drvf = tof(drv)
#         assert not drvf is None
#         gt = lambda x: 14.0*(x**6) - 5.0*(x**4)
#         err = 0.00001
#         for i in range(-100, -1):
#             assert abs(drvf(i) - gt(i)) <= err
#         for i in range(1, 100):
#             assert abs(drvf(i) - gt(i)) <= err
#         print('Assign 01: Unit Test 06: pass')
#
#     def runTest(self):
#         pass
#
# if __name__ == '__main__':
#     unittest.main()
#!/usr/bin/python

#############################################################
# module: hw02_unit_tests.py
# description: unit tests for CS 3430: S19: Assignment 02
# bugs to vladimir kulyukin via canvas
##############################################################

#uncomment the next line if you use Py2
#from __future__ import print_function
import unittest
from prod import prod
from maker import make_const, make_pwr, make_const, make_plus
from maker import make_prod
from plus import plus
from tof import tof
from deriv import deriv
from poly12 import find_poly_1_zeros, find_poly_2_zeros
from derivtest import loc_xtrm_1st_drv_test
from derivtest import loc_xtrm_2nd_drv_test
from infl import find_infl_pnts

class Assign02UnitTests(unittest.TestCase):

    # def test_assgn_02_ut_01(self):
    #     print('\n***** Assign 02: Problem 01: Unit Test 01 *****')
    #     f1 = make_prod(make_const(2.0),
    #                    make_pwr('x', 1.0))
    #     f2 = make_plus(f1, make_const(5.0))
    #     print(f2)
    #     z = find_poly_1_zeros(f2)
    #     print(z)
    #     f2f = tof(f2)
    #     err = 0.0001
    #     assert abs(f2f(z.get_val()) - 0.0) <= err
    #     print('Assign 02: Problem 01: Unit Test 01: pass')

    # def test_assgn_02_ut_02(self):
    #     print('\n***** Assign 02: Unit Test 02 *****')
    #     f1 = make_prod(make_const(3.0),
    #                    make_pwr('x', 1.0))
    #     f2 = make_plus(f1, make_const(100.0))
    #     print(f2)
    #     z = find_poly_1_zeros(f2)
    #     print(z)
    #     f2f = tof(f2)
    #     err = 0.0001
    #     assert abs(f2f(z.get_val()) - 0.0) <= err
    #     print('Assign 02: Problem 01: Unit Test 02: pass')

    # def test_assgn_02_ut_03(self):
    #     print('\n***** Assign 02: Problem 01: Unit Test 03 *****')
    #     f1 = make_prod(make_const(25.0),
    #                    make_pwr('x', 1.0))
    #     f2 = make_plus(f1, make_const(-1027.0))
    #     print(f2)
    #     z = find_poly_1_zeros(f2)
    #     print(z)
    #     f2f = tof(f2)
    #     err = 0.0001
    #     assert abs(f2f(z.get_val()) - 0.0) <= err
    #     print('Assign 02: Problem 01: Unit Test 03: pass')
    #
    # def test_assgn_02_ut_04(self):
    #     print('\n***** Assign 02: Problem 01: Unit Test 04 *****')
    #     f0 = make_prod(make_const(0.5), make_pwr('x', 2.0))
    #     f1 = make_prod(make_const(6.0), make_pwr('x', 1.0))
    #     f2 = make_plus(f0, f1)
    #     poly = make_plus(f2, make_const(0.0))
    #     print(poly)
    #     zeros = find_poly_2_zeros(poly)
    #     for z in zeros:
    #         print(z)
    #     pf = tof(poly)
    #     err = 0.0001
    #     for z in zeros:
    #         assert abs(pf(z.get_val()) - 0.0) <= err
    #     print('Assign 02: Problem 01: Unit Test 04: pass')
    #
    # def test_assgn_02_ut_05(self):
    #     print('\n***** Assign 02: Problem 01: Unit Test 05 *****')
    #     f0 = make_pwr('x', 2.0)
    #     f1 = make_pwr('x', 1.0)
    #     f2 = make_plus(f0, f1)
    #     poly = make_plus(f2, make_const(-4.0))
    #     print(poly)
    #     zeros = find_poly_2_zeros(poly)
    #     for z in zeros:
    #         print(z)
    #     pf = tof(poly)
    #     err = 0.0001
    #     for z in zeros:
    #         assert abs(pf(z.get_val()) - 0.0) <= err
    #     print('Assign 02: Problem 01: Unit Test 05: pass')

    # def test_assgn_02_ut_06(self):
    #     print('\n***** Assign 02: Problem 01: Unit Test 06 *****')
    #     f0 = make_pwr('x', 2.0)
    #     f1 = make_prod(make_const(-3.0), make_pwr('x', 1.0))
    #     f2 = make_plus(f0, f1)
    #     poly = make_plus(f2, make_const(-4.0))
    #     print(poly)
    #     zeros = find_poly_2_zeros(poly)
    #     for z in zeros:
    #         print(z)
    #     pf = tof(poly)
    #     err = 0.0001
    #     for z in zeros:
    #         assert abs(pf(z.get_val()) - 0.0) <= err
    #     print('Assign 02: Problem 01: Unit Test 06: pass')
    #
    # def test_assgn_02_ut_07(self):
    #     print('\n***** Assign 02: Problem 01: Unit Test 07 *****')
    #     f0 = make_pwr('x', 2.0)
    #     f1 = make_prod(make_const(0.0), make_pwr('x', 1.0))
    #     f2 = make_plus(f0, f1)
    #     poly = make_plus(f2, make_const(-4.0))
    #     print(poly)
    #     zeros = find_poly_2_zeros(poly)
    #     for z in zeros:
    #         print(z)
    #     pf = tof(poly)
    #     err = 0.0001
    #     for z in zeros:
    #         assert abs(pf(z.get_val()) - 0.0) <= err
    #     print('Assign 02: Problem 01: Unit Test 07: pass')
    #
    # def test_assgn_02_ut_08(self):
    #     print('\n***** Assign 02: Problem 01: Unit Test 08 *****')
    #     f0 = make_prod(make_const(6.0), make_pwr('x', 2.0))
    #     f1 = make_prod(make_const(11.0), make_pwr('x', 1.0))
    #     f2 = make_plus(f0, f1)
    #     poly = make_plus(f2, make_const(-35.0))
    #     print(poly)
    #     zeros = find_poly_2_zeros(poly)
    #     for z in zeros:
    #         print(z)
    #     pf = tof(poly)
    #     err = 0.0001
    #     for z in zeros:
    #         assert abs(pf(z.get_val()) - 0.0) <= err
    #     print('Assign 02: Problem 01: Unit Test 08: pass')
    #
    # def test_assgn_02_ut_09(self):
    #     print('\n***** Assign 02: Problem 01: Unit Test 09 ************')
    #     f0 = make_pwr('x', 2.0)
    #     f1 = make_prod(make_const(0.0), make_pwr('x', 1.0))
    #     f2 = make_plus(f0, f1)
    #     poly = make_plus(f2, make_const(-48.0))
    #     print(poly)
    #     zeros = find_poly_2_zeros(poly)
    #     for z in zeros:
    #         print(z)
    #     pf = tof(poly)
    #     err = 0.0001
    #     for z in zeros:
    #         assert abs(pf(z.get_val()) - 0.0) <= err
    #     print('Assign 02: Problem 01: Unit Test 09: pass')

    def test_assgn_02_ut_11(self):
        print('\n***** Assign 02: Problem 02: Unit Test 011 *****')
        f1 = make_prod(make_const(1.0/3.0), make_pwr('x', 3.0))
        f2 = make_prod(make_const(-2.0), make_pwr('x', 2.0))
        f3 = make_prod(make_const(3.0), make_pwr('x', 1.0))
        f4 = make_plus(f1, f2)
        f5 = make_plus(f4, f3)
        poly = make_plus(f5, make_const(1.0))
        print(poly)
        xtrma = loc_xtrm_1st_drv_test(poly)
        assert len(xtrma) == 2
        err = 0.0001
        for i, j in xtrma:
            print(i, str(j))
            if i == 'max':
                assert abs(j.get_x().get_val() - 1.0) <= err
                assert abs(j.get_y().get_val() - 2.33333333333) <= err
            if i == 'min':
                assert abs(j.get_x().get_val() - 3.0) <= err
                assert abs(j.get_y().get_val() - 1.0) <= err
        print('Assign 02: Problem 02: Unit Test 01: pass')

    # def test_assgn_02_ut_12(self):
    #     print('\n***** Assign 02: Problem 02: Unit Test 02 *****')
    #     f1 = make_prod(make_const(27.0), make_pwr('x', 3.0))
    #     f2 = make_prod(make_const(-27.0), make_pwr('x', 2.0))
    #     f3 = make_prod(make_const(9.0), make_pwr('x', 1.0))
    #     f4 = make_plus(f1, f2)
    #     f5 = make_plus(f4, f3)
    #     f6 = make_plus(f5, make_const(-1.0))
    #     print(f6)
    #     xtrma = loc_xtrm_1st_drv_test(f6)
    #     assert xtrma is None
    #     print('Assign 02: Problem 02: Unit Test 02: pass')
    #
    # def test_assgn_02_ut_13(self):
    #     print('\n***** Assign 02: Problem 02: Unit Test 03 *****')
    #     f1 = make_prod(make_const(1.0/4.0), make_pwr('x', 2.0))
    #     f2 = make_prod(make_const(-1.0), make_pwr('x', 1.0))
    #     f3 = make_plus(f1, f2)
    #     f4 = make_plus(f3, make_const(2.0))
    #     print(f4)
    #     xtrma = loc_xtrm_2nd_drv_test(f4)
    #     assert len(xtrma) == 1
    #     err = 0.0001
    #     for i, j in xtrma:
    #         print(i, str(j))
    #         if i == 'min':
    #             assert abs(j.get_x().get_val() - 2.0) <= err
    #             assert abs(j.get_y().get_val() - 1.0) <= err
    #     print('Assign 02: Problem 02: Unit Test 03: pass')
    #
    # def test_assgn_02_ut_14(self):
    #     print('\n***** Assign 02: Problem 02: Unit Test 04 *****')
    #     f1 = make_pwr('x', 3.0)
    #     f2 = make_prod(make_const(-3.0), make_pwr('x', 2.0))
    #     f3 = make_plus(f1, f2)
    #     f4 = make_plus(f3, make_const(5.0))
    #     print(f4)
    #     xtrma = loc_xtrm_2nd_drv_test(f4)
    #     assert len(xtrma) == 2
    #     err = 0.0001
    #     for i, j in xtrma:
    #         print(i, str(j))
    #         if i == 'max':
    #             assert abs(j.get_x().get_val() - 0.0) <= err
    #             assert abs(j.get_y().get_val() - 5.0) <= err
    #         if i == 'min':
    #             assert abs(j.get_x().get_val() - 2.0) <= err
    #             assert abs(j.get_y().get_val() - 1.0) <= err
    #     print('Assign 02: Problem 02: Unit Test 04: pass')
    #
    # def test_assgn_02_ut_15(self):
    #     print('\n***** Assign 02: Problem 02: Unit Test 05 *****')
    #     f1 = make_pwr('x', 3.0)
    #     f2 = make_prod(make_const(-27.0), make_pwr('x', 1.0))
    #     f3 = make_plus(f1, f2)
    #     f4 = make_plus(f3, make_const(0.0))
    #     print(f4)
    #     xtrma = loc_xtrm_2nd_drv_test(f4)
    #     assert len(xtrma) == 2
    #     err = 0.0001
    #     for i, j in xtrma:
    #         print(i, str(j))
    #         if i == 'max':
    #             assert abs(j.get_x().get_val() + 3.0) <= err
    #             assert abs(j.get_y().get_val() - 54.0) <= err
    #         if i == 'min':
    #             assert abs(j.get_x().get_val() - 3.0) <= err
    #             assert abs(j.get_y().get_val() + 54.0) <= err
    #     print('Assign 02: Problem 02: Unit Test 04: pass')
    #
    # def test_assgn_02_ut_16(self):
    #     print('\n***** Assign 02: Problem 03: Unit Test 01 *****')
    #     f1 = make_pwr('x', 3.0)
    #     f2 = make_prod(make_const(-3.0), make_pwr('x', 2.0))
    #     f3 = make_prod(make_const(0.0), make_pwr('x', 0.0))
    #     f4 = make_plus(f1, f2)
    #     f5 = make_plus(f4, f3)
    #     f6 = make_plus(f5, make_const(5.0))
    #     print(f6)
    #     ips = find_infl_pnts(f6)
    #     err = 0.0001
    #     assert len(ips) == 1
    #     ip = ips[0]
    #     assert abs(ip.get_x().get_val() - 1.0) <= err
    #     assert abs(ip.get_y().get_val() - 3.0) <= err
    #     print('Assign 02: Problem 03: Unit Test 01: pass')
    #
    # def test_assgn_02_ut_16(self):
    #     print('\n***** Assign 02: Problem 03: Unit Test 02 *****')
    #     f1 = make_pwr('x', 3.0)
    #     f2 = make_prod(make_const(-3.0),
    #                    make_pwr('x', 1.0))
    #     f3 = make_plus(f1, f2)
    #     f4 = make_plus(f3, make_const(2.0))
    #     inflps = find_infl_pnts(f4)
    #     assert len(inflps) == 1
    #     ip = inflps[0]
    #     assert ip.get_x().get_val() == 0.0
    #     assert ip.get_y().get_val() == 2.0
    #     for ip in inflps:
    #         print(str(ip))
    #     print('Assign 02: Problem 03: Unit Test 02: pass')
    #
    # def test_assgn_02_ut_17(self):
    #     print('\n***** Assign 02: Problem 03: Unit Test 03 *****')
    #     f1 = make_prod(make_const(-1.0),
    #                    make_pwr('x', 3.0))
    #     f2 = make_prod(make_const(3.0),
    #                    make_pwr('x', 2.0))
    #     f3 = make_plus(f1, f2)
    #     f4 = make_plus(f3, make_const(1.0))
    #     inflps = find_infl_pnts(f4)
    #     assert len(inflps) == 1
    #     ip = inflps[0]
    #     assert ip.get_x().get_val() == 1.0
    #     assert ip.get_y().get_val() == 3.0
    #     for ip in inflps:
    #         print(str(ip))
    #     print('Assign 02: Problem 03: Unit Test 03: pass')

    def runTest(self):
        pass

if __name__ == '__main__':
    unittest.main()
