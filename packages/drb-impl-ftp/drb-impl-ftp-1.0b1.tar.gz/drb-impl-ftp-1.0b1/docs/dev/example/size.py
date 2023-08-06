from drb_impl_ftp import DrbFtpNode, DrbFtpAttributeNames
from drb_impl_ftp.basic_auth import BasicAuth

node = DrbFtpNode("YOUR_URL_SERVER", host="YOUR_HOST", auth=BasicAuth("USER", "PWD"))

# Get the size of the file file1.txt
node['file.txt'].get_attribute( DrbFtpAttributeNames.SIZE.value)
