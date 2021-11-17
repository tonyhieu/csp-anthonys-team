from flask import Flask, render_template, request
import requests
from api.webapi import api_bp


app = Flask("app")

@app.route("/")
def index():
    return render_template("index.html")

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

@app.route("/games")
def games():
    url = "http://127.0.0.1:5000/api/games"
    response = requests.request("GET", url)
    print(response)
    return render_template("games.html", games=response.json())

@app.route("/game/<id>")
def game(id):
    url = "http://127.0.0.1:5000/api/games/" + id
    response = requests.request("GET", url)
    try:
        game_data = response.json()
        return render_template("game.html", game_data=game_data)
    except:
        return "Invalid ID"

@app.route("/about")
def about():
    anthony_response = requests.request("GET", "http://127.0.0.1:5000/api/anthony")
    return render_template("about.html", anthony=anthony_response.json())

app.register_blueprint(api_bp)

app.run(host="127.0.0.1", port=5000)