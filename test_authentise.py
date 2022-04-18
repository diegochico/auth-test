from authentise import reverse_letters, reverse_words
import unittest


class TestStringReversing(unittest.TestCase):
    # Test letters reversing function
    def test_reverse_l(self):
        self.assertEqual(reverse_letters('qwerty uiop'), 'poiu ytrewq')
        self.assertEqual(reverse_letters('qwerty \n uiop'), 'poiu \n ytrewq')
    # Test word reversing function
    def test_reverse_w(self):
        self.assertEqual(reverse_words('qwerty uiop'), 'uiop qwerty')
        self.assertEqual(reverse_words('qwerty \n uiop'), 'uiop \n qwerty')


if __name__ == '__main__':
    unittest.main()
