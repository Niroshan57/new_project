import qrcode

qr = qrcode.QRCode(
    version=2,
    box_size=10,
    border=2
    )

studentID = input ("Enter studentID: ")

qr.add_data(studentID)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save(f"{studentID}.png")