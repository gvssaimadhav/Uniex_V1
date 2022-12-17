import requests
import json
from flask import Flask, render_template,session, request, redirect,jsonify
from chat import get_response
from flask_recaptcha import ReCaptcha
import os
#import pymongo
#import bcrypt

app = Flask(__name__)

app.config.update({'RECAPTCHA_ENABLED': True,
                   'RECAPTCHA_SITE_KEY': 'Replace With Your Google Captcha Site Key',
                   'RECAPTCHA_SECRET_KEY': 'Replace With Your Google Captcha Secret Key'})


recaptcha = ReCaptcha(app=app)

GOOGLE_CLIENT_ID="Replace With Your Google OAuth Client ID"
GOOGLE_CLIENT_SECRET="Replace With Your Google OAuth Client Secret"

@app.route('/login')
def login():
    if request.args.get("next"):
        session["next"]=request.args.get("next")
    return redirect(f"https://accounts.google.com/o/oauth2/auth?scope=https://www.googleapis.com/auth/userinfo.profile&access_type=offline&include_granted_scopes=true&response_type=code&redirect_uri=http://127.0.0.1:5000/uniex&client_id={GOOGLE_CLIENT_ID}")

@app.route('/authorized')
def authorized():
    r=requests.post("https://oauth2.googleapis.com/token",data={
        'client_id':GOOGLE_CLIENT_ID,
        'client_secret':GOOGLE_CLIENT_SECRET,
        'code':request.args.get("code"),
        'grant_type':"authorization_code",
        'redirect_uri':"http://127.0.0.1:5000/uniex"
    })
    return r.json()
@app.get("/uniex")
def index_get():
    return render_template("base.html")

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    print('SUBMIT CALLED')
    username = ''
    password = ''

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

    print(request.form)

    if username == 'username' and password == 'password':
        print('CREDENTIALS ARE OK')

        r = requests.post('https://www.google.com/recaptcha/api/siteverify',
                          data={'secret':
                                'secret_key',
                                'response':
                                request.form['g-recaptcha-response']})

        google_response = json.loads(r.text)
        print('JSON: ', google_response)

        if google_response['success']:
            print('SUCCESS')
            return render_template('profile.html')
        else:
            # FAILED
            print('FAILED')
            return render_template('index.html')


#        if recaptcha.verify():
#            # SUCCESS

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)