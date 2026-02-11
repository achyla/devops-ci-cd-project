from app.main import app
import json

def test_home_returns_200():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_products_returns_json_and_200():
    client = app.test_client()
    response = client.get("/products")

    assert response.status_code == 200
    assert response.is_json is True

    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) >= 1
    assert "name" in data[0]

def test_get_single_product():
    client = app.test_client()
    response = client.get("/products/1")
    
    assert response.status_code == 200
    data = response.get_json()
    assert data["id"] == 1
    assert "name" in data
    assert "price" in data

def test_get_single_product_not_found():
    client = app.test_client()
    response = client.get("/products/9999")
    
    assert response.status_code == 404
    data = response.get_json()
    assert "error" in data

def test_create_product():
    client = app.test_client()
    new_product = {"name": "Test Product", "price": 99.99}
    response = client.post("/products", 
                          data=json.dumps(new_product),
                          content_type='application/json')
    
    assert response.status_code == 201
    data = response.get_json()
    assert data["name"] == "Test Product"
    assert data["price"] == 99.99
    assert "id" in data

def test_create_product_missing_fields():
    client = app.test_client()
    response = client.post("/products", 
                          data=json.dumps({"name": "Incomplete"}),
                          content_type='application/json')
    
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data

def test_update_product():
    client = app.test_client()
    updated_data = {"name": "Updated Name", "price": 15.99}
    response = client.put("/products/1",
                         data=json.dumps(updated_data),
                         content_type='application/json')
    
    assert response.status_code == 200
    data = response.get_json()
    assert data["name"] == "Updated Name"
    assert data["price"] == 15.99

def test_update_product_not_found():
    client = app.test_client()
    response = client.put("/products/9999",
                         data=json.dumps({"name": "Test"}),
                         content_type='application/json')
    
    assert response.status_code == 404

def test_delete_product():
    client = app.test_client()
    # Najpierw dodaj produkt do usunięcia
    new_product = {"name": "To Delete", "price": 1.00}
    create_response = client.post("/products", 
                                 data=json.dumps(new_product),
                                 content_type='application/json')
    product_id = create_response.get_json()["id"]
    
    # Usuń produkt
    response = client.delete(f"/products/{product_id}")
    assert response.status_code == 200
    data = response.get_json()
    assert "message" in data
    
    # Sprawdź, czy produkt został usunięty
    get_response = client.get(f"/products/{product_id}")
    assert get_response.status_code == 404

def test_delete_product_not_found():
    client = app.test_client()
    response = client.delete("/products/9999")
    
    assert response.status_code == 404