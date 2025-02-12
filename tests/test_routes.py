import pytest
import json
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    return app.test_client()

# Sample receipt data for testing
sample_receipt = {
    "retailer": "Target",
    "purchaseDate": "2022-01-01",
    "purchaseTime": "13:01",
    "items": [
        { "shortDescription": "Mountain Dew 12PK", "price": "6.49" },
        { "shortDescription": "Emils Cheese Pizza", "price": "12.25" },
        { "shortDescription": "Knorr Creamy Chicken", "price": "1.26" },
        { "shortDescription": "Doritos Nacho Cheese", "price": "3.35" },
        { "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ", "price": "12.00" }
    ],
    "total": "35.35"
}

def test_process_receipt(client):
    response = client.post("/receipts/process", data=json.dumps(sample_receipt), content_type='application/json')
    assert response.status_code == 200
    response_json = response.get_json()
    assert "id" in response_json

def test_get_points_invalid_id(client):
    response = client.get("/receipts/invalid-id/points")
    assert response.status_code == 404
    response_json = response.get_json()
    assert response_json["error"] == "Receipt not found"
