import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

link = input("input link, ")
qr = pyqrcode.create(link)
qr.png("myCode.png", scale=8)

d = decode(Image.open("mycode.png"))
print(d[0].data.decode("ascii"))