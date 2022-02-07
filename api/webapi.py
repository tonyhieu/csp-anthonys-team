from flask import Blueprint, jsonify, render_template

api_bp = Blueprint('api', __name__,
                   url_prefix='/api',
                   template_folder='templates',
                   static_folder='static', static_url_path='static/api')



# GAMES API
games = []
game_embeds = [
    "<iframe src='https://scratch.mit.edu/projects/199615756/embed' allowtransparency='true' width='700' height='700' frameborder='0' scrolling='no' allowfullscreen></iframe>", 
    "/api/games/embeds/2", 
    "/api/games/embeds/3", 
    "/api/games/embeds/4",
    "/api/games/embeds/5"
]
game_titles = [
    "Dabbing Tycoon", 
    "Snake", 
    "Conway's Game of Life", 
    "Pixel Art",
    "Amidakuji"
]
game_authors = [
    "Anthony Vo", 
    "John Mortensen", 
    "Nathaniel Cherian", 
    "Anthony Vo",
    "Anthony Vo"
]

def _init_games ():
    for i in range(len(game_embeds)):
        games.append({"id": i+1, "title": game_titles[i], "embed": game_embeds[i], "author": game_authors[i], "likes": 0, "dislikes": 0})

@api_bp.route('/games')
def get_games():
    if len(games) == 0:
        _init_games()
    return jsonify(games)

@api_bp.route('/games/<id>')
def get_game(id):
    if len(games) == 0:
        _init_games()
    try:
        return jsonify(games[int(id)-1])
    except:
        return "Invalid ID"

@api_bp.route('/games/embeds/<id>')
def embed(id):
    return render_template(str(id) + ".html")
# make it so that we can check whether the embed is actually in the database or if its in an html file, use that to determine how to load webpage

# INTERESTS API
anthony_interests = ["programming", "League of Legends", "golf", "VOCALOID", "rhythm games", "game development", "web development"]
ethan_interests = ["Running Track", "Video Games", "Wakeboarding", "Lofi", "Climbing/Hiking", "Attempting to learn violin"]
isaac_interests = ["Soccer", "Selling my soul to Riot Games", "Playing games", "Hanging out with friends", "Engineering"]
erik_interests = ["Memes", "Video games", "Karate", "Engineering", "Driving"]
samuel_interests = ["soccer", "games"]

@api_bp.route("/anthony")
def get_anthony_interests():
    return jsonify(anthony_interests)

@api_bp.route("/ethan")
def get_ethan_interests():
    return jsonify(ethan_interests)

@api_bp.route("/isaac")
def get_isaac_interests():
    return jsonify(isaac_interests)

@api_bp.route("/erik")
def get_erik_interests():
    return jsonify(erik_interests)

@api_bp.route("/samuel")
def get_samuel_interests():
    return jsonify(samuel_interests)