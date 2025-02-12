from flask import Blueprint, request, jsonify
import uuid
from app.services import calculate_points

receipt_blueprint = Blueprint("receipt", __name__)

# In-memory storage
receipts_db = {}

@receipt_blueprint.route("/receipts/process", methods=["POST"])
def process_receipt():
    receipt = request.json
    receipt_id = str(uuid.uuid4())
    points = calculate_points(receipt)
    receipts_db[receipt_id] = points
    return jsonify({"id": receipt_id})

@receipt_blueprint.route("/receipts/<receipt_id>/points", methods=["GET"])
def get_points(receipt_id):
    if receipt_id not in receipts_db:
        return jsonify({"error": "Receipt not found"}), 404
    return jsonify({"points": receipts_db[receipt_id]})
