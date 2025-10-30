import unittest

def to_binary(decimal):
    
    if(decimal == 0):
        return "0"
    
    else : 
        binaryList = ""
        while decimal > 0 :
            binaryList += str(decimal%2)
            decimal //= 2
        return (binaryList[::-1])

# def to_binary(decimal):
#     if decimal == 0:
#         return "0"
#     binary_str = ""
#     while decimal > 0:
#         binary_str = str(decimal % 2) + binary_str
#         decimal //= 2  # Use integer division for clarity
#     return binary_str

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(to_binary(5), "101")

    def test2(self):
        self.assertEqual(to_binary(12), "1100")

    def test3(self):
        self.assertEqual(to_binary(50), "110010")

    def test4(self):
        self.assertEqual(to_binary(99), "1100011")

    def test5(self):
        self.assertEqual(to_binary(0), "0")

  
if __name__ == "__main__":
    unittest.main()       