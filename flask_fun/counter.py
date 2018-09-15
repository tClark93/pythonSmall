from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'counterSecret'
@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] += 1
    return render_template("counter.html")
@app.route('/change', methods=['POST'])
def addTwo():
    if request.form['action'] == 'add':
        session['count'] += 1
    if request.form['action'] == 'clear':
        session['count'] = 0
    return redirect('/')
@app.route('/clear', methods=['POST'])
def clear():
    if request.form['action'] == 'clear':
        session['count'] = 0
    return redirect('/')
if __name__=="__main__":
    app.run(debug='true')