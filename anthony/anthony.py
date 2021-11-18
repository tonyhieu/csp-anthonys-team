from flask import Blueprint, render_template, request

anthony_bp = Blueprint('anthony', __name__,
                   url_prefix='/anthony',
                   template_folder='templates',
                   static_folder='static', static_url_path='static/anthony')

@anthony_bp.route("/")
def anthony_index():
    return render_template("anthonyIndex.html")
