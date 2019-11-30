import unittest
from io import StringIO
from unittest.mock import patch

from basic_programming.input_output import find_product, zoos, count_divisors


class TestInputOutput(unittest.TestCase):
    def test_find_product(self):
        """
        Test that it can find the product of
        a list of ints
        """
        list_size = 5
        int_list = [1, 2, 3, 4, 5]  # 120

        list_size2 = 6
        int_list2 = [1, 2, 3, 4, 5, 6]  # 720

        list_size3 = 8
        int_list3 = [7, 8, 3, 2, 9, 3, 2, 3]  # 54,432

        # Assert correct return values
        self.assertEqual(120, find_product(list_size, int_list))
        self.assertEqual(720, find_product(list_size2, int_list2))
        self.assertEqual(54432, find_product(list_size3, int_list3))

        # assert exception raised on wrong type
        n = 'String'
        n2 = 2
        with self.assertRaises(TypeError):
            find_product(n, int_list)
            find_product(list_size, n2)
        with self.assertRaises(ValueError):
            find_product(list_size, n)

    @patch('sys.stdout', new_callable=StringIO)
    def test_zoos(self, mock_stdout):
        zoos('zzzoooooo')
        zoos('zzzooooooo')
        assert mock_stdout.getvalue() == 'Yes\nNo\n'

    @patch('sys.stdout', new_callable=StringIO)
    def test_count_divisors(self, mock_stdout):
        count_divisors(1, 10, 1)
        count_divisors(2, 10, 2)
        assert mock_stdout.getvalue() == '10\n5\n'


if __name__ == '__main__':
    unittest.main()
