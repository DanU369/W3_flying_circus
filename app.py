from flask import Flask, request, redirect, render_template, url_for,session, escape

import data


app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
def index():
    if 'username' in session:
        username=session['username']
        return render_template("loged_in.html",username=username)
    return render_template("not_loged_in.html")

@app.route("/login" , methods=["GET","POST"])
def login():
    if request.method=="POST":
        username=request.form.get('username')
        password=request.form.get('password')
        users=data.users
        for user in users:
            if username in user:
                hashed_password=user[username]
                if data.verify_password(password, hashed_password):
                    session['username'] = username
                    return redirect("/")
                else:
                    return render_template("login.html", users=data.users, err="err")
        else:
            return render_template("login.html", users=data.users,err="err")
    return render_template("login.html",users=data.users,err=0)

@app.route("/test",methods=["GET","POST"])
def test():
    if 'username' not in session:
        return redirect("/login")
    questions = data.questions
    number_of_question=len(questions)
    if request.method=='GET':
        session['corect_answers']=0
        session['question_nr']=0
    if request.method=='POST':
        answer=request.form.get('answer')
        if answer == 'True':
            session['corect_answers']+=1
        session['question_nr']+=1
    if session['question_nr'] ==len(questions):
        return redirect("/result")
    question = list(questions.keys())[session['question_nr']]
    return render_template("test.html",questions=questions,question=question,number_of_question=number_of_question)


@app.route("/result")
def result():
    if 'username' not in session:
        return redirect("/login")
    questions = data.questions
    number_of_question = len(questions)
    return render_template("result.html", number_of_question=number_of_question)


@app.route("/logout")
def logout():
    if 'username' not in session:
        return redirect("/login")
    session.pop('username')
    session.pop('corect_answers', None)
    session.pop('question_nr', None)
    session.pop('username', None)
    return redirect("/")

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )

# from flask import Flask, session, redirect, url_for, escape, request, render_template
#
# app = Flask(__name__)
#
# # Set the secret key to some random bytes. Keep this really secret!
# app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
#
# @app.route('/')
# def index():
#     if 'username' in session:
#         return 'Logged in as %s' % escape(session['username'])
#     return 'You are not logged in'
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         session['username'] = request.form['username']
#         return redirect(url_for('index'))
#     return render_template('test.html')
#
# @app.route('/logout')
# def logout():
#     # remove the username from the session if it's there
#     session.pop('username', None)
#     return redirect(url_for('index'))
