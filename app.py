from flask import Flask, render_template

app = Flask(__name__)

isRegistrationOpen = True

@app.route('/')
def index():  # put application's code here
    return render_template('pumpkin.html')

@app.get('/home')
def home():
    return render_template('home.html')

@app.route('/enroll')
def enroll():
    if isRegistrationOpen:
        return render_template('enroll.html')
    else:
        return render_template('preEnrollment.html')


@app.get('/admin')
def admin():
    return ""

if __name__ == '__main__':
    app.run()
