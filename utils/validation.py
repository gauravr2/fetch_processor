import re

def validate_receipt(receipt):
    if not receipt:
        return "Receipt is empty."

    required_fields = ["retailer", "purchaseDate", "purchaseTime", "items", "total"]
    for field in required_fields:
        if field not in receipt:
            return f"Missing required field: {field}"

    if not re.match(r"^[\w\s\-&]+$", receipt["retailer"]):
        return "Invalid retailer name."

    if not re.match(r"^\d{4}-\d{2}-\d{2}$", receipt["purchaseDate"]):
        return "Invalid purchase date format. Expected YYYY-MM-DD."

    if not re.match(r"^\d+\.\d{2}$", receipt["total"]):
        return "Invalid total format. Expected decimal with two digits."

    if not isinstance(receipt["items"], list) or len(receipt["items"]) < 1:
        return "Items must be a non-empty array."

    for item in receipt["items"]:
        if "shortDescription" not in item or "price" not in item:
            return "Each item must have 'shortDescription' and 'price'."
        if not re.match(r"^[\w\s\-]+$", item["shortDescription"]):
            return "Invalid short description in an item."
        if not re.match(r"^\d+\.\d{2}$", item["price"]):
            return "Invalid price format in an item."

    return None
