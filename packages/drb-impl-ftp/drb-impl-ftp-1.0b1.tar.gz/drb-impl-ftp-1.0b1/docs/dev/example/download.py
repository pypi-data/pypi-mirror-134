import io
from drb_impl_ftp import DrbFtpNode
from drb_impl_ftp.basic_auth import BasicAuth

node = DrbFtpNode("YOUR_URL_SERVER", host="YOUR_HOST", auth=BasicAuth("USER", "PWD"))

# Download all the file
with node['file.txt'].get_impl(io.BytesIO) as stream:
    stream.read().decode()

# Download only the five first byte of the file
with node['file.txt'].get_impl(io.BytesIO) as stream:
    stream.read(5).decode()
