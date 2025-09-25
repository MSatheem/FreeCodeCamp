import unittest

def second_largest1(arr):
    #converting array to set to delete duplication
    myset = set(arr)
    #converting set to list
    sorted_list = list(myset)
    #sorting the list
    sorted_list.sort()
    #returning the second larggest element in the array
    if len(sorted_list) > 1:
        return sorted_list[-2] 
    else :
        return sorted_list[-1]

class TestFunction(unittest.TestCase):
    def test1(self):
        self.assertEqual(second_largest([1, 2, 3, 4]), 3)

    def test2(self):
        self.assertEqual(second_largest([20, 139, 94, 67, 31]), 94)

    def test3(self):
        self.assertEqual(second_largest([2, 3, 4, 6, 6]), 4)

    def test4(self):
        self.assertEqual(second_largest([10, -17, 55.5, 44, 91, 0]), 55.5)

    def test5(self):
        self.assertEqual(second_largest([1, 0, -1, 0, 1, 0, -1, 1, 0]), 0)

    def test6(self):
        self.assertEqual(second_largest([7,7,7]), 7)

    def test7(self):
        self.assertEqual(second_largest([1,2, 3,3,4]), 3)

if __name__ == '__main__':
    unittest.main()
