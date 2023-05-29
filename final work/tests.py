from calculate import calculate, load_params, convert_precision, PARAMS
import unittest

if __name__=="__main__":
    load_params()
    class TestCalculator(unittest.TestCase):
            def test_summ(self):
                self.assertEqual((calculate(*(3.2, 5.4, 1.0, 6), action="+", **PARAMS)), 15.6)

            def test_diff_pos(self):
                self.assertEqual((calculate(*(8, 2.3, 0, 4.55), action="-", **PARAMS)), 1.15)

            def test_diff_neg(self):
                self.assertEqual((calculate(*(2, 10.34), action="-", **PARAMS)), -8.34)

            def test_mult(self):
                self.assertEqual((calculate(*(3.2, 5.6, 1), action="*", **PARAMS)), 17.92)
            
            def test_power(self):
                self.assertEqual((calculate(*(5, 3), action="^", **PARAMS)), 125.0)

            def test_div(self):
                self.assertEqual((calculate(*(25, 5.0, 2.5), action="/", **PARAMS)), 2.0)

            def test_precision(self):
                self.assertEqual(convert_precision(0.0000001), 7)
                self.assertEqual(convert_precision(0.001), 3)

            def test_error(self):
                self.assertEqual(calculate(*(5, 0), action="/", **PARAMS),'Деление невозможно')

    unittest.main()