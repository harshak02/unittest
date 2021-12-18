import unittest

def add(num1,num2) :
    sum = num1+num2
    return sum

def sub(num1,num2) :
    subt = num1-num2
    return subt

def mul(num1,num2) :
    multi = num1*num2
    return multi

def div(num1,num2) :
    divi = num1/num2
    return divi

class test_class(unittest.TestCase) :
    def test_for_add (self) :
        self.assertEqual(100, add(75,25))
        
    def test_for_mul (self) :
        self.assertEqual(100, mul(25,4))
        
    def test_for_div (self) :
        self.assertEqual(5, div(20,4))

    def test_for_sub (self) :
        self.assertEqual(5, sub(20,15))
        

suite = unittest.TestLoader().loadTestsFromTestCase(test_class)

unittest.TextTestRunner(verbosity=4).run(suite)
        
    