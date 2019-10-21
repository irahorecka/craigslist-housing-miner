import csv
import copy
import datetime
import time
import logging
import os
import random
import multiprocessing as mp
from craigslist import CraigslistHousing
from cl_information import Filters as clsd
from search_information import SelectionKeys as sk
from compiled_set import Search
base_dir = os.path.dirname(os.path.abspath(__file__))
# 2019-10-21 develop temp global dict to omit repetition of search param

class CLHousingSelect:
    def __init__(self, inst_site, inst_category,
                 inst_filters, code_break, geotag=False):
        self.geotag = geotag
        self.inst_site = inst_site
        self.inst_category = inst_category
        self.inst_filters = inst_filters
        self.code_break = code_break

    def small_region(self):
        try:
            self.cl_instance = CraigslistHousing(
                site=self.inst_site,
                category=self.inst_category,
                filters=self.inst_filters
                )
        except Exception as e:  # commonly requests.ConnectionError, requests.ConnectionResetError
            handle_error(e)

    def large_region(self, inst_area):
        try:
            self.cl_instance = CraigslistHousing(
                site=self.inst_site,
                category=self.inst_category,
                filters=self.inst_filters,
                area=inst_area
                )
        except Exception as e:
            handle_error(e)

    def exec_search(self, header_list,
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
            else:
                print(len(header_list), state, region)
                return header_list
        except (AttributeError, OSError) as e:
            handle_error(e)

    def write_to_file(self, write_list,
                      inst_site_name, inst_state_name):
        date = datetime.date.today()
        new_dir = f'{base_dir}/Data/{date}'
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
        else:
            pass
        os.chdir(new_dir)
        title = f"{date}_geotag_{self.geotag}_all_craigslist_housing_{inst_site_name}_{inst_state_name.title()}.csv"
        with open(title, 'w', newline='') as rm_csv:
            writer = csv.writer(rm_csv, delimiter=',')
            try:
                writer.writerows([
                    i.split(self.code_break) for i in write_list
                    ])
            except TypeError as e:
                handle_error(e)
                pass
        os.chdir(base_dir)


def my_logger(func):
    logging.basicConfig(filename=f'{func.__name__}.log', level=logging.INFO)

    def wrapper(*args, **kwargs):
        date_time = str(datetime.datetime.now())[:-10]
        log_dict = clsd.extra_filters  # remove addition of zip - consider logging zip or distance in future
        logging.info(
            f'Ran with filters: {log_dict} at {date_time}')
        return func(*args, **kwargs)

    return wrapper


class ExecSearch:
    def __init__(self, house_filter):
        self.house_filter = house_filter  # this is a list of selected categories (i.e. 'apa' or 'roo')
        self.room_filter = {**clsd.extra_filters, **clsd.distance_filters}
        self.continental_us = Search.continental_us
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
                       reg, cat, geotag, area):
        header_list = copy.deepcopy(self.header)
        housing_result = CLHousingSelect(
            reg, cat,
            self.room_filter, self.code_break, geotag
            )
        if area == "":
            area = reg
            housing_result.small_region()
        else:
            housing_result.large_region(area)
        try:
            if not housing_result.cl_instance:
                pass
            else:
                append_list = housing_result.exec_search(
                    header_list, state.title(), reg, area, cat
                    )
                if not append_list:
                    return None
                else:
                    housing_result.write_to_file(append_list, area, state)
                    return 'OK'
        except AttributeError:
            pass

    def search_geotag(self, state, reg,
                      cat, geotag, area=''):
        result = self.search_package(state, reg, cat, geotag, area)
        if not result:
            return None
        else:
            return 'OK'

    def site(self, tup, housing_dict, q, d):
        state, reg = tup[0], tup[1]
        for cat in housing_dict:
            if cat not in self.house_filter:
                continue
            else:
                result = self.search_geotag(
                    state, reg, cat, geotag=d['geotag']
                    )
            if not result:
                continue
            q.put(tup)

    def area(self, tup, housing_dict, q, d):
        state, reg, sub_reg = tup[0], tup[1], tup[2]
        for cat in housing_dict:
            if cat not in self.house_filter:
                continue
            else:
                result = self.search_geotag(
                    state, reg, cat, area=sub_reg, geotag=d['geotag']
                    )
            if not result:
                continue
            q.put(tup)

    @my_logger
    def cl_search(self, q, d):
        housing_dict = clsd.cat_dict
        random.shuffle(self.continental_us)
        for tup in self.continental_us:
            if tup not in d['region']:
                self.area(
                    tup, housing_dict, q, d
                    ) if len(tup) == 3 else self.site(
                        tup, housing_dict, q, d
                        )
            else:
                pass


def handle_error(error):
    print(f'There was an error:: {error} - nothing written to file.')
    logging.basicConfig(
        filename=f'{base_dir}/CL_Mining_Error.log', level=logging.INFO
        )
    logging.info(f'Time:: {datetime.datetime.today()}\nError:: {error}')
    time.sleep(5)  # provide 5 sec wait time before continuing search


def execute_search(q, d):
    search_criteria = ExecSearch(sk.selected_cat)
    search_criteria.cl_search(q, d)


def listener(q, d):
    while True:
        item_to_write = q.get()
        if item_to_write == 'kill':
            break
        foo = d['region']
        foo.add(item_to_write)
        d['region'] = foo


def main(geotag):
    manager = mp.Manager()
    q = manager.Queue()
    d = manager.dict()
    d['region'] = set()
    d['geotag'] = geotag
    pool = mp.Pool(mp.cpu_count() + 2)
    watcher = pool.apply_async(listener, (q, d))
    jobs = []
    for i in range(24):
        job = pool.apply_async(execute_search, (q, d))
        jobs.append(job)
    for job in jobs:
        job.get()
    q.put('kill')
    pool.close()
    pool.join()
    print('process complete')


if __name__ == '__main__':
    geotag_input = (input(
        "Would you like to search for geotagged results?[y/n]: "
        )).lower()
    if geotag_input == 'y':
        geotag = True
    else:
        geotag = False
    main(geotag)
