# backend/routes/main.py
from flask import Blueprint, jsonify, request, render_template
from backend.utils import wallet_utils  # o ajustalo si moviste la carpeta


import logging

main_bp = Blueprint("main", __name__)

logger = logging.getLogger(__name__)

@main_bp.route("/")
def index():
    return render_template("index.html")

@main_bp.route("/generate")
def generate():
    priv_key = wallet_utils.generate_private_key()
    pub_key = wallet_utils.private_to_public_key(priv_key)
    addresses = wallet_utils.generate_addresses(pub_key)
    return jsonify({"private_key": priv_key, "addresses": addresses})

@main_bp.route("/from_key", methods=["POST"])
def from_key():
    data = request.json
    key = data.get("key", "")
    if not key or len(key) != 64:
        return jsonify({"error": "Clave inválida"}), 400
    try:
        pub_key = wallet_utils.private_to_public_key(key)
        addresses = wallet_utils.generate_addresses(pub_key)
        return jsonify({"private_key": key, "addresses": addresses})
    except Exception as e:
        logger.exception("Error en /from_key")
        return jsonify({"error": str(e)}), 500
