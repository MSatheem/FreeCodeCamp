import unittest

def format_number(number):
    numberFormat = f"+{number[0]} ({number[1:4]}) {number[4:7]}-{number[7:]}"
    return numberFormat


class TestFunctin(unittest.TestCase):
    def test1(self):
        self.assertEqual(format_number("05552340182"), "+0 (555) 234-0182")

    def test2(self):
        self.assertEqual(format_number("15554354792"), "+1 (555) 435-4792")

if __name__ == '__main__':
    unittest.main()