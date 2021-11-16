from flask import Blueprint, jsonify

api_bp = Blueprint('api', __name__,
                   url_prefix='/api',
                   template_folder='templates',
                   static_folder='static', static_url_path='static/api')

games = []
game_embeds = [
    '<iframe src="https://scratch.mit.edu/projects/199615756/embed" allowtransparency="true" width="485" height="402" frameborder="0" scrolling="no" allowfullscreen></iframe>'
]
game_titles = [
    "Dabbing Tycoon"
]
game_authors = [
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