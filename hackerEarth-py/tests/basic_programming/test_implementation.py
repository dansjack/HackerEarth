import unittest
from io import StringIO
from unittest.mock import patch

from basic_programming.implementation import count_digits


class TestImplementation(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_count_digits(self, mock_stdout):
        count_digits('77150')
        assert mock_stdout.getvalue() == '0 1\n1 1\n2 0\n3 0\n4 0\n5 1\n6 ' \
                                         '0\n7 2\n8 0\n9 0\n'
