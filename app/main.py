from flask import Flask, jsonify, request

app = Flask(__name__)

# Prosta "baza danych" w pamięci
products_db = [
    {"id": 1, "name": "Dzik", "price": 10.99},
    {"id": 2, "name": "Lays", "price": 12.99},
    {"id": 3, "name": "Castrol W5-30 5L", "price": 209.99},
]
next_id = 4

@app.route('/')
def home():
    return jsonify({"message": "Endpoint / jest dostępny ✅", "info": "Użyj /products, aby zobaczyć listę produktów."}), 200

# READ - Pobierz wszystkie produkty
@app.get('/products')
def get_products():
    return jsonify(products_db), 200

# READ - Pobierz pojedynczy produkt
@app.get('/products/<int:product_id>')
def get_product(product_id):
    product = next((p for p in products_db if p['id'] == product_id), None)
    if product is None:
        return jsonify({"error": "Produkt nie został znaleziony"}), 404
    return jsonify(product), 200

# CREATE - Dodaj nowy produkt
@app.post('/products')
def create_product():
    global next_id
    data = request.get_json()
    
    if not data or 'name' not in data or 'price' not in data:
        return jsonify({"error": "Wymagane pola: name, price"}), 400
    
    new_product = {
        "id": next_id,
        "name": data['name'],
        "price": float(data['price'])
    }
    products_db.append(new_product)
    next_id += 1
    
    return jsonify(new_product), 201

# UPDATE - Zaktualizuj produkt
@app.put('/products/<int:product_id>')
def update_product(product_id):
    product = next((p for p in products_db if p['id'] == product_id), None)
    if product is None:
        return jsonify({"error": "Produkt nie został znaleziony"}), 404
    
    data = request.get_json()
    if not data:
        return jsonify({"error": "Brak danych do aktualizacji"}), 400
    
    if 'name' in data:
        product['name'] = data['name']
    if 'price' in data:
        product['price'] = float(data['price'])
    
    return jsonify(product), 200

# DELETE - Usuń produkt
@app.delete('/products/<int:product_id>')
def delete_product(product_id):
    product = next((p for p in products_db if p['id'] == product_id), None)
    if product is None:
        return jsonify({"error": "Produkt nie został znaleziony"}), 404
    
    products_db.remove(product)
    return jsonify({"message": "Produkt został usunięty"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)