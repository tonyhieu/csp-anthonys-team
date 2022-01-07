from flask import Blueprint, render_template, request, json
import requests

samuel_bp = Blueprint('samuel', __name__,
                     url_prefix='/samuel',
                     template_folder='templates',
                     static_folder='static', static_url_path='static/samuel')

@samuel_bp.route("/")
def samuel_index():

    url = "https://numbersapi.p.rapidapi.com/6/21/date"

    querystring = {"fragment":"true","json":"true"}

    headers = {
        'x-rapidapi-host': "numbersapi.p.rapidapi.com",
        'x-rapidapi-key': "befd3aa94cmsh6c15f9448db64f3p194824jsn7727f7079e12"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    output = json.loads(response.text)
    return render_template("samuelIndex.html",questions=output)
