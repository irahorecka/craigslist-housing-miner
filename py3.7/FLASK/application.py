from flask import Flask, render_template, request, jsonify
from models import *
from geomap import *
from webscrape import *
from sqlalchemy import func
import random

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
    print(district)
    if district == '':
        zoom = 5  
    elif 'district' in district.lower():
        print('true')
        zoom = 14
    else:
        zoom = 11 
    lng,lat = GeoMap(str(app), district, state).get_geotag() if district!= '' else GeoMap(str(app), state, 'United States').get_geotag()
    if district != '':
        craigslist = Post.query.filter(func.lower(Post.cl_state)==func.lower(state)).filter(func.lower(Post.location).like("%"+func.lower(district)+"%")).order_by(Post.date_posted.desc()).limit(50)
    else:
        craigslist = Post.query.filter(func.lower(Post.cl_state)==func.lower(state)).order_by(Post.date_posted.desc()).limit(50)
    """Jot a name."""

    # Get form information.
    name = request.form.get("name")
    return render_template("initial.html", craigslist=craigslist, district=district, state=state, name=name, lng=lng, lat=lat, map_zoom=zoom)

@app.route("/post", methods=["POST"])
def post():
    var = (request.form.get("post_id").split('**'))
    print(var, type(var))
    try:
        post_id = int(var[0])
    except ValueError:
        return render_template("error.html", message="Invalid post number.")

    # Make sure the flight exists.
    post = Post.query.get(post_id)
    if not post:
        return render_template("error.html", message="No such post with that id.")

    # Add passenger.
    passengers = Users.query.filter_by(post_id=post_id).all()
    rand_int = random.randint(0,100000000000)
    return render_template("flight.html", post = post, name = var[1], passengers = passengers, content = return_body(post.url), rand = rand_int, state = var[2], district = var[3])


@app.route("/posts", methods=["POST"])
def posts():
    var = (request.form.get("name").split('**'))
    print(var)
    try:
        post_id = int(var[0])
    except ValueError:
        return render_template("error.html", message="Invalid post number.")

    # Make sure the flight exists.
    post = Post.query.get(post_id)
    if not post:
        return render_template("error.html", message="No such post with that id.")

    # Add passenger.
    post.add_candidate(var[1].title()) #name
    return render_template('success.html', name = var[1], state = var[2], district = var[3])
    #return render_template("flight.html", post = post, name = var[1], passengers = passengers, test=return_body(post.url))













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