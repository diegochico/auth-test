import unittest
import sys

# Fake the input to pass the argparse argument control while testing
sys.argv = ['authentise.py', 'input', '-w']

from authentise import reverse_letters, reverse_words, reverse_control


class TestStringReversing(unittest.TestCase):

    # Test letters reversing function
    def test_reverse_l(self):
        self.assertEqual(reverse_letters('qwerty uiop'), 'poiu ytrewq')
        self.assertEqual(reverse_letters('qwerty \n uiop'), 'poiu \n ytrewq')

    # Test word reversing function
    def test_reverse_w(self):
        self.assertEqual(reverse_words('qwerty uiop'), 'uiop qwerty')
        self.assertEqual(reverse_words('qwerty \n uiop'), 'uiop \n qwerty')

    # Test command execution with mocking input
    def test_reverse_c(self):
        # Test command input
        sys.argv = ['authentise.py', 'qwerty uiop', '-r']
        self.assertEqual(reverse_control(sys.argv[1:]), 'poiu ytrewq')
        sys.argv = ['authentise.py', 'qwerty uiop', '-w']
        self.assertEqual(reverse_control(sys.argv[1:]), 'uiop qwerty')
        sys.argv = ['authentise.py', '', '-w']
        self.assertRaises(Exception, reverse_control(sys.argv[1:]))
        sys.argv = ['authentise.py', 'qwerty uiop', '']
        self.assertRaises(Exception, reverse_control(sys.argv[1:]))


if __name__ == '__main__':
    unittest.main()
