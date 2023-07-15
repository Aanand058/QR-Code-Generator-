import pyqrcode  as qr
from pyqrcode import QRCode 
   
link = input("Enter the url of the link site to generate QR Code: ")
  
# Generate QR code 
url = qr.create(link) 
  
# Create and save the file as "QR_Code.svg" 
url.svg("QR_Code.svg", scale = 8) 
