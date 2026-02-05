from app.main import app

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