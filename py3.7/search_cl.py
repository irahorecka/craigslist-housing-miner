#2019-09-11 - a general all-housing search criteria for california. The purpose of this script is to acquire information on california housing information
#post-processing should be done on data acquired by this script

import os
import csv
from craigslist import CraigslistHousing
import datetime
import time
import logging
from cl_information import Filters as clsd #make better abbreviation later
from cl_information import States as sr #make better abbreviation later
from search_information import SelectionKeys as sk
import copy
base_dir = os.getcwd()

class CL_Housing_Select:
    def __init__(self, inst_site, inst_category, inst_filters):
        self.inst_site = inst_site
        self.inst_category = inst_category
        self.inst_filters = inst_filters
        self.code_break = ';n@nih;'

    def small_region(self):
        #make this into another method and add small_region addition below as its native method function
        return CraigslistHousing(site=self.inst_site,category=self.inst_category,filters=self.inst_filters)

    def large_region(self, inst_area):
        return CraigslistHousing(site=self.inst_site,category=self.inst_category,filters=self.inst_filters,area=inst_area)

    def write_to_file(self, write_list, inst_site_name, inst_state_name):
        date = datetime.date.today()
        new_dir = '{}/Data/{}'.format(base_dir, date)
        if not os.path.exists(new_dir):
                os.makedirs(new_dir)
        else: 
            pass
        os.chdir(new_dir)
        title = f'{date}_all_craigslist_housing_{inst_site_name}_{inst_state_name.title()}.csv'
        with open(title, 'w', newline = '') as rm_csv:
            writer = csv.writer(rm_csv, delimiter = ',')
            writer.writerows([i.split(self.code_break) for i in write_list])
        rm_csv.close()
        os.chdir(base_dir)


def my_logger(func):
    logging.basicConfig(filename=f'{func.__name__}.log', level = logging.INFO)

    def wrapper(*args, **kwargs):
        date_time = str(datetime.datetime.now())[:-10]
        logging.info(
            f'Ran with filters: {clsd.room_filters} at {date_time}')
        return func(*args, **kwargs)

    return wrapper


class ExecSearch:
    def __init__(self, states):
        self.states = states
        self.code_break = ';n@nih;'
        self.header = [f'CL State{self.code_break}CL Region{self.code_break}CL District{self.code_break}Housing Category{self.code_break}Post ID{self.code_break}Repost of (Post ID){self.code_break}Title{self.code_break}URL{self.code_break}Date Posted{self.code_break}Time Posted{self.code_break}Price{self.code_break}Location{self.code_break}Post has Image{self.code_break}Post has Geotag{self.code_break}Bedrooms{self.code_break}Area']

    @my_logger
    def cl_search(self):
        t0 = time.time()
        housing_dict = clsd.cat_dict

        for state in self.states:
            focus_list = [] 
            if 'focus_dist' in eval(f'sr.{state}'):
                for reg, reg_name in eval(f'sr.{state}')["focus_dist"].items():
                    if reg == 'newyork' or reg == 'boston':
                        housing_dict = clsd.apa_dict
                    for sub_reg in reg_name:
                        header_list = copy.deepcopy(self.header)
                        for cat, cat_name in housing_dict.items():
                            housing_result = CL_Housing_Select(reg, cat, clsd.room_filters)
                            large_region = housing_result.large_region(sub_reg)
                            header_list.extend([f"{state.title()}{self.code_break}{reg}{self.code_break}{sub_reg}{self.code_break}{cat_name}{self.code_break}{i['id']}{self.code_break}{i['repost_of']}{self.code_break}{i['name']}{self.code_break}{i['url']}{self.code_break}{i['datetime'][0:10]}{self.code_break}{i['datetime'][11:]}{self.code_break}{i['price']}{self.code_break}{i['where']}{self.code_break}{i['has_image']}{self.code_break}{i['geotag']}{self.code_break}{i['bedrooms']}{self.code_break}{i['area']}" for i in large_region.get_results(sort_by='newest')])
                            print(state, sub_reg, cat)
                        housing_result.write_to_file(header_list, sub_reg, state)
                        focus_list.append(reg)
            for reg, reg_name in eval(f'sr.{state}').items():
                if reg in focus_list:
                    continue
                else:
                    try:
                        header_list = copy.deepcopy(self.header)
                        for cat, cat_name in housing_dict.items():
                            housing_result = CL_Housing_Select(reg, cat, clsd.room_filters)
                            small_region = housing_result.small_region()
                            header_list.extend([f"{state.title()}{self.code_break}{reg}{self.code_break}{reg_name}{self.code_break}{cat_name}{self.code_break}{i['id']}{self.code_break}{i['repost_of']}{self.code_break}{i['name']}{self.code_break}{i['url']}{self.code_break}{i['datetime'][0:10]}{self.code_break}{i['datetime'][11:]}{self.code_break}{i['price']}{self.code_break}{i['where']}{self.code_break}{i['has_image']}{self.code_break}{i['geotag']}{self.code_break}{i['bedrooms']}{self.code_break}{i['area']}" for i in small_region.get_results(sort_by='newest')])
                            print(state, reg, cat)
                        housing_result.write_to_file(header_list, reg_name, state)
                    except ValueError:
                        print('focus_dict encountered')
                        pass
            t1 = time.time()
            print(f"Run time: {'%.2f' % (t1 - t0)} sec")

def execute_search():
    search_criteria = ExecSearch(sk.state_keys)
    search_criteria.cl_search()