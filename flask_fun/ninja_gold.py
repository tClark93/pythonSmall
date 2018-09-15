from flask import Flask, render_template, request, redirect, session
from random import randint
from datetime import datetime
app = Flask(__name__)
app.secret_key = 'gold_secret'
# secret keys encrypt sessions, you can't start without it

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activity' not in session:
        session['activity'] =[]
    return render_template("ninja_gold.html", gold = session['gold'], activity=session['activity'])

@app.route('/process', methods=['POST'])
def process():
    activity = session['activity']
    if request.form['action'] == 'farm':
        reward = randint(10,20)
        session['gold'] += reward
        activity.insert(0,"Earned "+ str(reward) +" gold from the farm! (" +str(datetime.now())+")")
    elif request.form['action'] == 'cave':
        reward = randint(5,10)
        session['gold'] += reward
        activity.insert(0,"Earned "+ str(reward) +" gold from the cave! (" +str(datetime.now())+")")
    elif request.form['action'] == 'house':
        reward = randint(2,5)
        session['gold'] += reward
        activity.insert(0,"Earned "+ str(reward) +" gold from the house! (" +str(datetime.now())+")")
    elif request.form['action'] == 'casino' and session['gold'] == 0:
        activity.insert(0,"You're poor, leave")
    elif request.form['action'] == 'casino':
        reward = randint(-50,50)
        if reward < 0:
            session['gold']+= reward
            color = 'red'
            if session['gold'] < 0:
                session['gold'] = 0
            activity.insert(0, "You've lost " + str(reward) + " gold at the casino(" +str(datetime.now())+")")
        if reward >= 0:
            session['gold']+= reward
            color = 'green'
            activity.insert(0, "You've won " + str(reward) + " money at the casino.(" +str(datetime.now())+")")
    session['activity'] = activity
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')
        # if session['gold'] < 1:
        #     # activity.insert(0,"Too poor gamble")
        # if session['gold'] >= 1 and session['gold'] < 50:
        #     # reward = randint(-session['gold'],session[gold])
        # if session['gold'] >= 50
        #     # reward = randint(-50,50)

# @app.route('/correct')
# def index():
    # value = 
    # return render_template("great_number_game.html", session=session, value='', color='green', result='Correct!')

if __name__=="__main__":
    app.run(debug='true')