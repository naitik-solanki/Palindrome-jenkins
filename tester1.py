import unittest

from palindrome import isPalindrome

class TestCase(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(isPalindrome("malayalam"),True)

    def test_case2(self):
        self.assertEqual(isPalindrome("civic"),True)

    def test_case3(self):
        self.assertEqual(isPalindrome("rotar"),False)  

if __name__ == '__main__':
    unittest.main()