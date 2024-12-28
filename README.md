# QR-Code-Generator-Python 🚀

A simple web app to generate QR codes using Python, Flask, and the qrcode library. Just enter your data (text, URL, etc.), and the app will generate a corresponding QR code! 🧑‍💻

Features ✨
Generate QR codes from any input data like text, URLs, or other information 📱
Easy-to-use interface with a simple form to enter the data 📑
Download your QR code image or view it directly on the screen 🖼️

How It Works 🛠️
Visit the Web App 🌐: Open the QR code generator web app in your browser.
Enter Data 📝: Input any data (text, URL, etc.) in the provided form field.
Generate QR Code 🔄: Click the "Generate QR Code" button to create the QR code.
View and Download 🔍: See the generated QR code on the results page and optionally download the image.

Installation 🏗️
To run this QR Code Generator on your local machine, follow these steps:

Clone this Repository: Download or clone the repository to your local machine.

Install Dependencies:
Make sure you have Python installed. Then, install the required libraries using: pip install flask qrcode[pil]

Run the Application:
Start the Flask app with: python app.py

Access the App: Open your browser and go to http://127.0.0.1:5000/ to start generating QR codes! 🌍

Folder Structure 📂
qr-code-generator/ │
├── app.py # Main Python file with Flask routes
├── static/
│ ├── qr_codes/ # Folder to store generated QR code images
├── templates/
│ ├── index.html # Form page for input data
│ └── result.html # Page to display the generated QR code
├── requirements.txt # List of required packages
└── README.md # This file

![image](https://github.com/user-attachments/assets/0c191b7b-9ae3-435a-ac1b-61590be8ca96)
![image](https://github.com/user-attachments/assets/2205fac0-f9a2-40c9-a3f6-ca2273b70b78)

Happy coding! 💻🔧
