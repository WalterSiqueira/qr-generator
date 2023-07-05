from flask import Flask, render_template, request
from packages.qr import qr
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    url = request.form.get('url')
    return qr.generate(url)

if __name__ == '__main__':
    app.run()