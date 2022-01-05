from flask import Blueprint, render_template, request

erik_bp = Blueprint('erik', __name__,
                       url_prefix='/erik',
                       template_folder='templates',
                       static_folder='static', static_url_path='static/erik')
# test

@erik_bp.route("/")
def erik_index():
    return render_template("erikIndex.html")
