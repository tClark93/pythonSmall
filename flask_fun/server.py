from flask import Flask, render_template, request, redirect, session
from mysqlconnection import connectToMySQL
app = Flask(__name__)
mysql = connectToMySQL('names')
print("all the users", mysql.query_db("SELECT * FROM names;"))
if __name__ == "__main__":
    app.run(debug=True)