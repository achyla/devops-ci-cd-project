from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Endpoint / działa ✅"

@app.get('/products')
def products():
    data = [
        {"id": 1, "name": "Dzik", "price": 10.99},
        {"id": 2, "name": "Lays", "price": 12.99},
        {"id": 3, "name": "Castrol W5-30 5L", "price": 209.99},
    ]
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)