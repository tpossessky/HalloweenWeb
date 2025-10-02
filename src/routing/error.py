from flask import Blueprint

error_routes_bp = Blueprint("error", __name__)

@error_routes_bp.errorhandler(429)
def slowdown_cowboy(_):
    return "Slow down there partner!"
