from flask import Blueprint, render_template, request, make_response
from flask_limiter.util import get_remote_address

active_party_bp = Blueprint("active_party", __name__)

@active_party_bp.route("/party")
def party():
    return render_template("active_party/dashboard.html")