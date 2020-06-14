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
        location.append(geotagged)

    specific_locations_tuple = tuple(tuple(location) for location in specific_locations)
    utils.map_processes(utils.scrape_housing, specific_locations_tuple)
    # utils.scrape_housing(specific_locations_tuple[0])


if __name__ == "__main__":
    # simple demo for now - eventually accept user args and kwargs
    countries = ["japan", "united_kingdom"]
    main(countries=countries, geotagged=False)
