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

# user history of matches table
#command = "create table IF NOT EXISTS history (user TEXT, 

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
    if request.method == 'GET':
        return render_template('login.html', login="Please login!")
    username = request.form['username']
    password = request.form['password']

    c.execute("SELECT * FROM login;")
    user_logins = c.fetchall()

    for user in user_logins:
        if username == user[0] and password == user[1]:
            session['username'] = username
            loc = ""
            dat = ""
            tim = ""
            img = ""
            names = ""
            player1 = player_stats()
            player2 = player_stats()
            full_item = get_item()
            reaction = yes_no()
            print(reaction[0])
            calculator = calculate_love(player1[0], player2[0], reaction[0])
            if calculator >= 75:
                outing = sunset_sunrise()
                names = str(player1[0]) + " and " + str(player1[2]) + " will have their first date!"
                loc = "Location: Central Park"
                dat = "Date: " + str(outing[0])
                tim = "Time: " + str(outing[1])
                img = outing[2]
            else:
                names = "Sadly, there will be no first date between " + str(player1[0]) + " and " + str(player2[0]) + ". Better luck next time."
                loc = ""
                dat = ""
                tim = ""
                img = "data:image/jpeg;base64,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"
            return render_template('home.html', status="Successfully logged in!", name_date=names, name1=player1[0], position=player1[1], teamname=player1[2], avg_games_played=player1[3], name2=player2[0], position2=player2[1], teamname2=player2[2], avg_games_played2=player2[3], item_name=full_item[0], item_price=full_item[1], item_description=full_item[2], item_link=full_item[3], answer=reaction[0], answer_link=reaction[1], percentage=calculator, location=loc, date=dat, time=tim, img_date=img)
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
        if len(newUser) < 8 or len(newPass) < 8 :
            return render_template('createaccount.html', status="Username and Password must be at least 8 characters long!")
        if newUser == user[0]:
            return render_template('createaccount.html', status="Submitted username is already in use.")

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
