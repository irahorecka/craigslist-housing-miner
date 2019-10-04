import os.path
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import csv

base_dir = os.path.dirname(os.path.abspath(__file__))

#create engine for craigslist database \c craigslist in psql to nav there
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    os.chdir(f'{base_dir}/Data/2019-10-03/')
    for filename in os.listdir():
        f = open(filename, encoding='utf8', errors = 'ignore')
        reader=csv.reader(x.replace('\0', '') for x in f)
        try:
            for cl_state, cl_region, cl_district, housing_category, post_id, repost_id, title, url, date_posted, time_posted, price, location, has_image, has_geotag, bedrooms, area in reader:                
                db.execute("INSERT INTO craigslist (cl_state, cl_region, cl_district, housing_category, post_id, repost_id, title, url, date_posted, time_posted, price, location, has_image, has_geotag, bedrooms, area) VALUES (:cl_state, :cl_region, :cl_district, :housing_category, :post_id, :repost_id,	:title, :url, :date_posted, :time_posted, :price, :location, :has_image, :has_geotag, :bedrooms, :area)",
                    {'cl_state':cl_state, 'cl_region':cl_region, 'cl_district':cl_district, 'housing_category':housing_category, 'post_id':post_id, 'repost_id':repost_id, 'title':title, 'url':url, 'date_posted':date_posted, 'time_posted':time_posted, 'price':price, 'location':location, 'has_image':has_image, 'has_geotag':has_geotag, 'bedrooms':bedrooms, 'area':area})
        except ValueError: #to avoid ValueError for unpacking error
            print('error')   
        db.commit()

if __name__ == '__main__':
    main()



