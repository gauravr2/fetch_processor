from flask import Flask, request, jsonify
from handlers.receipt_handler import process_receipt, get_points

app = Flask(__name__)

# Routes
@app.route("/receipts/process", methods=["POST"])
def process_receipts():
    return process_receipt(request)

@app.route("/receipts/<receipt_id>/points", methods=["GET"])
def get_receipt_points(receipt_id):
    return get_points(receipt_id)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
