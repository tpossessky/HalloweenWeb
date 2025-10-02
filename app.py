from __future__ import annotations

from typing import List

from flask import Flask, render_template, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from src.routing.party import party_bp
from src.routing.admin import admin_bp
from src.routing.index import home_bp
from src.data.model.Contestant import Contestant
from src.routing.enrollment import enrollment_bp
from src.routing.error import error_routes_bp
from src.utils import utils


app = Flask(__name__)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["1 per second", "50 per hour"],
    storage_uri="memory://",
)


app.register_blueprint(home_bp)
app.register_blueprint(party_bp)
app.register_blueprint(enrollment_bp)
app.register_blueprint(error_routes_bp)
app.register_blueprint(admin_bp)

limiter.limit("1/second") (enrollment_bp)
limiter.limit("1/second") (party_bp)
limiter.limit("1/second") (error_routes_bp)
limiter.limit("1/second") (admin_bp)
limiter.limit("1/second") (home_bp)


ideas : List[str] = []
global_contestants: List[Contestant] = []


@app.route('/I_Guess_Were_Not_Good_Enough_For_You', methods=['GET','POST'])
def suggest():
    errorMsg = ""
    submitted = False

    if request.method == 'POST':
        idea = request.form.get('idea')
        errorMsg = utils.get_error_message(idea)
        submitted = True
        ideas.append(idea)

    return render_template('suggest.html', errorMsg=errorMsg, submitted=submitted)




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
