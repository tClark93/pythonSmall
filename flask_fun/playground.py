from flask import Flask, render_template
app = Flask(__name__)
@app.route('/play')
def index():
    return render_template("playground.html", times=3, color="lightblue")
@app.route('/play/<num>')
def play(num): 
    return render_template("playground.html", times=int(num), color="lightblue")
@app.route('/play/<num>/<shade>')
def colors(num,shade):
    return render_template("playground.html", times=int(num), color=shade)

app.run(debug=True)