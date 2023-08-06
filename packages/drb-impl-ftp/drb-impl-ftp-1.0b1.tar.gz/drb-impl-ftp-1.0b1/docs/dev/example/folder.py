from drb_impl_ftp import DrbFtpNode, DrbFtpAttributeNames
from drb_impl_ftp.basic_auth import BasicAuth

node = DrbFtpNode("YOUR_URL_SERVER", host="YOUR_HOST", auth=BasicAuth("USER", "PWD"))

# Return true if the file is a directory False otherwise
node['file.txt'].get_attribute( DrbFtpAttributeNames.DIRECTORY.value)
