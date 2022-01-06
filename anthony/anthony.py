from flask import Blueprint, render_template, request
import requests
from riotwatcher import LolWatcher, TftWatcher

anthony_bp = Blueprint('anthony', __name__,
                   url_prefix='/anthony',
                   template_folder='templates',
                   static_folder='static', static_url_path='static/anthony')

@anthony_bp.route("/", methods=['GET','POST'])
def anthony_index():
    user_dicts = [{'username':'R04'}, {'username':'ShintaroKisaragi'}, {'username':'so phan bi xoan'}]
    if request.form:
        id = request.form.get("accountId")
        if len(id) != 0:
            user_dicts.append({'username':id})

    api_key = 'RGAPI-e76dd7e1-4e8c-42b2-9e68-f3c71cfd03c3'
    # RGAPI-2fbc42f9-e279-44ba-8f3f-fa878f3d9600
    watcher = LolWatcher(api_key, 5)
    tft_watcher = TftWatcher(api_key, 5)
    my_region = 'na1'

    for user in user_dicts:
        try:
            summoner = watcher.summoner.by_name(my_region, user['username'])

            user['lol_stats'] = watcher.league.by_summoner(my_region, summoner['id'])
            user['tft_stats'] = tft_watcher.league.by_summoner(my_region, summoner['id'])
        except:
            user['lol_stats'] = [{'queueType': 'N/A', 'rank':'N/A', 'tier': '', 'leaguePoints': 'N/A', 'wins': 0, 'losses': 1}]
            user['tft_stats'] = []

    mode_dict = {'RANKED_TFT_PAIRS': 'TFT Double Up', 'RANKED_SOLO_5x5':'Ranked Solo/Duo', 'RANKED_FLEX_SR': 'Ranked Flex', 'RANKED_TFT':'Ranked TFT', 'N/A':"Data not found"}

    return render_template("anthonyIndex.html", users=user_dicts, mode_dict=mode_dict)
