from flask import Blueprint, render_template, request

create_task_bp = Blueprint('create_task', __name__,
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

@create_task_bp.route("/SamuelIsaac")
def SamuelIsaac():
    return render_template("Samuel_Isaac.html")