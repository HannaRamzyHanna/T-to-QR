from flask import Flask, render_template, request, jsonify
import qrcode
import io
import base64
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data = request.form['data']
    qr = qrcode.make(data)
    buffer = io.BytesIO()
    qr.save(buffer, format='PNG')
    buffer.seek(0)
    qr_base64 = base64.b64encode(buffer.getvalue()).decode()
    return jsonify({'qr_code': qr_base64})

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5001  # Set default port to 5001
    app.run(debug=True, host='0.0.0.0', port=port)
