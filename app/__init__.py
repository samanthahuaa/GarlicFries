import sqlite3
from refresh import *
from api_calls import *
# from user_db import *
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

@app.route('/home', methods=['GET', 'POST'])
def authenticate():
    username = request.form['username']
    password = request.form['password']

    c.execute("SELECT * FROM login;")
    user_logins = c.fetchall()

    for user in user_logins:
        if username == user[0] and password == user[1]:
            session['username'] = username
            player1 = player_stats()
            player2 = player_stats()
            full_item = get_item()
            reaction = yes_no()
            calculator = calculate_love(player1[0], player2[0], reaction[0])
            outing = sunset_sunrise()
            return render_template('home.html', status="Successfully logged in!", name1=player1[0], position=player1[1], teamname=player1[2], avg_games_played=player1[3], name2=player2[0], position2=player2[1], teamname2=player2[2], avg_games_played2=player2[3], item_name=full_item[0], item_price=full_item[1], item_description=full_item[2], item_link=full_item[3], answer=reaction[0], answer_link=reaction[1], percentage=calculator[0], date=outing[0], time=outing[1])
        if username == user[0] and password != user[1]:
            return render_template('login.html', login="Invalid Password!")

    return render_template('login.html', login="Submitted username is not registered!")

########################### LOGGING IN SYSTEM ###########################
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
