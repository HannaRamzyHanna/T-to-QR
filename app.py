from flask import Flask, request, render_template_string
import qrcode
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_image = None
    if request.method == 'POST':
        text = request.form['text']
        qr = qrcode.make(text)
        buffered = BytesIO()
        qr.save(buffered, format="PNG")
        qr_image = base64.b64encode(buffered.getvalue()).decode()
    return render_template_string('''
        <form method="post">
            Text: <input type="text" name="text">
            <input type="submit" value="Generate QR Code">
        </form>
        {% if qr_image %}
            <img src="data:image/png;base64,{{ qr_image }}" alt="QR Code">
        {% endif %}
    ''', qr_image=qr_image)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)



