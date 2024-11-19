import qrcode

data=input("Enter the url for which QR code has to be generated").strip() #to get rid of white spaces
filename=input("Enter the filename:").strip()
qr=qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image=qr.make_image(fill_color='blue',back_color='white')
image.save(filename)
print(f'QR Code saved as {filename}')
