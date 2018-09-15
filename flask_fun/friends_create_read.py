from flask import Flask, render_template, request, redirect, session
from mysqlconnection import connectToMySQL
app = Flask(__name__)

@app.route('/')
def index():
    print("Fetched all friends", all_friends)
    return render_template('friends_create_read.html', friends = all_friends)
@app.route('/create_friend', methods=['POST'])
def create():
    if request.form['action'] == 'submit':
        query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(occupation)s, NOW(), NOW());"
        data = {
                'first_name': request.form['first_name'],
                'last_name':  request.form['last_name'],
                'occupation': request.form['occupation']
            }
        mysql.query_db(query, data)
        return redirect('/')




if __name__ == "__main__":
    app.run(debug=True)