import unittest

from basic_programming.input_output import find_product, sum_ab


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


class TestComplexityAnalysis(unittest.TestCase):
    def test_ab(self):
        """
        Tests that it can sum two given numbers
        """
        answer_list = [3, 7, 24]
        input_list = [[1, 2], [2, 5], [10, 14]]
        for i in range(len(answer_list)):
            print('i: {}'.format(i))
            self.assertEqual(answer_list[i],
                             sum_ab(input_list[i][0], input_list[i][1]))


if __name__ == '__main__':
    unittest.main()
