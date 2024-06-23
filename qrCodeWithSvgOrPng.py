import qrcode
import inquirer
from xml.etree import ElementTree as ET


def save_qr_code(data, file_format='png', file='qr_code'):
    qr = qrcode.QRCode(
        version=3,
        box_size=20,
        border=10,
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )

    qr.add_data(data)
    qr.make(fit=True)

    if file_format.lower() == 'svg':
        file_name=f"{file}.svg"
        img = qr.make_image(fill_color="#DBEE49", back_color="#2D1B81")
        img.save(file_name)
        
    elif file_format.lower() == 'png':
        file_name = f"{file}.png"
        img = qr.make_image(fill_color="#DBEE49", back_color="#2D1B81")
 
        img.save(file_name)
    else:
        raise ValueError("Unsupported file format. Please choose 'svg' or 'png'.")

    print(f"QR code saved as {file_name}")

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#edit the data variable to generate a QR code for your URL
#edit the fileName variable to name your QR code file
data = "https://satr.codes/"
fileName = "qr_code"
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
file_format_question = [
    inquirer.List('file_format',
                  message="Choose the file format:",
                  choices=['SVG', 'PNG'],
                  ),
]

answers = inquirer.prompt(file_format_question)

if answers['file_format'] == 'SVG':
    save_qr_code(data, 'svg', fileName)
else:
    save_qr_code(data, 'png', fileName)
