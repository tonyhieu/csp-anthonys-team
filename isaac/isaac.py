from flask import Blueprint, render_template, request, json
import requests

isaac_bp = Blueprint('isaac', __name__,
                       url_prefix='/isaac',
                       template_folder='templates',
                       static_folder='static', static_url_path='static/isaac')

@isaac_bp.route("/")
def isaac_index():

    url = "https://na1.api.riotgames.com/lol/platform/v3/champion-rotations"

    headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
                "Accept-Language": "en-US,en;q=0.9",
                "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",

                "Origin": "https://developer.riotgames.com",
                "X-Riot-Token": "RGAPI-b6d7f5aa-a41c-44e8-a47e-e772e9506d16"
            }

    response = requests.request("GET", url, headers=headers)

    print(response.text)
    output = json.loads(response.text)
    return render_template("isaacIndex.html", lol=output)

