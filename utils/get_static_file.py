import json
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))


def search_filters():
    """Get and load search filters JSON."""
    search_filters_path = os.path.join(BASE_DIR, "static", "search_filters.json")
    with open(search_filters_path) as json_path:
        return json.load(json_path)["search_filters"]


def housing_categories():
    """Get and load housing categories JSON."""
    housing_categories_path = os.path.join(
        BASE_DIR, "static", "housing_categories.json"
    )
    with open(housing_categories_path) as json_path:
        return json.load(json_path)["housing_categories"]


def craigslist_regions():
    """Get and load Craigslist region JSON."""
    craigslist_regions_path = os.path.join(
        BASE_DIR, "static", "craigslist_regions.json"
    )
    with open(craigslist_regions_path) as json_path:
        craigslist_regions = json.load(json_path)
    return craigslist_regions

    # tidy_craigslist_regions = {}
    # for country, regions in craigslist_regions.items():
    #     tidy_craigslist_regions[country] = [tuple(region) for region in regions]
    # return tidy_craigslist_regions


if __name__ == "__main__":
    print(housing_categories())
    print(craigslist_regions())
    print(search_filters())
