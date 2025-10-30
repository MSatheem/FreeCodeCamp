import unittest

def find_landing_spot(matrix):
    minRiskArr = []
    minRisk = -1

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                risk = 0
                #calculating risk
                if j > 0:
                    risk += matrix[i][j-1]
                if j < len(matrix[i]) - 1:
                    risk += matrix[i][j+1]
                
                if i > 0:
                    risk += matrix[i-1][j]
                if i < len(matrix) - 1:
                    risk += matrix[i+1][j]

                if minRisk == -1:
                    minRisk = risk
                    minRiskArr = [i,j]

                if risk < minRisk:
                    minRisk = risk
                    minRiskArr = [i,j]
    
    return minRiskArr or None

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(find_landing_spot([[1, 0], [2, 0]]), [0, 1])
    def test2(self):
        self.assertEqual(find_landing_spot([[9, 0, 3], [7, 0, 4], [8, 0, 5]]), [1, 1])
    def test3(self):
        self.assertEqual(find_landing_spot([[1, 2, 1], [0, 0, 2], [3, 0, 0]]) , [2, 2])
    def test4(self):
        self.assertEqual(find_landing_spot([[9, 6, 0, 8], [7, 1, 1, 0], [3, 0, 3, 9], [8, 6, 0, 9]]), [2, 1])
    def test5(self):
        self.assertEqual(find_landing_spot([[1, 1], [2, 1]]), None)
    


if __name__ == '__main__':
    unittest.main()



#method2
# def find_landing_spot(matrix):
#     minRiskArr, minRisk = None, float('inf')

#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if matrix[i][j] == 0:
#                 # Calculate risk with boundary checks
#                 risk = sum(matrix[i+di][j+dj] 
#                            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)] 
#                            if 0 <= i+di < len(matrix) and 0 <= j+dj < len(matrix[i]))

#                 # Update minimum risk and position
#                 if risk < minRisk:
#                     minRisk, minRiskArr = risk, [i, j]

#     return minRiskArr

