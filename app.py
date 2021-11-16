from flask import Flask, render_template


app = Flask("app")

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

@app.route("/")
def index():
    return render_template("index.html")

app.run(host="127.0.0.1", port=8080)