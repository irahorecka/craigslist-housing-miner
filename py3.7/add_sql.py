import csv
import os.path

from flask import Flask, render_template, request
from models import *
base_dir = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    f = open(f'{base_dir}/Data/test.csv')
    reader = csv.reader(f)
    for cl_state, cl_region, cl_district, housing_category,	post_id, repost_id,	title, url, date_posted, time_posted, price, location, has_image, has_geotag, bedrooms, area in reader:
        craigslist = Post(cl_state=cl_state, cl_region=cl_region, cl_district=cl_district, housing_category=housing_category, post_id=post_id, repost_id=repost_id,	title=title, url=url, date_posted=date_posted, time_posted=time_posted, price=price, location=location, has_image=has_image, has_geotag=has_geotag, bedrooms=bedrooms, area=area)
        db.session.add(craigslist)
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        main()
