"""
A program to facilitate multiprocessing search in Craigslist Housing
leveraging the python-craigslist library.
"""
import csv
import copy
import datetime
import time
import os
import pandas as pd
import random
import multiprocessing as mp
import queue
from craigslist import CraigslistHousing
from cl_information import Filters as clsd
from search_information import SelectionKeys as sk
from cl_regions import Regions

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = f"{BASE_DIR}/Data/{datetime.date.today()}"


class CLHousingSelect:
    """ This class will gather search parameters and
    pass into the python-craigslist module. This class
    encompasses methods to set search instance, execute
    search, and write search information to .csv files. """

    def __init__(self, country, inst_category, inst_filters, code_break, _geotag):
        self.country = country
        self.inst_category = inst_category
        self.inst_filters = inst_filters
        self.code_break = code_break
        self.geotag = _geotag
        self.cl_instance = ""

    def small_region(self, inst_site):
        try:
            self.cl_instance = CraigslistHousing(
                site=inst_site, category=self.inst_category, filters=self.inst_filters
            )
        except Exception as e:  # commonly requests.ConnectionError, requests.ConnectionResetError
            handle_error(e)

    def large_region(self, inst_site, inst_area):
        try:
            self.cl_instance = CraigslistHousing(
                site=inst_site,
                area=inst_area,
                category=self.inst_category,
                filters=self.inst_filters,
            )
        except Exception as e:
            handle_error(e)

    def parse_search(self, header_list, state, region, sub_region, category):
        try:
            header_list.extend(
                [
                    f"{self.country}{self.code_break}{state}{self.code_break}{region}{self.code_break}"
                    f"{sub_region}{self.code_break}{category}{self.code_break}"
                    f"{i['id']}{self.code_break}{i['repost_of']}{self.code_break}"
                    f"{i['name']}{self.code_break}{i['url']}{self.code_break}"
                    f"{i['datetime'][0:10]}{self.code_break}{i['datetime'][11:]}{self.code_break}"
                    f"{i['price']}{self.code_break}{i['where']}{self.code_break}"
                    f"{i['has_image']}{self.code_break}{i['geotag']}{self.code_break}"
                    f"{i['bedrooms']}{self.code_break}{i['area']}"
                    for i in self.cl_instance.get_results(
                        sort_by=None, geotagged=self.geotag, limit=None
                    )
                ]
            )
            if len(header_list) == 1:
                print(state, region, "NO POSTS**")
                # return None
            else:
                print(len(header_list), state, region)
            return header_list
        except (AttributeError, OSError) as e:
            handle_error(e)

    def write_to_file(self, write_list, inst_site_name, inst_state_name):
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)
        else:
            pass
        os.chdir(DATA_DIR)
        title = f"{datetime.date.today()}_geotag_{self.geotag}_craigslist_{self.inst_category}_{inst_site_name}_{inst_state_name}.csv"
        with open(title, "w", newline="") as rm_csv:
            writer = csv.writer(rm_csv, delimiter=",")
            try:
                writer.writerows([i.split(self.code_break) for i in write_list])
            except TypeError as e:
                handle_error(e)
        os.chdir(BASE_DIR)


class ExecuteSearch:
    """ A class to prepare search parameters by parsing
    search information into a format compatible with
    python-craigslist module. This class operates closely
    with CLHousingSelect. """

    def __init__(self, country, house_filter, q, d):
        self.q = q
        self.d = d
        self.country = country
        self.house_filter = house_filter  # (e.g. 'apa' or 'roo')
        self.room_filter = {**clsd.extra_filters, **clsd.distance_filters}
        self.code_break = ";n@nih;"
        self.header = [
            f"CL Country{self.code_break}CL State{self.code_break}CL Region{self.code_break}"
            f"CL District{self.code_break}Housing Category{self.code_break}"
            f"Post ID{self.code_break}Repost of (Post ID){self.code_break}"
            f"Title{self.code_break}URL{self.code_break}"
            f"Date Posted{self.code_break}Time Posted{self.code_break}"
            f"Price{self.code_break}Location{self.code_break}"
            f"Post has Image{self.code_break}Post has Geotag{self.code_break}"
            f"Bedrooms{self.code_break}Area"
        ]

    def cl_search(self, tup):
        housing_dict = clsd.housing_categories
        if len(tup) == 3:
            self.area(tup, housing_dict)
        else:
            self.site(tup, housing_dict)

    def site(self, tup, housing_dict):
        state, reg = tup[0].lower(), tup[1].lower()
        for cat in housing_dict:
            if cat not in self.house_filter:
                continue
            else:
                result = self.search_package(state, reg, cat, _geotag=self.d["geotag"])
            if not result:
                continue
        self.concat_csv(state, reg)

    def area(self, tup, housing_dict):
        state, reg, sub_reg = tup[0].lower(), tup[1].lower(), tup[2].lower()
        for cat in housing_dict:
            if cat not in self.house_filter:
                continue
            else:
                result = self.search_package(
                    state, reg, cat, area=sub_reg, _geotag=self.d["geotag"]
                )
            if not result:
                continue
        self.concat_csv(state, sub_reg)

    def search_package(self, state, reg, cat, _geotag, area=""):
        header_list = copy.deepcopy(self.header)
        housing_result = CLHousingSelect(
            self.country, cat, self.room_filter, self.code_break, _geotag
        )
        if area == "":
            area = reg
            housing_result.small_region(reg)
        else:
            housing_result.large_region(reg, area)
        try:
            if not housing_result.cl_instance:
                return None
            else:
                append_list = housing_result.parse_search(
                    header_list, state, reg, area, cat
                )
                if not append_list:
                    return None
                housing_result.write_to_file(append_list, area, state)
                return "OK"
        except AttributeError:
            pass

    def concat_csv(self, state, region):
        """
        once all subsearches for a search category (e.g. CraigslistHousing)
        is complete, concat all file content per state and region into one
        .csv file -- this will compress the amount of filespace in your Data
        directory.
        """
        if not os.path.exists(DATA_DIR):
            print(f"{DATA_DIR} does not exist.")
        else:
            os.chdir(DATA_DIR)
            file_list = [i for i in os.listdir() if f"{region}_{state}" in i]
            for i in enumerate(file_list):
                if os.path.isfile(i[1]):
                    if i[0] == 0:
                        cat_file = pd.read_csv(i[1])
                    else:
                        cat_file = cat_file.append(pd.read_csv(i[1]))
                    os.remove(i[1])
                else:
                    print("no_file")
            try:
                cat_file.to_csv(f"CraigslistHousing_{state}_{region}.csv", index=False)
            except UnboundLocalError as error:
                handle_error(error)


def handle_error(error):
    print(f"There was an error:: {error} - nothing written to file.")
    time.sleep(5)  # provide 5 sec wait time before continuing search


def execute_search(country, state, q, d):
    search_criteria = ExecuteSearch(country, sk.selected_cat, q, d)
    search_criteria.cl_search(state)


def main(_geotag):
    manager = mp.Manager()
    q = manager.Queue()
    d = manager.dict()
    d["geotag"] = _geotag
    pool = mp.Pool(mp.cpu_count() + 2)
    jobs = []
    country_list = [country for country in Regions.__dict__ if country[0:2] != "__"]
    for country in country_list:
        for province in eval(f"Regions.{country}"):
            job = pool.apply_async(execute_search, (country, province, q, d))
            jobs.append(job)
    try:
        for job in jobs:
            job.get(3000)  # timeout after 3000 sec
    except mp.TimeoutError:
        print("process exceeded 10 minutes: mutliprocessing terminated.")
        pool.terminate()
    print("process complete")


if __name__ == "__main__":
    GEOTAG_INPUT = (
        input("Would you like to search for geotagged results?[y/n]: ")
    ).lower()
    GEOTAG = True if GEOTAG_INPUT == "y" else False
    main(GEOTAG)
