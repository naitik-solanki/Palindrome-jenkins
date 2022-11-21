import unittest

from palindrome import isPalindrome

class TestCase(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(isPalindrome("Malayalam"),True)

    def test_case2(self):
        self.assertEqual(isPalindrome("mAdam"),True) 

if __name__ == '__main__':
    unittest.main()