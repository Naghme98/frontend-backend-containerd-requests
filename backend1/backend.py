# backend1.py
from flask import Flask

app = Flask(__name__)

@app.route('/backend1')
def backend1():
    return 'reached backend1'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
