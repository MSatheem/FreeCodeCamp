import unittest
import math

def goldilocks_zone(mass):
    luminosity = mass ** 3.5
    startZone = 0.95 * luminosity ** 0.5
    endZone = 1.37 * luminosity ** 0.5
    return [round(startZone,2), round(endZone,2)]

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(goldilocks_zone(1), [0.95, 1.37])
    def test2(self):
        self.assertEqual(goldilocks_zone(0.5), [0.28, 0.41])
    def test3(self):
        self.assertEqual(goldilocks_zone(6), [21.85, 31.51])
    def test4(self):
        self.assertEqual(goldilocks_zone(3.7), [9.38, 13.52])
    def test5(self):
        self.assertEqual(goldilocks_zone(20), [179.69, 259.13])

if __name__ == '__main__':
    unittest.main()
