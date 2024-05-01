import pyqrcode #module
url = 'https://github.com/Deva6113/ybi-wine-quality-prediction.git'
k = pyqrcode.create(url) #variable declaration
k.svg('qrcode.svg', scale=10) #svg extension with qr code size 10
