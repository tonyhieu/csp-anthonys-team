from flask import Blueprint, render_template, request

samuel_bp = Blueprint('samuel', __name__,
                       url_prefix='/samuel',
                       template_folder='templates',
                       static_folder='static', static_url_path='static/samuel')

@samuel_bp.route("/")
def samuel_index():
    return render_template("samuelIndex.html")