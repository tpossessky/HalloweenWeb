from typing import List

from flask import Flask, render_template, make_response, request
import random
from data.Contestant import Contestant
from data.Member import Member
from utils import utils
import json

app = Flask(__name__)

isRegistrationOpen = True
ideas : List[str] = []
global_contestants: List[Contestant] = []


@app.route('/')
def index():
    hasVisited = request.cookies.get('hasVisited', '0')
    showAnimation = (hasVisited != '1')
    print(f'showAnimation: {showAnimation}')
    resp = make_response(render_template('pumpkin.html', showAnimation= showAnimation))
    resp.set_cookie('hasVisited', '1')
    return resp

@app.get('/home')
def home():
    return render_template('home.html')

@app.get('/enroll')
def enroll():
    if isRegistrationOpen:
        return render_template('enroll.html')
    else:
        return render_template('preEnrollment.html')

@app.post('/enroll')
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
def preroll():
    return render_template('preEnrollment.html')


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

@app.get('/ideas')
def get_ideas():
    return ideas

@app.get('/admin')
def admin():
    """
    1. Show ideas
    2. Show users
    """
    return ""


@app.get('/admin/contestants')
def get_contestants():
    return global_contestants

@app.post('/start-voting-process')
def start_voting_process():
    print('start_vote')

@app.post('/stop-voting-process')
def stop_voting_process():
    print('stop_vote')

@app.post('/tally-votes')
def tally_votes():
    print('tally_votes')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
