from flask import Blueprint, render_template, request, json
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

create_task_bp = Blueprint('create_task_home', __name__,
                       url_prefix='/create-task',
                       template_folder='templates',
                       static_folder='static', static_url_path='static')

@create_task_bp.route("/")
def index():
    return render_template("create_task_home.html")

@create_task_bp.route("/anthony")
def anthony():
    return render_template("anthony.html")

@create_task_bp.route("/matthew")
def matthew():
    return render_template("matthew.html")

@create_task_bp.route("/chris")
def chris():
    return render_template("chris.html")

@create_task_bp.route("/tigran")
def tigran():
    return render_template("tigran.html")

@create_task_bp.route("/derek")
def derek():
    return render_template("derek.html")

@create_task_bp.route("/erik")
def erik():
    return render_template("erik.html")

@create_task_bp.route("/spotifyfinder")
def spotifyfinder():
    if request.form:
        tracks_dicts = [{'name':'Heat Waves'}]
        artist_dicts = [{'name':'Glass Animals'}]
        artist_id = request.form.get("artist_id")
        if len(artist_id) != 0:
            tracks_dicts.append({'artist':artist_id})


    cid = '8178d9fc45274bb5b0ebef69552934bb'
    secret = '54e37228eeb94540915939462917d92f'
    AUTH_URL = 'https://accounts.spotify.com/api/token'

    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': cid,
        'client_secret': secret,
    })
    auth_response_data = auth_response.json()
    access_token = auth_response_data['access_token']

    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }
    url = 'https://api.spotify.com/v1/artists'

    track_id = '6y0igZArWVi6Iz0rj35c1Y'
    r = requests.get(url + 'artists/' + track_id, headers=headers)
    r = r.json()
    r


    r = requests.get(url + 'artists/' + artist_id + '/top-tracks',
                     headers=headers,
                     params={'include_groups': 'toptracks', 'limit': 5})
    d = r.json()

    data = []
    tracks = []

    for toptracks in d['items']:
        print(toptracks['name'], ' --- ', toptracks['release_date'])


    for toptracks in d['items']:
        toptracks_name = toptracks['name']
        trim_name = toptracks_name.split(('(') [0].strip)()
        if trim_name.upper() in tracks or int(toptracks['release_date'][:4]) > 2000:
            continue
        tracks.append(trim_name.upper())
        print(toptracks_name)
        r = requests.get(url + 'artists/' + artist_id + '/top-tracks',
            headers=headers)
        tracks = r.json()['items']

    r.update({
        'track_name' : tracks['name'],
        'release_date' : toptracks['release_date'],
        'track_id': toptracks['id']
    })

    return render_template('spotifyfinder.html')


@create_task_bp.route("/erik_ethan")
def erik_ethan():
    return render_template("erik_ethan.html")

@create_task_bp.route("/SamuelIsaac")
def SamuelIsaac():
    return render_template("Samuel_Isaac.html")