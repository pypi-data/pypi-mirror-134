import unittest

from drb import DrbNode
from drb_impl_ftp import DrbFtpNode, DrbFtpFactory


class TestDrbFtpFactory(unittest.TestCase):

    def test_create(self):
        factory = DrbFtpFactory()
        node = factory.create('ftp://localhost:test.txt')
        self.assertIsInstance(node, (DrbFtpNode, DrbNode))
