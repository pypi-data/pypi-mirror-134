from drb_impl_ftp import DrbFtpNode
from drb_impl_ftp.basic_auth import BasicAuth
from ftplib import FTP_TLS

# To connect to a simple FTP server
node = DrbFtpNode("YOUR_URL_SERVER", host="YOUR_HOST", auth=BasicAuth("USER", "PWD"))

# to connect to a server using TLS protocol PROTOCOL_TLS
node = DrbFtpNode("YOUR_URL_SERVER", host="YOUR_HOST", auth=BasicAuth("USER", "PWD"), protocol=FTP_TLS)
