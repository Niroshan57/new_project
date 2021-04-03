from pyzbar.pyzbar import decode
from PIL import Image

data = decode(Image.open('guna123.png'))

print(data[0][0].decode('utf-8'))

#CV Computer Vision 
#openCV