import io
import time
import unittest
from multiprocessing import Process
import re

from drb_impl_ftp import DrbFtpNode, DrbFtpAttributeNames
from drb_impl_ftp.basic_auth import BasicAuth
from tests.utility import PORT, PATH, start_serve


class TestDrbFtp(unittest.TestCase):
    process = Process(target=start_serve)
    url_ok = 'ftp://localhost:' + str(PORT) + PATH
    url_false = 'ftp://localhost:' + str(PORT) + PATH + '/NOT_HERE'
    node = DrbFtpNode(url_ok, auth=BasicAuth("user", "12345"))

    @classmethod
    def setUpClass(cls) -> None:
        cls.process.start()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.process.kill()
        cls.node.close()

    def test_check_class(self):
        self.assertTrue(issubclass(DrbFtpNode, DrbFtpNode))

    def test_not_found(self):
        node = DrbFtpNode(self.url_false, None,
                          auth=BasicAuth("user", "12345"))
        self.assertFalse(node.check_file_exist(node.name))

    def test_name(self):
        self.assertEqual('resources', self.node.name)

    def test_namespace_uri(self):
        self.assertIsNone(self.node.namespace_uri)

    def test_value(self):
        self.assertIsNone(self.node.value)

    def test_parent(self):
        self.assertIsNone(self.node.parent)
        child = self.node.children[0]
        self.assertEqual(self.node, child.parent)

    def test_attributes(self):
        self.assertTrue(self.node.get_attribute(
            DrbFtpAttributeNames.DIRECTORY.value))
        self.assertIsNone(self.node.get_attribute(
            DrbFtpAttributeNames.SIZE.value))
        children = self.node['test_file1.txt']
        self.assertFalse(children.get_attribute(
            DrbFtpAttributeNames.DIRECTORY.value))
        self.assertEqual(24, children.get_attribute(
            DrbFtpAttributeNames.SIZE.value))
        r = re.compile("[A-Z][a-z]{2} \d{2} \d{2}:\d{2}")
        self.assertIsNotNone(r.match(children.get_attribute(
            DrbFtpAttributeNames.MODIFIED.value)))

    def test_children(self):
        self.assertEqual(3, len(self.node.children))

    def test_download(self):
        with self.node['test_file1.txt'].get_impl(io.BytesIO) as stream:
            self.assertEqual('This is my awesome test.',
                             stream.read().decode())
        with self.node['test_file1.txt'].get_impl(io.BytesIO) as stream:
            self.assertEqual('T',
                             stream.read(1).decode())
