import unittest
import math

def infected(days):
    if days<1:
        return 0
    else:
        number_of_computers = 1
        for i in range(days):
            #number of computer infected double per day
            number_of_computers *= 2
            #every third day patched 20% computers
            if (i+1) % 3 == 0:
                #rounding the infected computers to the next whole number 
                number_of_computers = number_of_computers - math.ceil(number_of_computers * 0.2)

        return number_of_computers            

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(infected(1),2)
    def test2(self):
        self.assertEqual(infected(2),4)
    def test3(self):
        self.assertEqual(infected(3),6)
    def test4(self):
        self.assertEqual(infected(8),152)
    def test5(self):
        self.assertEqual(infected(17),39808)
    def test6(self):
        self.assertEqual(infected(24),2608819)
    def test7(self):
        self.assertEqual(infected(25),5217638)

if __name__ == '__main__':
    unittest.main()
