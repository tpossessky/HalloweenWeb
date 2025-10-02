from flask import Blueprint

admin_bp = Blueprint("admin", __name__)


@admin_bp.get('/admin')
def admin():
    """
    Basically return everything?
    1. Show ideas
    2. Show users
    3. song requests
    """
    return ""
