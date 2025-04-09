# backend/routes/donations.py
from flask import Blueprint, jsonify, request, render_template
from backend.utils import wallet_utils  # o ajustalo si moviste la carpeta




donations_bp = Blueprint("donations", __name__)

@donations_bp.route("/donations")
def donaciones():
    return jsonify({
        "author": wallet_utils.AUTHOR,
        "donation_addresses": wallet_utils.DONATION_ADDRESSES
    })
