import unittest


def to_decimal(binary):
    decimalValue = 0
    count = 0
    for num in reversed(binary):
        decimalValue += int(num) * 2 ** count
        count +=1
    return decimalValue

class TestFunction(unittest.TestCase): 
    def test1(self):
        self.assertEqual(to_decimal("101"), 5)

    def test2(self):
        self.assertEqual(to_decimal("1010"), 10)

    def test3(self):
        self.assertEqual(to_decimal("10010"), 18)

    def test4(self):
        self.assertEqual(to_decimal("1010101"), 85)

if __name__ == '__main__':
    unittest.main()