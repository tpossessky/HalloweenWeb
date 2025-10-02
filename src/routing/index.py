from flask import Blueprint, make_response, render_template, request

home_bp = Blueprint("home", __name__)


@home_bp.route('/')
def index():
    hasVisited = request.cookies.get('hasVisited', '0')
    showAnimation = (hasVisited != '1')
    print(f'showAnimation: {showAnimation}')
    resp = make_response(render_template('pumpkin.html', showAnimation= showAnimation))
    resp.set_cookie('hasVisited', '1')
    return resp

@home_bp.get('/home')
def home():
    return render_template('home.html')
