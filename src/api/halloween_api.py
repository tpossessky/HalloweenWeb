from flask import Blueprint

api_bp = Blueprint("api", __name__)

@api_bp.get('/ideas')
def get_ideas():
    print('idea')


@api_bp.get('/tally-votes')
def tally_votes():
    print('tally_votes')


@api_bp.post('/register')
def register_user():
    print('reg user')


@api_bp.get('/admin/contestants')
def get_contestants():
    print('contestants')


@api_bp.post('/start-voting-process')
def start_voting_process():
    print('start_vote')


@api_bp.post('/stop-voting-process')
def stop_voting_process():
    print('stop_vote')