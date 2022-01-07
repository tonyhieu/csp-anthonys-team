from flask import Flask, render_template, request, redirect, url_for, session
import requests
from __init__ import app
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

from db import Games

from api.webapi import api_bp
from anthony.anthony import anthony_bp
from erik.erik import erik_bp
from isaac.isaac import isaac_bp
from samuel.samuel import samuel_bp
from ethan.ethan import ethan_bp

at_school = True     # CHANGE THIS VARIABLE DEPENDING IF YOURE AT SCHOOL OR AT HOME, SHOULD BE SET TO FALSE ON GITHUB
domain = ""

if at_school:
    domain = "http://127.0.0.1:6969"
else:
    domain = "https://www.anthonysharem.cf"

#Login System Code
app = Flask('login')
app.secret_key= 'joebidenshusband'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'pythonlogin'

mysql = MySQL(app)

@app.route('/csp-anthonys-harem/', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and ' username' in request.form and 'password in request.form':
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connecction.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accoutns WHERE usernmane = %s AND password = %s', (username, password,))
        account = cursor.fetchone()
    if account:
        session['loggedin'] = True
        session['id'] = account['id']
        session['username'] = account['username']
        return 'Log in successful!'
    else:
        msg = 'Incorrect username or password.'
    return render_template ('login.html', msg='')

#Logout system
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))

#Register system
@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out all areas!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s)', (username, password, email,))
            mysql.connection.commit()
            msg = 'Thank you for Registering!'
    elif request.method == 'POST':
        msg = 'Please fill out all areas!'
    return render_template('register.html', msg=msg)




@app.route("/")
def index():
    return render_template("index.html")

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html", error_message="Oops! We hit a roadblock. Try accessing this page later.")

@app.route("/games")
def games():
    url = "https://" + domain + "/api/games"
    response = requests.request("GET", url)
    print(response)
    return render_template("games.html", games=response.json())

@app.route("/game/<id>")
def game(id):
    url = "https://" + domain + "/api/games/" + id
    response = requests.request("GET", url)
    try:
        game_data = response.json()
        return render_template("game.html", game_data=game_data)
    except:
        return "Invalid ID"

@app.route("/about")
def about():
    anthony_response = requests.request("GET", domain + "/api/anthony")
    isaac_response = requests.request("GET", domain + "/api/isaac")
    ethan_response = requests.request("GET", domain + "/api/ethan")
    erik_response = requests.request("GET", domain + "/api/erik")
    samuel_response = requests.request("GET", domain + "/api/samuel")
    return render_template("about.html", anthony=anthony_response.json(), isaac=isaac_response.json(), ethan=ethan_response.json(), erik=erik_response.json(), samuel=samuel_response.json())


def get_all_games_json():
    return [game.read() for game in Games.query.all()]


@app.route("/games_database", methods=["GET", "POST"])
def games_database():
    if request.method != "POST":  # i just learned about guard clauses so of course i'll use one here
        return render_template("database.html", games=get_all_games_json())

    new_game = Games(title=request.form['title'], author=request.form['author'], embed=request.form['embed'])
    try:
        new_game.create()
    except:
        return render_template("404.html", error_message="Something went wrong with adding your game.")
    return redirect('/games_database')


@app.route("/delete/<id>", methods=["GET", "POST"])
def delete(id):
    game = Games.query.filter_by(gameID=id).first()
    if game is not None:
        game.delete()
    return redirect("/games_database")

@app.route("/update/<id>", methods=["GET", "POST"])
def update(id):
    game = Games.query.filter_by(gameID=id).first()
    if request.method != "POST":
        return render_template("update_database.html", game=game, id=id)

    new_title = game.title
    new_author = game.author
    new_embed = game.embed

    if request.form["title"] is not None:
        new_title = request.form["title"]
    if request.form["author"] is not None:
        new_author = request.form["author"]
    if request.form["embed"] is not None:
        new_embed = request.form["embed"]

    try:
        game.update(title=new_title, author=new_author, embed=new_embed)
    except:
        return render_template("404.html", error_message="Something went wrong with updating your game.")

    return redirect("/games_database")


app.register_blueprint(api_bp)
app.register_blueprint(anthony_bp)
app.register_blueprint(erik_bp)
app.register_blueprint(samuel_bp)
app.register_blueprint(ethan_bp)
app.register_blueprint(isaac_bp)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=6969)

