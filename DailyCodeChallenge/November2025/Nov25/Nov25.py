import unittest

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(fizz_buzz(2),[1, 2])
    def test2(self):
        self.assertEqual(fizz_buzz(4), [1, 2, "Fizz", 4])
    def test3(self):
        self.assertEqual(fizz_buzz(8), [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8])
    def test4(self):
        self.assertEqual(fizz_buzz(20),[1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz"])
    def test5(self):
        self.assertEqual(fizz_buzz(50),[1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz", "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "FizzBuzz", 31, 32, "Fizz", 34, "Buzz", "Fizz", 37, 38, "Fizz", "Buzz", 41, "Fizz", 43, 44, "FizzBuzz", 46, 47, "Fizz", 49, "Buzz"])


def fizz_buzz(n):
    #empty array declaration
    arr = []

    #looping until n    
    for i in range(1, n+1):
        
        if(i%3==0 and i%5==0):
            arr.append("FizzBuzz")
        elif(i%3==0):
            arr.append("Fizz")
        elif(i%5==0):
            arr.append("Buzz")
        else:
            arr.append(i)
    return arr


if __name__ == '__main__':
    unittest.main()
