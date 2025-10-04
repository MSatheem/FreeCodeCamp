import unittest

def classification(temp):
    if temp >= 0 and temp <=3699:
        return "M"
    elif temp >= 3700 and temp <=5199:
        return "K"
    elif temp >= 5200 and temp <=5999:
        return "G"
    elif temp >= 6000 and temp <=7499:
        return "F"
    elif temp >= 7500 and temp <=9999:
        return "A"
    elif temp >= 10000 and temp <= 29999:
        return "B"
    elif temp >= 30000:
        return "O"

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(classification(5778), "G")
    def test2(self):
        self.assertEqual(classification(2400), "M")
    def test3(self):
        self.assertEqual(classification(9999), "A")
    def test4(self):
        self.assertEqual(classification(3700), "K")
    def test5(self):
        self.assertEqual(classification(3699), "M")
    def test6(self):
        self.assertEqual(classification(210000), "O")
    def test7(self):
        self.assertEqual(classification(6000), "F")
    def test8(self):
        self.assertEqual(classification(11432), "B")
                         

if __name__ == "__main__":
    unittest.main()