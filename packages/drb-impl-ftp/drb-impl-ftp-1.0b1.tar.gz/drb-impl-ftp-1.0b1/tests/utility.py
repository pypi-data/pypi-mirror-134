from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

PORT = 1026
PATH = '/tests/resources'


def start_serve():
    """This method allow us to launch a small http server for our tests."""
    authorizer = DummyAuthorizer()
    authorizer.add_user("user", "12345", ".", perm="elradfmw")

    handler = FTPHandler
    handler.authorizer = authorizer

    server = FTPServer(("localhost", 1026), handler)
    server.serve_forever()
