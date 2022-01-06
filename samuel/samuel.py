from flask import Blueprint, render_template, request
import requests
import json
samuel_bp = Blueprint('samuel', __name__,
                       url_prefix='/samuel',
                       template_folder='templates',
                       static_folder='static', static_url_path='static/samuel')

@samuel_bp.route("/")
def samuel_index():
    url = "https://football-prediction-api.p.rapidapi.com/api/v2/predictions"

    querystring = {"market":"classic","iso_date":"2018-12-01","federation":"UEFA"}

    headers = {
    'x-rapidapi-host': "football-prediction-api.p.rapidapi.com",
    'x-rapidapi-key': "befd3aa94cmsh6c15f9448db64f3p194824jsn7727f7079e12"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    output = json.loads(response.text)
    return render_template("samuelIndex.html", questions=output)


