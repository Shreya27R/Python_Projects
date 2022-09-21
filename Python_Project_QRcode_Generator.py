
# #code -1 -------------------------------------
# #for qr code generation using module
import qrcode as qr
#qrcode to be saved as png
img=qr.make("Hello Shreya")
# #save the qrcode with the name mentioned in quotes(png)
# img.save("hello.png")



#code 2 below ------------------------------------

import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=10,)
qr.add_data("Powerful girl")
qr.make(fit=True)

img=qr.make_image(fill_color="red",back_color="blue")
img.save("Image.png")
