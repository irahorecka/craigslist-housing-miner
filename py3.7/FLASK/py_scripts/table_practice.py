import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():

    # List top 10 titles.
    posts = db.execute("SELECT id, title, price FROM craigslist").fetchmany(10)
    for post in posts:
        print(f"{post.id} and {post.title} and the price {post.price}")

    # Prompt user to choose a location.
    post_loc = (input("\nPost location: "))
    post_locs = db.execute("SELECT id, price, title, cl_region FROM craigslist WHERE cl_region = :reg AND bedrooms = '1'",
                        {"reg": post_loc}).fetchmany(10)
    # Make sure flight is valid.
    if post_locs is None:
        print("Error: No such post.")
        return
    else:
        for post in post_locs:
            print(f'{post.id}, {post.price}, {post.title}')

    '''# List passengers.
    passengers = db.execute("SELECT name FROM passengers WHERE flight_id = :flight_id",
                            {"flight_id": flight_id}).fetchall()
    print("\nPassengers:")
    for passenger in passengers:
        print(passenger.name)
    if len(passengers) == 0:
        print("No passengers.")'''

if __name__ == "__main__":
    main()
