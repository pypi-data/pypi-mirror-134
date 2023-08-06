import unittest
from pokemontcgsdkasync.config import __pypi_package_name__, __github_username__, __github_repo_name__


class TestConfig(unittest.TestCase):

    def test_has_proper_package_name(self):
        self.assertEqual('pokemontcgsdkasync', __pypi_package_name__)

    def test_has_proper_github_username(self):
        self.assertEqual('Pole458', __github_username__)

    def test_has_proper_github_repo_name(self):
        self.assertEqual('pokemon-tcg-sdk-python-async', __github_repo_name__)
