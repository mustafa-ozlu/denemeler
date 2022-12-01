import pyqrcode
from pyqrcode import QRCode

s="https://github.com/mustafa-ozlu"

url=pyqrcode.create(s)

url.svg("qr.svg", scale=8)
