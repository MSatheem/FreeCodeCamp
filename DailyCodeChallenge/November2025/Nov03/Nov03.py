import unittest

def count_words(sentence):
    stringSplit = sentence.split(' ')
    count = 0
    for i in stringSplit:
        count += 1
    return count

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(count_words("Hello world"),2)
    def test2(self):
        self.assertEqual(count_words("The quick brown fox jumps over the lazy dog."), 9)
    def test3(self):
        self.assertEqual(count_words("I like coding challenges!"),4)
    def test4(self):
        self.assertEqual(count_words("Complete the challenge in JavaScript and Python."),7)
    def test5(self):
        self.assertEqual(count_words("The missing semi-colon crashed the entire internet."),7)

if __name__ == '__main__':
    unittest.main()
