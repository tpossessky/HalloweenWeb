from __future__ import annotations

from typing import List

from flask import Flask, render_template, make_response, request, url_for
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import random
from data.Contestant import Contestant
from data.Member import Member
from utils import utils
import json

app = Flask(__name__)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://",
)


from active_party_routes import active_party_bp
app.register_blueprint(active_party_bp)

isRegistrationOpen = False
ideas : List[str] = []
global_contestants: List[Contestant] = []


@app.route('/')
@limiter.limit("1/second", override_defaults=False)
def index():
    hasVisited = request.cookies.get('hasVisited', '0')
    showAnimation = (hasVisited != '1')
    print(f'showAnimation: {showAnimation}')
    resp = make_response(render_template('pumpkin.html', showAnimation= showAnimation))
    resp.set_cookie('hasVisited', '1')
    return resp

@app.get('/home')
@limiter.limit("1/second", override_defaults=False)
def home():
    return render_template('home.html')

@app.get('/enroll')
@limiter.limit("1/second", override_defaults=False)
def enroll():
    if isRegistrationOpen:
        return render_template('enroll.html')
    else:
        return render_template('preEnrollment.html')

@app.post('/enroll')
@limiter.limit("1/second", override_defaults=False)
def enroll_post():

    enrollmentSuccessful = False
    contest_type = request.form.get("contest_type")
    contestant = Contestant()
    contestantID = random.randint(1, 5000)

    if contest_type == 'individual':
        memberID = random.randint(1, 5000)

        realName = request.form.get("full_name")
        costume = request.form.get("individual_costume")
        contestant.members = [Member(memberID ,realName, costume)]
        enrollmentSuccessful = True

    else:
        groupCostume = request.form.get("group_costume")
        group_members_json = request.form.get("group_members_data")
        # Parse the JSON data
        if group_members_json:
            groupJSON = json.loads(group_members_json)
            group_members = []

            for member in groupJSON:
                memberID = random.randint(0, 5000)
                group_members.append(Member(memberID, member['name'], member['costume']))
                print(f"  - {member['name']} as {member['costume']}")

            contestant.id = contestantID
            contestant.members = group_members
            contestant.isGroup = True
            contestant.groupCostume = groupCostume
            enrollmentSuccessful = True
        else:
            print("No group members found")
        #TODO: create data structure for users/contestants

    contestant.id = contestantID

    print(contestant)
    global_contestants.append(contestant)

    return render_template('enroll.html', isEnrolled= enrollmentSuccessful)


@app.get('/preroll')
@limiter.limit("1/second", override_defaults=False)
def preroll():
    return render_template('preEnrollment.html')


@app.route('/I_Guess_Were_Not_Good_Enough_For_You', methods=['GET','POST'])
@limiter.limit("1/second", override_defaults=False)
def suggest():
    errorMsg = ""
    submitted = False

    if request.method == 'POST':
        idea = request.form.get('idea')
        errorMsg = utils.get_error_message(idea)
        submitted = True
        ideas.append(idea)

    return render_template('suggest.html', errorMsg=errorMsg, submitted=submitted)

@app.get('/ideas')
@limiter.limit("1/second", override_defaults=False)
def get_ideas():
    return ideas

@app.get('/admin')
@limiter.limit("1/second", override_defaults=False)
def admin():
    """
    Basically return everything?
    1. Show ideas
    2. Show users
    3. song requests
    """
    return ""


@app.get('/admin/contestants')
@limiter.limit("1/second", override_defaults=False)
def get_contestants():
    return global_contestants

@app.post('/start-voting-process')
@limiter.limit("1/second", override_defaults=False)
def start_voting_process():
    print('start_vote')

@app.post('/stop-voting-process')
@limiter.limit("1/second", override_defaults=False)
def stop_voting_process():
    print('stop_vote')

@app.post('/tally-votes')
@limiter.limit("1/second", override_defaults=False)
def tally_votes():
    print('tally_votes')

@app.errorhandler(429)
def slowdown_cowboy(something):
    return "Slow down there partner!"



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
