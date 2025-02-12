from app.services import calculate_points

def test_points_calculation():
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

    expected_points = 28  # Based on the example
    assert calculate_points(sample_receipt) == expected_points
