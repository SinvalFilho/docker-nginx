from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({'message': 'O backend está funcionando !!!!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
