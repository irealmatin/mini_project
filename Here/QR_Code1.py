import qrcode

my_data = 'https://github.com/irealmatin'

the_qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)
the_qr.add_data(my_data)
the_qr.make(fit = True)
 
img = the_qr.make_image(fill_color = "blue", back_color = "white")

img.save('C:/Users/ireal/OneDrive/دسکتاپ/Here/qr.png')
