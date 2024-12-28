import os
import qrcode
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Folder to store generated QR codes
UPLOAD_FOLDER = 'static/qr_codes'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Home route that displays the form
@app.route('/')
def index():
    return render_template('index.html')

# Route to generate QR code
@app.route('/generate', methods=['POST'])
def generate_qr_code():
    if request.method == 'POST':
        data = request.form['data']  # The data to encode in QR code
        filename = f"{data[:10]}.png"  # Simple filename from first 10 characters of data
        
        # Full path to save the QR code image
        qr_code_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        # Generate the QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        
        img = qr.make_image(fill="black", back_color="white")
        img.save(qr_code_path)
        
        # Redirect to a page that displays the input, output, and QR code
        return render_template('result.html', data=data, filename=filename)

if __name__ == '__main__':
    app.run(debug=True)
