from flask import Flask, render_template

app = Flask(__name__)

projects = [
    {
        "name": "Minbaingu website built with Wordpress",
        "thumb": "img/minbaringu.png",
        "hero": "img/minbaringu.png",
        "categories": ["python", "web"],
        "slug": "habit-tracking",
        "prod": "https://udemy.com"
    },
    {
        "name": "Broken Universe Comics website built with Wordpress",
        "thumb": "img/broken-universe-comics.png",
        "hero": "img/broken-universe-comics.png",
        "categories": ["react", "javascript"],
        "slug": "personal-finance"
    },
    {
        "name": "Polton Inn Pub website built with Wordpress",
        "thumb": "img/polton-inn-pub.png",
        "hero": "img/polton-inn-pub.png",
        "categories": ["writing"],
        "slug": "api-docs"
    }
]


@app.route("/")
def home():
    return render_template("home.html", projects=projects)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

