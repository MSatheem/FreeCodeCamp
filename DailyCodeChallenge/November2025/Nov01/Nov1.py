import unittest

def verify(message, key, signature):
    message_key = decode(message) + decode(key)
    if message_key == signature:
        return True
    else:
        return False

def decode(encoded):
    total = 0
    for i in encoded:
        unicode_num = ord(i)
        if (unicode_num >=97 and unicode_num <= 122) or (unicode_num >=65 and unicode_num <= 90):
            if unicode_num >=97:
                total += (unicode_num - 96)
            else :
                total += (unicode_num - 38)
    return total

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(verify("foo", "bar", 57), True)
    def test2(self):
        self.assertEqual(verify("foo", "bar", 54), False)
    def test3(self):
        self.assertEqual(verify("freeCodeCamp", "Rocks", 238), True)
    def test4(self):
        self.assertEqual(verify("Is this valid?", "No", 210), False)
    def test5(self):
        self.assertEqual(verify("Is this valid?", "Yes", 233), True)
    def test6(self):
        self.assertEqual(verify("Check out the freeCodeCamp podcast,", "in the mobile app", 514), True)


if __name__ == '__main__':
    unittest.main()
