import unittest

def get_longest_word(sentence):
    list = sentence.strip().replace('.','').split(" ")
    longestword = list[0]
    for i in list:
        if(len(i) > len(longestword)):
            longestword = i
    return longestword


class TestFunction(unittest.TestCase):
    def test1(self):
        self.assertEqual(get_longest_word("coding is fun"), "coding")

    def test2(self):
        self.assertEqual(get_longest_word("Coding challenges are fun and educational."), "educational")

    def test3(self):
        self.assertEqual(get_longest_word("This sentence has multiple long words."), "sentence")
    
    def test4(self):
        self.assertEqual(get_longest_word("Longestishere This sentence has multiple long words."), "Longestishere")

if __name__ == '__main__':
    unittest.main()

print(get_longest_word("Coding challenges are fun and educational."))