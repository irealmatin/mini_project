from PIL import Image
from pyzbar.pyzbar import decode

img = Image.open('C:/Users/ireal/OneDrive/دسکتاپ/Here/qr.png')
res = decode(img)

print(res)
