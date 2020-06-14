import time
import utils


def main():
    search_locations = utils.craigslist_regions().get("united_states")
    geotagged = True

    for location in search_locations:
        location.append(geotagged)

    search_location_tuple = tuple(tuple(location) for location in search_locations)
    short_search = (
        search_location_tuple[0],
        search_location_tuple[22],
        search_location_tuple[40],
    )

    t0 = time.time()
    utils.map_processes(utils.scrape_housing, short_search)
    t1 = time.time()
    print(t1 - t0)
    # utils.scrape_housing(search_location_tuple[0])


if __name__ == "__main__":
    main()
