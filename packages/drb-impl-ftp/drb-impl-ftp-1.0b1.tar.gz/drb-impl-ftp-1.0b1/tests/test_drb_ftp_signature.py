import os
import sys
import unittest

from drb.factory import DrbFactoryResolver
from drb.utils.url_node import UrlNode
from drb.exceptions import DrbFactoryException


class TestDrbFtpFactory(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        path = os.path.dirname(__file__)

        cls.mock_package_path = os.path.abspath(
            os.path.join(path, 'resources'))
        sys.path.append(cls.mock_package_path)
        print(cls.mock_package_path)
        cls.resolver = DrbFactoryResolver()

    @classmethod
    def tearDownClass(cls) -> None:
        sys.path.remove(cls.mock_package_path)

    def test_resolve_ok(self):
        node = UrlNode('ftp://localhost:2121/test.txt')
        signature = self.resolver.resolve(node)
        self.assertEqual('ftp', signature[0].label)

    def test_resolve_fails(self):
        node = UrlNode('.')
        with self.assertRaises(DrbFactoryException):
            self.resolver.resolve(node)
