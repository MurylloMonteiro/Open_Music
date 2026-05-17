from flask import render_template


def Home():
    return render_template("index.html")