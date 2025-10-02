import random

from flask import Blueprint, render_template, request, json

from src.data.model.Contestant import Contestant
from src.data.model.Member import Member

enrollment_bp = Blueprint("enroll", __name__)


isRegistrationOpen = False

@enrollment_bp.get('/enroll')
def enroll():
    if isRegistrationOpen:
        return render_template('enrollment/enroll.html')
    else:
        return render_template('enrollment/preEnrollment.html')

@enrollment_bp.post('/enroll')
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
    # global_contestants.append(contestant)

    return render_template('enrollment/enroll.html', isEnrolled= enrollmentSuccessful)


