from flask import Flask, render_template, make_response, request
from utils import utils
app = Flask(__name__)

isRegistrationOpen = True
ideas = []
@app.route('/')
def index():
    hasVisited = request.cookies.get('hasVisited', '0')
    showAnimation = (hasVisited != '1')
    print(f'showAnimation: {showAnimation}')
    resp = make_response(render_template('pumpkin.html', showAnimation=showAnimation))
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
    global isRegistrationOpen


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
def getIdeas():
    return ideas

@app.get('/admin')
def admin():
    """
    1. Show ideas
    2. Show users
    """
    return ""



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
    app.run()
