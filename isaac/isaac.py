from flask import Blueprint, render_template, request

isaac_bp = Blueprint('isaac', __name__,
                       url_prefix='/isaac',
                       template_folder='templates',
                       static_folder='static', static_url_path='static/isaac')

@isaac_bp.route("/")
def isaac_index():
    return render_template("isaacIndex.html")