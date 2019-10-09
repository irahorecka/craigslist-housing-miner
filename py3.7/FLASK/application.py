from flask import Flask, render_template, request
from models import *
from webscrape import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.route("/")
def index():
    craigslist = Post.query.filter(Post.cl_district=='greenbay').order_by(Post.date_posted.desc()).limit(50)
    return render_template("index.html", craigslist=craigslist)


@app.route("/book", methods=["POST"])
def book():
    """Jot a name."""

    # Get form information.
    name = request.form.get("name")
    try:
        post_id = int(request.form.get("post_id"))
    except ValueError:
        return render_template("error.html", message="Invalid post number.")

    # Make sure the flight exists.
    post = Post.query.get(post_id)
    if not post:
        return render_template("error.html", message="No such post with that id.")

    # Add passenger.
    post.add_candidate(name)
    return render_template("success.html")


@app.route("/posts")
def posts():
    """List all posts."""
    posts = Post.query.filter(Post.cl_district=='greenbay').order_by(Post.date_posted.desc()).limit(50)
    return render_template("flights.html", posts=posts)

@app.route("/posts/<int:post_id>")
def post(post_id):
    """List details about a single post."""

    # Make sure flight exists.
    post = Post.query.get(post_id)
    if post is None:
        return render_template("error.html", message="No such post.")

    # Get all passengers.
    passengers = Users.query.filter_by(post_id=post_id).all()
    return render_template("flight.html", post=post, passengers=passengers, test=return_body(post.url))