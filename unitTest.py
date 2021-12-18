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
        list1 = [1,2,3,4]
        list2 = [4,3,2,1]
        for i in range(0,len(list1)) :    
            self.assertEqual(5, add(list1[i],list2[i]))
        
    def test_for_mul (self) :
        list3 = [2,4,8]
        list4 = [16,8,4]
        for i in range (0,len(list3)) :
            self.assertEqual(32, mul(list3[i],list4[i]))
        
    def test_for_div (self) :
        list5 = [16,32,64]
        list6 = [8,16,32]
        for i in range(0,len(list5)) :
            self.assertEqual(2, div(list5[i],list6[i]))

    def test_for_sub (self) :
        list1 = [5,3,2,1]
        list2 = [4,2,1,0]
        for i in range(0,len(list1)) :    
            self.assertEqual(1, sub(list1[i],list2[i]))
        

suite = unittest.TestLoader().loadTestsFromTestCase(test_class)

unittest.TextTestRunner(verbosity=4).run(suite)
        