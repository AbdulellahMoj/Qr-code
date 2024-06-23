import qrcode

qr = qrcode.QRCode(version=3, box_size=20, border=10, error_correction=qrcode.constants.ERROR_CORRECT_H)

data = "https://satr.codes/"

qr.add_data(data)

qr.make(fit=True)

img = qr.make_image(fill_color="#DBEE49", back_color="#2D1B81")

img.save("qr_code.png")
print("QR code saved as qr_code.png")