import math
from datetime import datetime

def calculate_points(receipt):
    points = 0

    # Rule 1: One point for every alphanumeric character in the retailer name
    points += sum(c.isalnum() for c in receipt["retailer"])

    # Rule 2: 50 points if total is a round dollar amount (no cents)
    if float(receipt["total"]).is_integer():
        points += 50

    # Rule 3: 25 points if total is a multiple of 0.25
    if float(receipt["total"]) % 0.25 == 0:
        points += 25

    # Rule 4: 5 points for every two items
    points += (len(receipt["items"]) // 2) * 5

    # Rule 5: Points based on item description length (if length is multiple of 3)
    for item in receipt["items"]:
        trimmed_desc = item["shortDescription"].strip()
        if len(trimmed_desc) % 3 == 0:
            price_points = math.ceil(float(item["price"]) * 0.2)
            points += price_points

    # Rule 6: 6 points if purchase day is odd
    purchase_date = datetime.strptime(receipt["purchaseDate"], "%Y-%m-%d")
    if purchase_date.day % 2 == 1:
        points += 6

    # Rule 7: 10 points if time is after 2:00pm and before 4:00pm
    purchase_time = datetime.strptime(receipt["purchaseTime"], "%H:%M")
    if 14 <= purchase_time.hour < 16:
        points += 10

    return points
