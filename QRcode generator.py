
__author__ : '@rockdevu'

import pyqrcode
from pyqrcode import QRCode
import png

data = 'Hello This is rockdevu, The Creater, you can contact me anytime if you want to do project with me. Thank you'

(pyqrcode.create(data)).png('qrcode.png', scale=8)
