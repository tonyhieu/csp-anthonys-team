from flask import Blueprint, render_template, request

ethan_bp = Blueprint('ethan', __name__,
                       url_prefix='/ethan',
                       template_folder='templates',
                       static_folder='static', static_url_path='static/ethan')

@ethan_bp.route("/")
def ethan_index():
    return render_template("ethanIndex.html")
