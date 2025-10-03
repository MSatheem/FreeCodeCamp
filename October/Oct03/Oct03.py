import unittest

def check_strength(password):
    passwordScore = 0
    if(len(password) >=8):
        passwordScore += 1

    if(passwordScore ==1):
        return "Weak"

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(check_strength("123456"), "Weak")


if __name__ == "__main__":
    unittest.main()