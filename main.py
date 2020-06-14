import utils


def main(countries=[], geotagged=False):
    """Function to initialize scraping of Craigslist housing
    data. Uses static JSON files from /static dir and
    parallel + scraping functions from /utils dir."""

    all_locations = utils.craigslist_regions()
    specific_locations = []
    if countries:
        for country in countries:
            specific_locations.extend(all_locations.get(country.lower()))
    else:
        # search every country
        for country, _ in all_locations.items():
            specific_locations.extend(all_locations.get(country.lower()))

    for location in specific_locations:
        # append geotag bool to location list
        location.append(geotagged)

    specific_locations_tuple = tuple(tuple(location) for location in specific_locations)
    utils.map_processes(utils.scrape_housing, specific_locations_tuple)


if __name__ == "__main__":
    # simple demo for now - eventually accept user args and kwargs
    countries = input(
        "Input a list of appropriate countries.\nIf no list provided, a global search will be conducted: "
    )
    if countries:
        countries = eval(countries)
    geotagged = input(
        "Would you like to include geotags of your Craigslist posts [y/n]: "
    )
    geotagged = True if geotagged.lower() == "y" else False
    main(countries=countries, geotagged=geotagged)
