from drb_impl_ftp import DrbFtpNode
from drb_impl_ftp.basic_auth import BasicAuth

node = DrbFtpNode("YOUR_URL_SERVER", host="YOUR_HOST", auth=BasicAuth("USER", "PWD"))

# print(node.name)
if node.has_child():
    for e in node.children:
        # Do Something with your children
        print(e.name)
