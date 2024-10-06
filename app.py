# Remove unused imports
from flask import Flask, request, jsonify
import qrcode

app = Flask(__name__)

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    # Your QR code generation logic
    pass

if __name__ == '__main__':
    app.run(debug=True)
