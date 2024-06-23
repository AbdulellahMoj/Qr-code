from flask import Flask, render_template, request, send_file
import qrcode
from io import BytesIO
from base64 import b64encode
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def genQrCode():
    data = request.form.get('link')

    # Create a QR code with custom colors
    qr = qrcode.QRCode(
        version=3,
        box_size=20,
        border=10,
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#DBEE49", back_color="#2D1B81")

    # Save image to a bytes buffer
    memo = BytesIO()
    img.save(memo)
    memo.seek(0)
    base64_img = "data:image/png;base64," + b64encode(memo.getvalue()).decode('ascii')

    # Ensure the static directory exists
    if not os.path.exists('static'):
        os.makedirs('static')

    # Save the QR code image to a static folder for download
    img.save('static/qr_code.png')

    return render_template('index.html', qr_code=base64_img)

@app.route('/download')
def download():
    return send_file('static/qr_code.png', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
