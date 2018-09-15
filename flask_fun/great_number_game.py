from flask import Flask, render_template, request, redirect, session
from random import randint
app = Flask(__name__)
app.secret_key = 'number_secret'

@app.route('/')
def index():
    session['num'] = randint(1,5)
    return render_template("great_number_game.html", session=session, value='hidden')

@app.route('/guess', methods=['POST'])
def guess():
    if request.form['guess'] == session['num']:
        return redirect('/correct')
    if request.form['guess'] > session['num']:
        return redirect('/high')
    if request.form['guess'] < session['num']:
        return redirect('/low')

# @app.route('/correct')
# def index():
    # value = 
    # return render_template("great_number_game.html", session=session, value='', color='green', result='Correct!')

if __name__=="__main__":
    app.run(debug='true')