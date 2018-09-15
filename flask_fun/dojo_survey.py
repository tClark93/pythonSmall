from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("dojo_survey.html")
@app.route('/result', methods = ['POST'])
def create():
    print(request.form)
    print('name',request.form['name'])
    print('dojo',request.form['dojo'])
    print('favorite_language',request.form['favorite_language'])
    print('comments',request.form['comments'])
    return render_template("dojo_survey_created.html")
@app.route('/danger')
def danger():
    render_template("dojo_survey_danger.html")
    return ,redirect('/')
# def danger():
#     print('User tried to visit /danger')
#     return redirect('/')
if __name__=="__main__":
    app.run(debug=True)