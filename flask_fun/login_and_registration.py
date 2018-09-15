from flask import Flask, render_template, request, redirect, session, flash
import re, pymysql.cursors

class MySQLConnection:
    def __init__(self, db):
        connection = pymysql.connect(host = 'localhost',user = 'root', password = 'root', db = db, charset = 'utf8mb4', cursorclass = pymysql.cursors.DictCursor, autocommit = True)
        self.connection = connection
    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                executable = cursor.execute(query, data)
                if query.lower().find("insert") >= 0:
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    result = cursor.fetchall()
                    return result
                else:
                    self.connection.commit()
            except Exception as e:
                print("Something went wrong", e)
                flash("Email address already in use!",'doubleAlert')
def connectToMySQL(db):
    return MySQLConnection(db)

mysql = connectToMySQL('')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'register'


@app.route('/')
def index():
    # if 'allEmails' not in session:
    #     session['allEmails'] = []
    return render_template('login_and_registration.html', session=session)

@app.route('/success')
def reindex():
    return render_template('login_and_registration_success.html', session=session)

@app.route('/submit', methods=['POST'])
def register():
    confirm_session = session
    if len(request.form['firstName']) < 2:
        flash("Name must be two characters long", 'shortFirst')
    if request.form['firstName'].isalpha() == False:
        flash("Name cannot contain numbers", 'numFirst')
    if len(request.form['lastName']) < 2:
        flash("Name must be two characters long", 'shortLast')
    if request.form['lastName'].isalpha() == False:
        flash("Name cannot contain numbers", 'numLast')
    if not EMAIL_REGEX.match(request.form['registerEmail']):
        flash("Invalid Email Address", 'invalidEmail')
    if len(request.form['password']) < 8:
        flash("Name must be eight characters long", 'shortPass')
    if request.form['password'] != request.form['confirmPassword']:
        flash("Password fields must match", 'conPass')
    return redirect('/')
    # elif request.form['entered_email'] not in session:
    #     session['allEmails'] += request.form['entered_email']
    #     query = "INSERT INTO email (email_address, created_at, edited_at) VALUES (%(email_address)s, NOW(), NOW());"
    #     data = {'email_address': request.form['entered_email']}
    #     mysql.query_db(query, data)
    #     session['allEmails'] = mysql.query_db("SELECT * FROM email;")
    #     return redirect('/success')
    # elif request.form['entered_email'] in session:
    #     flash("Email address already in use!","doubleAlert")
    #     return redirect('/')
    # else:
    #     return redirect('/')

@app.route('/delete', methods=['POST'])
def delete():
    print('deleting')
    if request.form['submit'] == 'submit':
        request.form['value'] = x    
    query = "DELETE FROM email WHERE id='x'"
    return redirect('/success')

if __name__ == "__main__":
    app.run(debug=True)