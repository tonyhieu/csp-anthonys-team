from flask import Flask, render_template, request
import requests
from __init__ import app

from api.webapi import api_bp
from anthony.anthony import anthony_bp
from erik.erik import erik_bp
from isaac.isaac import isaac_bp
from samuel.samuel import samuel_bp
from ethan.ethan import ethan_bp

@app.route("/")
def index():
    return render_template("index.html")

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

@app.route("/games")
def games():
    url = "http://127.0.0.1:6969/api/games"
    response = requests.request("GET", url)
    print(response)
    return render_template("games.html", games=response.json())

@app.route("/game/<id>")
def game(id):
    url = "http://127.0.0.1:6969/api/games/" + id
    response = requests.request("GET", url)
    try:
        game_data = response.json()
        return render_template("game.html", game_data=game_data)
    except:
        return "Invalid ID"

@app.route("/about")
def about():
    anthony_response = requests.request("GET", "http://127.0.0.1:6969/api/anthony")
    isaac_response = requests.request("GET", "http://127.0.0.1:6969/api/isaac")
    ethan_response = requests.request("GET", "http://127.0.0.1:6969/api/ethan")
    erik_response = requests.request("GET", "http://127.0.0.1:6969/api/erik")
    samuel_response = requests.request("GET", "http://127.0.0.1:6969/api/samuel")
    return render_template("about.html", anthony=anthony_response.json(), isaac=isaac_response.json(), ethan=ethan_response.json(), erik=erik_response.json(), samuel=samuel_response.json())


app.register_blueprint(api_bp)
app.register_blueprint(anthony_bp)
app.register_blueprint(erik_bp)
app.register_blueprint(samuel_bp)
app.register_blueprint(ethan_bp)
app.register_blueprint(isaac_bp)

app.run(host="127.0.0.1", port=6969)