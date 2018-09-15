from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("fruit_stand.html")
@app.route('/purchase_complete', methods=['POST'])
def results():
    return render_template("fruit_stand_created.html")
if __name__=="__main__":
    app.run(debug='true')