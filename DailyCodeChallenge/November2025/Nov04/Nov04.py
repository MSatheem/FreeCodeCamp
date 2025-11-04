import unittest

def image_search(images, term):
    term_matched = []
    for i in images:
        #if the string value  is not found: find() return -1
        if i.lower().find(term.lower()) != -1:
            #adding the matched element to the array
            term_matched.append(i) 
    return term_matched     


class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(image_search(["dog.png", "cat.jpg", "parrot.jpeg"], "dog"), ["dog.png"])
    def test2(self):
        self.assertEqual(image_search(["Sunset.jpg", "Beach.png", "sunflower.jpeg"], "sun"), ["Sunset.jpg", "sunflower.jpeg"])
    def test3(self):
        self.assertEqual(image_search(["Moon.png", "sun.jpeg", "stars.png"], "PNG"), ["Moon.png", "stars.png"])
    def test4(self):
        self.assertEqual(image_search(["cat.jpg", "dogToy.jpeg", "kitty-cat.png", "catNip.jpeg", "franken_cat.gif"], "Cat"),["cat.jpg", "kitty-cat.png", "catNip.jpeg", "franken_cat.gif"] )
    

if __name__ == '__main__':
    unittest.main()
