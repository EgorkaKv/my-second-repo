import unittest
from src import zigzag


class MyTestCase(unittest.TestCase):

    def test_5_5(self):
        test_5 = zigzag.ZigZag([[11, 12, 13, 14, 15],
                                [21, 22, 23, 24, 25],
                                [31, 32, 33, 34, 35],
                                [41, 42, 43, 44, 45],
                                [51, 52, 53, 54, 55]], 5, 5)
        self.assertEqual(test_5.zigzag_r,
                         [55, 54, 45, 35, 44, 53, 52, 43, 34, 25, 15, 24, 33, 42, 51, 41, 32, 23, 14, 13, 22, 31, 21,
                          12, 11])

    def test_2_4(self):
        test_2 = zigzag.ZigZag([[11, 12, 13, 14],
                                [21, 22, 23, 24], ], 4, 2)
        self.assertEqual(test_2.zigzag_r, [24, 23, 14, 13, 22, 21, 12, 11])

    def test_1_6(self):
        test_6 = zigzag.ZigZag([[11],
                                [21],
                                [31],
                                [41],
                                [51],
                                [61]], 1, 6)
        self.assertEqual(test_6.zigzag_r, [11, 21, 31, 41, 51, 61, 11])


if __name__ == '__main__':
    unittest.main()
