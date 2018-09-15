from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'shhhh'
@app.route('/')
def index():
    return render_template('registration_form.html', session=session)
@app.route('/register', methods=['POST'])
def register():
    confirm_session = session
    session['first_name'] = request.form['first_name']
    if len(request.form['first_name']) < 1:
        flash('Must enter first name!', 'firstNameAlert')
    session['last_name'] = request.form['last_name']
    if session['last_name'] =='':
        flash('Must enter last name!', 'lastNameAlert')
    session['email']=request.form['email']
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!", 'blankEmailAlert')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!", 'invalidEmailAlert')
    else:
        flash("Success!")
    session['password']=request.form['password']
    session['confirm_password']=request.form['confirm_password']
    if session['password'] == '':
        flash('Must enter password!', 'noPassAlert')
    if session['password'] != confirm_session['confirm_password']:
        flash('Confirm password does not match', 'confirmPassAlert')
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)