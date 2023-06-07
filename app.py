from flask import Flask, render_template, request, session, redirect, flash, url_for, abort

app = Flask(__name__)


@app.route("/")
@app.route("/home")
@app.route("/index.html")
def home():
    return render_template("index.html")

@app.route("/events")
def events():
    return render_template("events.html")
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/sched")
def sched():
    return render_template("sched.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/findus")
def findus():
    return render_template("findus.html")


if __name__ == "__main__":
    # app.run()
    app.run('0.0.0.0')
