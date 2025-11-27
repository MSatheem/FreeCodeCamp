import unittest

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(is_fizz_buzz([1, 2, "Fizz", 4]), True)
    def test2(self):
        self.assertEqual(is_fizz_buzz([1, 2, 3, 4]), False)
    def test3(self):
        self.assertEqual(is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", 7]), False)
    def test4(self):
        self.assertEqual(is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, "FizzBuzz"]), False)
    def test5(self):
        self.assertEqual(is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, "Fizz"]), False)
    def test6(self):
        self.assertEqual(is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, "Buzz"]), False)
    def test7(self):
        self.assertEqual(is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz", "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "FizzBuzz", 31, 32, "Fizz", 34, "Buzz", "Fizz", 37, 38, "Fizz", "Buzz", 41, "Fizz", 43, 44, "FizzBuzz", 46, 47, "Fizz", 49, "Buzz"]), True)

def is_fizz_buzz(sequence):
    for j in range(0, len(sequence)):
        i = j + 1;
        if i % 3 == 0 and i % 5 == 0 and sequence[j]!="FizzBuzz":
            return False
        elif i % 3 == 0 and i % 5 !=0 and sequence[j]!="Fizz":
            return False
        elif i % 5 == 0 and i % 3 !=0 and sequence[j]!="Buzz":
            return False    
        elif i % 3 != 0 and i % 5 !=0 and sequence[j] != i:
            return False
    return True

if __name__ == '__main__':
    unittest.main()

