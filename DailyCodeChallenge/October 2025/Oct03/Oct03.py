import unittest

def check_strength(password):
    if password == None:
        return "weak"

    password_score = 0
    
    has_upper =False
    has_lower = False
    has_digit = False
    has_special = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():
            has_special = True
        if has_upper and has_lower and has_digit and has_special:
            break
        
    if len(password) >=8:
        password_score += 1
    if has_upper and has_lower:
        password_score += 1
    if has_digit:
        password_score += 1
    if has_special:
        password_score += 1

    if password_score < 2:
        return "weak"
    elif password_score < 4:
        return "medium"
    else:
        return "strong"

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(check_strength("123456"), "weak")

    def test2(self):
        self.assertEqual(check_strength("pass!!!"), "weak")
        
    def test3(self):
        self.assertEqual(check_strength("Qwerty"), "weak")

    def test4(self):
        self.assertEqual(check_strength("PASSWORD"), "weak")

    def test5(self):
        self.assertEqual(check_strength("PASSWORD!"), "medium")

    def test6(self):
        self.assertEqual(check_strength("PassWord%^!"), "medium")

    def test7(self):
        self.assertEqual(check_strength("qwerty12345"), "medium")

    def test8(self):
        self.assertEqual(check_strength("PASSWORD!"), "medium")

    def test9(self):
        self.assertEqual(check_strength("PASSWORD!"), "medium")
    
    def test10(self):
        self.assertEqual(check_strength("S3cur3P@ssw0rd"), "strong")
    
    def test11(self):
        self.assertEqual(check_strength("C0d3&Fun!"), "strong")

    def test12(self):
        self.assertEqual(check_strength(""), "weak")
    
    def test13(self):
        self.assertEqual(check_strength(None), "weak")

if __name__ == "__main__":
    unittest.main()