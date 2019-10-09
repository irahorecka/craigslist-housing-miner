from flask import Flask, render_template, request
from models import *
from webscrape import *
from sqlalchemy import func

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.route("/")
def index():
    return render_template("index.html", states = States().state_keys)

@app.route("/initial", methods=['POST'])
def initial():
    state = request.form.get('state_id')
    district = request.form.get("district_id")
    craigslist = Post.query.filter(func.lower(Post.cl_state)==func.lower(state)).filter(func.lower(Post.location).like("%"+func.lower(district)+"%")).order_by(Post.date_posted.desc()).limit(50)
    return render_template("initial.html", craigslist = craigslist)

@app.route("/post", methods=["POST"])
def post():
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
    passengers = Users.query.filter_by(post_id=post_id).all()
    return render_template("flight.html", post = post, passengers = passengers, test=return_body(post.url))


'''@app.route("/posts")
def posts(district):
    """List all posts."""
    posts = Post.query.filter(Post.cl_district==district.title()).order_by(Post.date_posted.desc()).limit(50)
    return render_template("flights.html", posts=posts)'''

'''@app.route("/posts/<int:post_id>")
def post(post_id):
    """List details about a single post."""

    # Make sure flight exists.
    post = Post.query.get(post_id)
    if post is None:
        return render_template("error.html", message="No such post.")

    # Get all passengers.
    passengers = Users.query.filter_by(post_id=post_id).all()
    return render_template("flight.html", post=post, passengers=passengers, test=return_body(post.url))'''