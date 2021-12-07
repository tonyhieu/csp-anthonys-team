from flask import Blueprint, render_template, request
import requests

anthony_bp = Blueprint('anthony', __name__,
                   url_prefix='/anthony',
                   template_folder='templates',
                   static_folder='static', static_url_path='static/anthony')

@anthony_bp.route("/")
def anthony_index():
    url = "https://the-cocktail-db.p.rapidapi.com/random.php"

    headers = {
        'x-rapidapi-host': "the-cocktail-db.p.rapidapi.com",
        'x-rapidapi-key': "f34f39d457msh80116afa9392991p16f534jsn6a54d17a536d"
        }

    response = requests.request("GET", url, headers=headers)


    print(response.json())

    return render_template("anthonyIndex.html")
