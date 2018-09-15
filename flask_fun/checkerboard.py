from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("checkerboard.html", x=8, y=8)
@app.route('/<num1>/<num2>')
def size(num1,num2):
    return render_template("checkerboard.html", x=int(num1), y=int(num2))
app.run(debug=True)