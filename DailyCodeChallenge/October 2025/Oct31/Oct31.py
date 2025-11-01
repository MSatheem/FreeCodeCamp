import unittest

def spookify(boo):
    #replacing _ and - with  ~
    replaced_text = boo.replace("_", "~").replace("-","~")
    #variable to store spookified test
    spookified = ""
    count = 0;
    for i in replaced_text:
        if i != '~':
            count += 1
            if count%2 != 0:
                #capitalize characters in even postion
                i = i.upper()
            else : 
                #small charactes in odd positoin
                i = i.lower();
        spookified = spookified + i
    return spookified

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(spookify("hello_world"),"HeLlO~wOrLd")
    def test2(self):
        self.assertEqual(spookify("Spooky_Case"), "SpOoKy~CaSe")
    def test3(self):
        self.assertEqual(spookify("TRICK-or-TREAT"), "TrIcK~oR~tReAt")
    def test4(self):
        self.assertEqual(spookify("c_a-n_d-y_-b-o_w_l"), "C~a~N~d~Y~~b~O~w~L")
    def test5(self):
        self.assertEqual(spookify("thE_hAUntEd-hOUsE-Is-fUll_Of_ghOsts"), "ThE~hAuNtEd~HoUsE~iS~fUlL~oF~gHoStS")


if __name__ == '__main__':
    unittest.main()

# print(spookify("hello_world"))