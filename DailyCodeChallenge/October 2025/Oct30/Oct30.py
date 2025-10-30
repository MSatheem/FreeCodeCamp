import unittest;

def nth_prime(n):
    nth_prime_num = 2
    if n==1 :
        return nth_prime_num
    else:
        count = 1
        while(count!=n):
            nth_prime_num += 1
            if(isPrime(nth_prime_num)):
                count += 1
    return nth_prime_num

def isPrime(num):
    for i in range(2, num):
        if(num % i == 0) :
            return False
    return True

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual( nth_prime(5), 11);
    def test2(self):
        self.assertEqual( nth_prime(10), 29);
    def test3(self):
        self.assertEqual( nth_prime(16), 53);
    def test4(self):
            self.assertEqual( nth_prime(99), 523);
    def test5(self):
            self.assertEqual( nth_prime(1000), 7919);


if __name__ == '__main__':
    unittest.main()