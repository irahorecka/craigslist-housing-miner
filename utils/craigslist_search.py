import csv
import datetime
import os
from craigslist import CraigslistHousing
import pandas as pd
from . import get_static_file

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
DATA_DIR = os.path.join(BASE_DIR, "data", f"{datetime.date.today()}")


def scrape_housing(craigslist_region):
    """Module function to appropriately scrape and write Craigslist
    housing information using specified housing categories and filters."""

    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    housing_categories = get_static_file.housing_categories()
    if len(craigslist_region) == 4:
        state, region, sub_region, geotag_bool = craigslist_region
    else:
        state, region, geotag_bool = craigslist_region
        sub_region = ""

    for category in housing_categories:
        search_result = query_housing_data(
            state, region, sub_region, category, geotag_bool
        )
        if not search_result:
            continue

        if sub_region:
            write_single_result_to_csv(search_result, state, sub_region, category)
        else:
            write_single_result_to_csv(search_result, state, region, category)

    if sub_region:
        concat_similar_results_to_csv(state, sub_region)
    else:
        concat_similar_results_to_csv(state, region)


def query_housing_data(state, reg, sub_reg, housing_cat, geotag):
    """A function to apply housing filters and instantiate
    craigslist.CraigslistHousing object with appropriate data."""

    search_filters = get_static_file.search_filters()
    if sub_reg:
        housing_object = CraigslistHousing(
            site=reg, area=sub_reg, category=housing_cat, filters=search_filters
        )
        return mine_housing_data(
            housing_object, state, reg, housing_cat, geotag, sub_reg=sub_reg
        )
    else:
        housing_object = CraigslistHousing(
            site=reg, category=housing_cat, filters=search_filters
        )
        return mine_housing_data(housing_object, state, reg, housing_cat, geotag)


def mine_housing_data(
    housing_obj,
    state,
    region,
    housing_category,
    geotagged,
    sub_reg="",
    code_break=";n@nih;",
):
    """A function to appropritely concatenate information sourced from
    the Craigslist housing object to a header list for downstream CSV
    export."""

    header = [
        f"State or Country{code_break}Region{code_break}"
        f"Subregion{code_break}Housing Category{code_break}"
        f"Post ID{code_break}Repost of (Post ID){code_break}"
        f"Title{code_break}URL{code_break}"
        f"Date Posted{code_break}Time Posted{code_break}"
        f"Price{code_break}Location{code_break}"
        f"Post has Image{code_break}Post has Geotag{code_break}"
        f"Bedrooms{code_break}Area"
    ]
    try:
        header.extend(
            [
                f"{state}{code_break}{region}{code_break}"
                f"{sub_reg if sub_reg else region}{code_break}"
                f"{get_static_file.housing_categories().get(housing_category)}{code_break}"
                f"{post['id']}{code_break}{post['repost_of']}{code_break}"
                f"{post['name']}{code_break}{post['url']}{code_break}"
                f"{post['datetime'][0:10]}{code_break}{post['datetime'][11:]}{code_break}"
                f"{post['price']}{code_break}{post['where']}{code_break}"
                f"{post['has_image']}{code_break}{post['geotag']}{code_break}"
                f"{post['bedrooms']}{code_break}{post['area']}"
                for post in housing_obj.get_results(
                    sort_by=None, geotagged=geotagged, limit=None
                )
            ]
        )
        return header
    except (AttributeError, OSError) as error:
        print(error)
        return


def is_data_related(func):
    """Wrapper to change into data directory if function is pertaining
    to data export."""

    def wrapper(*args, **kwargs):
        os.chdir(DATA_DIR)
        func(*args, **kwargs)
        os.chdir(BASE_DIR)

    return wrapper


@is_data_related
def write_single_result_to_csv(
    search_result, state, region, category, code_break=";n@nih;"
):
    """Write single result file to CSV (i.e. file with state, region,
    and housing category)"""

    file_title = f"{datetime.date.today()}_craigslist_{category}_{state}_{region}.csv"
    with open(file_title, "w", newline="") as csv_file:
        writer = csv.writer(csv_file, delimiter=",")
        try:
            writer.writerows([row.split(code_break) for row in search_result])
        except TypeError as error:
            print(error)


@is_data_related
def concat_similar_results_to_csv(state, reg):
    """Concatenate all CSV files pertaining to a state and region
    (or sub-region) to one CSV file."""

    grouped_files = [file for file in os.listdir() if f"{state}_{reg}" in file]
    for index, file in enumerate(grouped_files):
        if os.path.isfile(file):
            if index == 0:
                concat_file = pd.read_csv(file)
            else:
                concat_file = concat_file.append(pd.read_csv(file))
            os.remove(file)
    try:
        concat_file.to_csv(f"CraigslistHousing_{state}_{reg}.csv", index=False)
    except UnboundLocalError as error:
        print(error)
