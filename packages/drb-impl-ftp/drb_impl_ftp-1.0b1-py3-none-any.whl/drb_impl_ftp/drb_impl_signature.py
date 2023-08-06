import uuid

from drb.factory import DrbSignature, DrbSignatureType, DrbFactory

from drb import DrbNode
from drb_impl_ftp import DrbFtpFactory


class DrbFtpSignature(DrbSignature):
    def __init__(self):
        self._factory = DrbFtpFactory()

    @property
    def uuid(self) -> uuid.UUID:
        return uuid.UUID('d61c923a-5f1b-11ec-bf63-0242ac130002')

    @property
    def label(self) -> str:
        return 'ftp'

    @property
    def category(self) -> DrbSignatureType:
        return DrbSignatureType.PROTOCOL

    @property
    def factory(self) -> DrbFactory:
        return self._factory

    def match(self, node: DrbNode) -> bool:
        if node.path.is_remote:
            scheme = node.path.scheme
            return scheme == 'ftp' or scheme == 'sftp' or scheme == 'ftps'
        return False
