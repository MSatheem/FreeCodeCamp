import unittest

def sort(emails):
    return sorted(emails, key=lambda email: (email.split('@')[1].lower(), (email.split('@')[0].lower())))
    


class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(sort(["jill@mail.com", "john@example.com", "jane@example.com"]),["jane@example.com", "john@example.com", "jill@mail.com"] )
    def test2(self):
        self.assertEqual(sort(["bob@mail.com", "alice@zoo.com", "carol@mail.com"]),["bob@mail.com", "carol@mail.com", "alice@zoo.com"])
    def test3(self):
        self.assertEqual(sort(["user@z.com", "user@y.com", "user@x.com"]),["user@x.com", "user@y.com", "user@z.com"])
    def test4(self):
        self.assertEqual(sort(["sam@MAIL.com", "amy@mail.COM", "bob@Mail.com"]) ,["amy@mail.COM", "bob@Mail.com", "sam@MAIL.com"])
    def test5(self):
        self.assertEqual(sort(["simon@beta.com", "sammy@alpha.com", "Sarah@Alpha.com", "SAM@ALPHA.com", "Simone@Beta.com", "sara@alpha.com"]),["SAM@ALPHA.com", "sammy@alpha.com", "sara@alpha.com", "Sarah@Alpha.com", "simon@beta.com", "Simone@Beta.com"])


if __name__ == '__main__':
    unittest.main()

# emails = ["jill@mail.com", "john@example.com", "jane@example.com"]
# sorted_email = sort(emails)
# print(sorted_email)