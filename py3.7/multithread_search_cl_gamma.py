"""
A program to facilitate multiprocessing search in Craigslist Housing
leveraging the python-craigslist library.
"""
import csv
import copy
import datetime
import time
import logging
import os
import random
import multiprocessing as mp
import queue
from craigslist import CraigslistHousing
from cl_information import Filters as clsd
from search_information import SelectionKeys as sk
from compiled_set import Search
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
"""
2019-10-21 develop temp global dict
to omit repetition of search param
"""


class CLHousingSelect:
    """ This class will gather search parameters and
    pass into the python-craigslist module. This class
    encompasses methods to set search instance, execute
    search, and write search information to .csv files. """

    def __init__(self, inst_category,
                 inst_filters, code_break, _geotag):
        self.inst_category = inst_category
        self.inst_filters = inst_filters
        self.code_break = code_break
        self.geotag = _geotag
        self.cl_instance = ""

    def small_region(self, inst_site):
        try:
            self.cl_instance = CraigslistHousing(
                site=inst_site,
                category=self.inst_category,
                filters=self.inst_filters
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

    def parse_search(self, header_list,
                     state, region, sub_region, category):
        try:
            header_list.extend(
                [f"{state.title()}{self.code_break}{region}{self.code_break}"
                 f"{sub_region}{self.code_break}{category}{self.code_break}"
                 f"{i['id']}{self.code_break}{i['repost_of']}{self.code_break}"
                 f"{i['name']}{self.code_break}{i['url']}{self.code_break}"
                 f"{i['datetime'][0:10]}{self.code_break}{i['datetime'][11:]}{self.code_break}"
                 f"{i['price']}{self.code_break}{i['where']}{self.code_break}"
                 f"{i['has_image']}{self.code_break}{i['geotag']}{self.code_break}"
                 f"{i['bedrooms']}{self.code_break}{i['area']}"
                 for i in self.cl_instance.get_results(
                     sort_by=None,
                     geotagged=self.geotag,
                     limit=None
                 )]
                )
            if len(header_list) == 1:
                print(state, region, 'FAILED')
                return None
            print(len(header_list), state, region)
            return header_list
        except (AttributeError, OSError) as e:
            handle_error(e)

    def write_to_file(self, write_list,
                      inst_site_name, inst_state_name):
        date = datetime.date.today()
        new_dir = f'{BASE_DIR}/Data/{date}'
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
        else:
            pass
        os.chdir(new_dir)
        title = f"{date}_geotag_{self.geotag}_craigslist_{self.inst_category}_{inst_site_name}_{inst_state_name.title()}.csv"
        with open(title, 'w', newline='') as rm_csv:
            writer = csv.writer(rm_csv, delimiter=',')
            try:
                writer.writerows([
                    i.split(self.code_break) for i in write_list
                    ])
            except TypeError as e:
                handle_error(e)
        os.chdir(BASE_DIR)


def my_logger(func):
    logging.basicConfig(filename=f'{func.__name__}.log', level=logging.INFO)

    def wrapper(*args, **kwargs):
        date_time = str(datetime.datetime.now())[:-10]
        log_dict = clsd.extra_filters
        # remove addition of zip - consider logging zip or distance
        logging.info(
            f'Ran with filters: {log_dict} at {date_time}')
        return func(*args, **kwargs)

    return wrapper


class ExecSearch:
    """ A class to prepare search parameters by parsing
    search information into a format compatible with
    python-craigslist module. This class operates closely
    with CLHousingSelect. """
    def __init__(self, house_filter, q, d):
        self.q = q
        self.d = d
        self.house_filter = house_filter  # (e.g. 'apa' or 'roo')
        self.room_filter = {**clsd.extra_filters, **clsd.distance_filters}
        self.code_break = ';n@nih;'
        self.header = [
            f"CL State{self.code_break}CL Region{self.code_break}"
            f"CL District{self.code_break}Housing Category{self.code_break}"
            f"Post ID{self.code_break}Repost of (Post ID){self.code_break}"
            f"Title{self.code_break}URL{self.code_break}"
            f"Date Posted{self.code_break}Time Posted{self.code_break}"
            f"Price{self.code_break}Location{self.code_break}"
            f"Post has Image{self.code_break}Post has Geotag{self.code_break}"
            f"Bedrooms{self.code_break}Area"
            ]

    def search_package(self, state,
                       reg, cat, _geotag, area):
        header_list = copy.deepcopy(self.header)
        housing_result = CLHousingSelect(
            cat, self.room_filter, self.code_break, _geotag
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
                    header_list, state.title(), reg, area, cat
                    )
                if not append_list:
                    return None
                housing_result.write_to_file(append_list, area, state)
                return 'OK'
        except AttributeError:
            pass

    def search_geotag(self, state, reg,
                      cat, _geotag, area=''):
        result = self.search_package(state, reg, cat, _geotag, area)
        if not result:
            return None
        else:
            return 'OK'

    def site(self, tup, housing_dict):
        state, reg = tup[0], tup[1]
        for cat in housing_dict:
            if cat not in self.house_filter:
                continue
            else:
                result = self.search_geotag(
                    state, reg, cat, _geotag=self.d['geotag']
                    )
            if not result:
                continue

    def area(self, tup, housing_dict):
        state, reg, sub_reg = tup[0], tup[1], tup[2]
        for cat in housing_dict:
            if cat not in self.house_filter:
                continue
            else:
                result = self.search_geotag(
                    state, reg, cat, area=sub_reg, _geotag=self.d['geotag']
                    )
            if not result:
                continue

    @my_logger
    def cl_search(self, tup):
        housing_dict = clsd.cat_dict
        if len(tup) == 3:
            self.area(tup, housing_dict)
        else:
            self.site(tup, housing_dict)


def handle_error(error):
    print(f'There was an error:: {error} - nothing written to file.')
    logging.basicConfig(
        filename=f'{BASE_DIR}/CL_Mining_Error.log', level=logging.INFO
        )
    logging.info(f'Time:: {datetime.datetime.today()}\nError:: {error}')
    time.sleep(5)  # provide 5 sec wait time before continuing search


def execute_search(i, q, d):
    search_criteria = ExecSearch(sk.selected_cat, q, d)
    search_criteria.cl_search(i)
<<<<<<< HEAD
=======


def listener(q, d, stop_event):
    while not stop_event.is_set():
        try:
           exc_tup = q.get(timeout=0.1)
           execute_search(exc_tup, q, d)
        except queue.Empty:
            pass
    print("Listener process stopped")
>>>>>>> 6b68b281f7f89261d3bc6ad4238de822f7a3465c


def main(_geotag):
    manager = mp.Manager()
    stop_event = manager.Event()
    q = manager.Queue()
    d = manager.dict()
    d['geotag'] = _geotag
    pool = mp.Pool(mp.cpu_count() + 2) # spawn?
    jobs = []
    for i in Search.continental_us:
        job = pool.apply_async(execute_search, (i, q, d))
        jobs.append(job)
    try:
        for job in jobs:
            job.get(300) # timeout after 300 sec
    except mp.TimeoutError:
        pool.terminate()
    print('process complete')


if __name__ == '__main__':
    GEOTAG_INPUT = (input(
        "Would you like to search for geotagged results?[y/n]: "
        )).lower()
    GEOTAG = True if GEOTAG_INPUT == "y" else False
    main(GEOTAG)