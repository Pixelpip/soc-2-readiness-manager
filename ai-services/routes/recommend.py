from flask import Blueprint, request, jsonify

recommend_bp = Blueprint("recommend", __name__)

@recommend_bp.post("/recommend")
def recommend():
    data = request.get_json(force=True)
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "text is required"}), 400

    # Service logic will go here on Day 4
    return jsonify({"result": "recommend endpoint ready", "input": text})