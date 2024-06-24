from flask import Flask, render_template, request, send_file
import qrcode
import qrcode.image.svg
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
    format = request.form.get('format')
    fill_color = request.form.get('fill_color')
    back_color = request.form.get('back_color')

    qr = qrcode.QRCode(
        version=3,
        box_size=20,
        border=10,
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )
    qr.add_data(data)
    qr.make(fit=True)

    if format == 'svg':
        img = qr.make_image(image_factory=qrcode.image.svg.SvgImage, fill_color=fill_color, back_color=back_color)
        ext = 'svg'
        mime = 'image/svg+xml'
    else:
        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        ext = 'png'
        mime = 'image/png'

    memo = BytesIO()
    img.save(memo)
    memo.seek(0)
    base64_img = f"data:{mime};base64," + b64encode(memo.getvalue()).decode('ascii')

    if not os.path.exists('static'):
        os.makedirs('static')

    file_path = f'static/qr_code.{ext}'
    with open(file_path, 'wb') as f:
        f.write(memo.getvalue())

    return render_template('index.html', qr_code=base64_img, file_path=file_path)

@app.route('/download')
def download():
    file_path = request.args.get('file_path')
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
