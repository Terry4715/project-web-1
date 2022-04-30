from flask import Flask, render_template, abort

app = Flask(__name__)

projects = [
    {
        "name": "Minbaingu website built with Wordpress",
        "thumb": "img/minbaringu.png",
        "hero": "img/minbaringu.png",
        "categories": ["wordpress", "web"],
        "slug": "minbaringu",
        "prod": "https://www.minbaringu.com.au/"
    },
    {
        "name": "Broken Universe Comics website built with Wordpress",
        "thumb": "img/broken-universe-comics.png",
        "hero": "img/broken-universe-comics.png",
        "categories": ["wordpress", "web"],
        "slug": "broken-universe-comics",
        "prod": "https://brokenuniversecomics.com/"
    },
    {
        "name": "Polton Inn Pub website built with Wordpress",
        "thumb": "img/polton-inn-pub.png",
        "hero": "img/polton-inn-pub.png",
        "categories": ["wordpress", "web"],
        "slug": "polton-inn-pub",
        "prod": "https://poltonpub.co.uk/"
    }
]

slug_to_project = {project['slug']: project for project in projects}

@app.route("/")
def home():
    return render_template("home.html", projects=projects)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(f"project_{slug}.html", project=slug_to_project[slug])

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404