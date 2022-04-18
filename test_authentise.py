from authentise import reverse_letters
import unittest
from unittest.mock import patch


class TestStringReversing(unittest.TestCase):
    # Test characters reversing with mocking input
    @patch('authentise.get_input')
    def test_reverse(self, mock_input):
        mock_input.return_value = 'qwerty uiop'
        self.assertEqual(reverse_letters(), 'poiu ytrewq')

    @patch('authentise.get_input')
    def test_reverse_empty(self, mock_input):
        mock_input.return_value = ''
        self.assertEqual(reverse_letters(), '')


if __name__ == '__main__':
    unittest.main()


if __name__ == '__main__':
    unittest.main()
