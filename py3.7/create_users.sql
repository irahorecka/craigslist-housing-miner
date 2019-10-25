-- to create a table called flights in SQL
-- you must clearly define all datatypes that will be present in your column values, as written below
CREATE TABLE users (
    id SERIAL PRIMARY KEY, -- id is of type serial - primary key means each id will be unique
    name VARCHAR NOT NULL, -- varchar with values that are not null (which means there MUST be data here - it cannot be empty)
    post_id INTEGER NOT NULL -- not null also forces the data to have information for these fields, which is mandatory
);

-- incorporate into psql database by typing the following:
-- $ psql -d craigslist -a -f create_users.sql