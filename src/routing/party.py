from flask import Blueprint, render_template, request, make_response
from flask_limiter.util import get_remote_address

party_bp = Blueprint("party", __name__)

@party_bp.route("/party")
def party():
    return render_template("party/dashboard.html")