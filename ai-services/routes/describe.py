from flask import Blueprint, request, jsonify

describe_bp = Blueprint("describe", __name__)

@describe_bp.post("/describe")
def describe():
    data = request.get_json(force=True)
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "text is required"}), 400

    # Service logic will go here on Day 2
    return jsonify({"result": "describe endpoint ready", "input": text})