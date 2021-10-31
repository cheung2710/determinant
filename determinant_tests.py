import unittest
from determinant import determinant


class Tests(unittest.TestCase):
    def test_1x1(self):
        m = [[100]]
        self.assertEqual(determinant(m), 100)

    def test_2x2(self):
        m = [[1, 2], [3, 4]]
        self.assertEqual(determinant(m), -2)

    def test_3x3_01(self):
        m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(determinant(m), 0)

    def test_3x3_02(self):
        m = [[8, -4, 7], [2, 7, 9], [-2, -9, 1]]
        self.assertEqual(determinant(m), 756)

    def test_4x4(self):
        m = [[8, 0, 6, -1], [7, 6, -6, 8], [2, 3, 4, 5], [1, 8, -10, 3]]
        self.assertEqual(determinant(m), -3562)


if __name__ == '__main__':
    unittest.main()
