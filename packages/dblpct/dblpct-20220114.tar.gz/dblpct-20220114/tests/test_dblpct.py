import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from dblpct.dblpct import dblpct, dblpct_r


class TestDblpct(unittest.TestCase):
    def test_dblpct_1(self):
        arg1 = "test"
        expected = "test"
        actual = dblpct(arg1)
        self.assertEqual(expected, actual)

    def test_dblpct_2(self):
        arg1 = "%"
        expected = "%%"
        actual = dblpct(arg1)
        self.assertEqual(expected, actual)

    def test_dblpct_3(self):
        arg1 = "test%test"
        expected = "test%%test"
        actual = dblpct(arg1)
        self.assertEqual(expected, actual)

    def test_dblpct_4(self):
        arg1 = "http://example.com/%E3%83%86%E3%82%B9%E3%83%88URL"
        expected = "http://example.com/%%E3%%83%%86%%E3%%82%%B9%%E3%%83%%88URL"
        actual = dblpct(arg1)
        self.assertEqual(expected, actual)

    def test_dblpct_r_1(self):
        arg1 = "test"
        expected = "test"
        actual = dblpct_r(arg1)
        self.assertEqual(expected, actual)

    def test_dblpct_r_2(self):
        arg1 = "%test%"
        expected = "%test%"
        actual = dblpct_r(arg1)
        self.assertEqual(expected, actual)

    def test_dblpct_r_3(self):
        arg1 = "%test%%"
        expected = "%test%"
        actual = dblpct_r(arg1)
        self.assertEqual(expected, actual)

    def test_dblpct_r_4(self):
        arg1 = "%test%%%"
        expected = "%test%%"
        actual = dblpct_r(arg1)
        self.assertEqual(expected, actual)

    def test_dblpct_r_5(self):
        arg1 = "%"
        expected = "%"
        actual = dblpct_r(arg1)
        self.assertEqual(expected, actual)

    def test_dblpct_r_6(self):
        arg1 = "%%"
        expected = "%"
        actual = dblpct_r(arg1)
        self.assertEqual(expected, actual)

    def test_dblpct_r_7(self):
        arg1 = "%%%"
        expected = "%%"
        actual = dblpct_r(arg1)
        self.assertEqual(expected, actual)

    def test_dblpct_r_8(self):
        arg1 = "%%%%%"
        expected = "%%%"
        actual = dblpct_r(arg1)
        self.assertEqual(expected, actual)

    def test_dblpct_r_9(self):
        arg1 = "%%%test%%%"
        expected = "%%test%%"
        actual = dblpct_r(arg1)
        self.assertEqual(expected, actual)

    def test_dblpct_r_10(self):
        arg1 = "http://example.com/%E3%83%86%E3%82%B9%E3%83%88URL"
        expected = "http://example.com/%E3%83%86%E3%82%B9%E3%83%88URL"
        actual = dblpct_r(arg1)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
