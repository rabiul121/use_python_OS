from tkinter.filedialog import test
from rearrange import rearrange_name
import unittest
from validations import validate_user

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Islam, Robiul"
        expected = "Robiul Islam"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)

    def test_double_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_single_name(self):
        testcase = "Volraire"
        expected = "Volraire"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_invalid_minlen(self):
        self.assertRaises(ValueError, validate_user, "user", -1)

unittest.main()
