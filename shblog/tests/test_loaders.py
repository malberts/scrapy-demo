import unittest
from ..loaders import Strip


class TestStrip(unittest.TestCase):
    def test_with_strip_whitespace(self):
        """Empty and whitespace only items must be removed."""
        strip = Strip(strip_whitespace=True)
        result = strip(["a", "", " ", "b"])
        self.assertListEqual(result, ["a", "b"])

    def test_without_strip_whitespace(self):
        """Only empty items must be removed."""
        strip = Strip(strip_whitespace=False)
        result = strip(["a", "", " ", "b"])
        self.assertListEqual(result, ["a", " ", "b"])
