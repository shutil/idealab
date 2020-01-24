from server import app
from flask import render_template, request
from routes.db import insert
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/post_idea",methods=["POST"])
def ideas():
    if request.method == "POST":
        pl = request.form['programing_laungage']
        idea = request.form['idea']
        by = request.form['by']

        pl_secure = pl.replace("<","&lt;").replace(">","&gt")
        idea_secure = idea.replace("<","&lt;").replace(">","&gt")
        by_secure = by.replace("<","&lt;").replace(">","&gt")
        
        progress = insert(pl_secure,idea_secure,by_secure)
        return progress