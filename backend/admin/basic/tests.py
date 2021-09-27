from django.test import TestCase
import unittest
# Create your tests here.
from basic.models import MySum, Palindrome

class TestMySum(unittest.TestCase):

    def test_one_to_ten_sum_1(self):
        instance = MySum()
        instance.start_number = 1
        instance.end_number = 11
        res = instance.one_to_ten_sum_2()
        print(f'My Expected Value is {res}')
        self.assertEqual(res, 55)


class TestPalindrome(unittest.TestCase):

    def test_palindrome(self):
        instance = Palindrome()
        self.assertEqual(instance.isPalindrome(instance.str_to_list("A man, a plan, a canal: Panama"))["Result"], True)

if __name__ == '__main__':
    unittest.main()