import sqlite3

from flask import Flask, redirect, render_template, request, session, url_for

# sqlite

DB_FILE = "tables.db"
db = sqlite3.connect(DB_FILE, check_same_thread=False)
c = db.cursor()

# user login table
command = "create table IF NOT EXISTS login (user TEXT, password TEXT)"
c.execute(command)
db.commit()

# flask
app = Flask(__name__)
app.secret_key = 'a\8$x5T!H2P7f\m/rwd[&'

@app.route("/")
def index():
    if 'username' in session:
        return render_template('home.html', status="Successfully logged in!")
    else:
        return render_template('login.html')

@app.route('/auth', methods=['GET', 'POST'])
def authenticate():
    username = request.form['username']
    password = request.form['password']

    c.execute("SELECT * FROM login;")
    user_logins = c.fetchall()

    for user in user_logins:
        if username == user[0] and password == user[1]:
            session['username'] = username
            return render_template('home.html', status="Successfully logged in!")
        if username == user[0] and password != user[1]:
            return render_template('login.html', login="Invalid Password!")

    return render_template('login.html', login="Submitted username is not registered!")

@app.route("/register")
def register():
    return render_template('createaccount.html')

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    newUser = request.form['username']
    newPass = request.form['password']

    c.execute("SELECT * FROM login;")
    user_logins = c.fetchall()

    for user in user_logins:
        if newUser == user[0]:
            return render_template('createaccount.html', status = "Submitted username is already in use.")

    c.execute("INSERT INTO login VALUES (?,?);", (newUser, newPass))
    db.commit()
    return render_template('login.html', login="New user has been created successfully! Log in with your new credentials!")


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.debug = True
    app.run()
