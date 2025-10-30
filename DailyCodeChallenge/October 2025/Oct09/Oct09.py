import unittest
from datetime import datetime, date

def moon_phase(date_string):
    date_start = date(2000,1,6)
    date_given = datetime.strptime(date_string, "%Y-%m-%d").date()
    days_difference = (date_given - date_start).days
    phase = (days_difference % 28) + 1
    if phase <= 7:
        return "New"
    elif phase <=14:
        return "Waxing"
    elif phase <= 21:
        return "Full"
    else :
        return "Waning"
    
class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(moon_phase("2000-01-12"), "New")
    def test2(self):
        self.assertEqual(moon_phase("2000-01-13"), "Waxing")
    def test3(self):
        self.assertEqual(moon_phase("2014-10-15"), "Full")
    def test4(self):
        self.assertEqual(moon_phase("2012-10-21"), "Waning")
    def test5(self):
        self.assertEqual(moon_phase("2022-12-14"), "New")






if __name__ == '__main__':
    unittest.main()
