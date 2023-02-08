import unittest

from helper import clean_path


class TestPathMethods(unittest.TestCase):
    def test_clean_path(self):
        clean_path_test = "path/to/file/"
        unclean_path_test = "path/to/file"

        assert clean_path(clean_path_test) == "path/to/file/"
        assert clean_path(unclean_path_test) == "path/to/file/"
