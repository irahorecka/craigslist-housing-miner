from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Post(db.Model):
    __tablename__ = "craigslist"
    id = db.Column(db.Integer, primary_key=True)
    cl_state = db.Column(db.String, nullable=False)
    cl_region = db.Column(db.String, nullable=False)
    cl_district = db.Column(db.String, nullable=False)
    housing_category = db.Column(db.String, nullable=False)
    post_id = db.Column(db.String, nullable=False)
    repost_id = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)
    date_posted = db.Column(db.Date, nullable=False)
    time_posted = db.Column(db.Time, nullable=False)
    price = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    has_image = db.Column(db.String, nullable=False)
    has_geotag = db.Column(db.String, nullable=False)
    bedrooms = db.Column(db.String, nullable=False)
    area = db.Column(db.String, nullable=False)
