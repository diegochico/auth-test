from authentise import reverse_letters, reverse_words
import unittest
from unittest.mock import patch


class TestStringReversing(unittest.TestCase):
    # Test letters reversing with mocking input
    @patch('authentise.get_input')
    def test_reverse_l(self, mock_input):
        mock_input.return_value = 'qwerty uiop'
        self.assertEqual(reverse_letters(), 'poiu ytrewq')

    @patch('authentise.get_input')
    def test_reverse_empty_l(self, mock_input):
        mock_input.return_value = ''
        self.assertEqual(reverse_letters(), '')

    # Test word reversing with mocking input
    @patch('authentise.get_input')
    def test_reverse_w(self, mock_input):
        mock_input.return_value = 'qwerty uiop'
        self.assertEqual(reverse_words(), 'uiop qwerty')

    @patch('authentise.get_input')
    def test_reverse_empty_w(self, mock_input):
        mock_input.return_value = ''
        self.assertEqual(reverse_words(), '')


if __name__ == '__main__':
    unittest.main()
