from math import ceil

def calculate_points(receipt):
    points = 0

    points += sum(c.isalnum() for c in receipt["retailer"])

    total = float(receipt["total"])
    if total.is_integer():
        points += 50

    if total % 0.25 == 0:
        points += 25

    items = receipt.get("items", [])
    points += (len(items) // 2) * 5

    for item in items:
        desc = item["shortDescription"].strip()
        if len(desc) % 3 == 0:
            points += ceil(float(item["price"]) * 0.2)

    purchase_date = receipt["purchaseDate"]
    day = int(purchase_date.split("-")[2])
    if day % 2 != 0:
        points += 6

    purchase_time = receipt["purchaseTime"]
    hour, _ = map(int, purchase_time.split(":"))
    if 14 <= hour < 16:
        points += 10

    return points
