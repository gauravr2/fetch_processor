from flask import jsonify
from services.receipt_service import calculate_points
from utils.validation import validate_receipt
from storage.storage import MemoryStore
import uuid


store = MemoryStore()

def process_receipt(request):
    try:
        receipt = request.get_json()
        validation_error = validate_receipt(receipt)
        if validation_error:
            return jsonify({"error": "The receipt is invalid."}), 400
        
        receipt_id = str(uuid.uuid4())
        points = calculate_points(receipt)

        store.add(receipt_id, points)
        return jsonify({"id": receipt_id}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_points(receipt_id):
    points = store.get(receipt_id)
    if points is None:
        return jsonify({"error": "No receipt found for that ID."}), 404
    return jsonify({"points": points}), 200
