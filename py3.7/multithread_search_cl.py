import csv
import copy
import datetime
import time
import logging
import pickle
import os
import random
import multiprocessing
from craigslist import CraigslistHousing
from cl_information import Filters as clsd, States as sr #make better abbreviation later
from search_information import SelectionKeys as sk
base_dir = os.getcwd()

#FIX BUGG FOR AAP I.E. NY AND BOS
class CL_Housing_Select:
    def __init__(self, inst_site, inst_category, inst_filters, code_break, geotag=False):
        self.geotag = geotag
        self.inst_site = inst_site
        self.inst_category = inst_category
        self.inst_filters = inst_filters
        self.code_break = code_break

    def small_region(self):
        self.cl_instance = CraigslistHousing(site=self.inst_site,category=self.inst_category,filters=self.inst_filters)

    def large_region(self, inst_area):
        self.cl_instance = CraigslistHousing(site=self.inst_site,category=self.inst_category,filters=self.inst_filters,area=inst_area)

    def exec_search(self, header_list, state, region, sub_region, category):
        try:
            header_list.extend([f"{state.title()}{self.code_break}{region}{self.code_break}{sub_region}{self.code_break}{category}{self.code_break}{i['id']}{self.code_break}{i['repost_of']}{self.code_break}{i['name']}{self.code_break}{i['url']}{self.code_break}{i['datetime'][0:10]}{self.code_break}{i['datetime'][11:]}{self.code_break}{i['price']}{self.code_break}{i['where']}{self.code_break}{i['has_image']}{self.code_break}{i['geotag']}{self.code_break}{i['bedrooms']}{self.code_break}{i['area']}" for i in self.cl_instance.get_results(sort_by='newest', geotagged=self.geotag)])
            return header_list
        except (AttributeError, OSError) as e:
            print(f'There was an error:: {e}\nRERUN!')
            execute_search(list_shuffle(sk.state_keys))

    def write_to_file(self, write_list, inst_site_name, inst_state_name):
        date = datetime.date.today()
        new_dir = f'{base_dir}/Data/{date}'
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
        else: 
            pass
        os.chdir(new_dir)
        title = f'{date}_geotag_{self.geotag}_all_craigslist_housing_{inst_site_name}_{inst_state_name.title()}.csv'
        with open(title, 'w', newline = '') as rm_csv:
            writer = csv.writer(rm_csv, delimiter = ',')
            try:
                writer.writerows([i.split(self.code_break) for i in write_list])
            except TypeError as e:
                print(f'There was an error::{e}\nRERUN!')
                execute_search(list_shuffle(sk.state_keys))
        rm_csv.close()
        os.chdir(base_dir)


class Pickle:
    def pickle_reset(self):
        with open("completed_search.txt", "wb") as pickle_set:
            pickle.dump(set(), pickle_set)

    def pickle_read(self):
        with open("completed_search.txt", "rb") as pickle_set:
            return pickle.load(pickle_set)

    def pickle_dump(self, item_to_write):
        with open("completed_search.txt", "rb") as pickle_set:
            completed = pickle.load(pickle_set)
        with open("completed_search.txt", "wb") as pickle_set:
            completed.add(item_to_write)
            pickle.dump(completed, pickle_set)


def my_logger(func):
    logging.basicConfig(filename=f'{func.__name__}.log', level = logging.INFO)
    def wrapper(*args, **kwargs):
        date_time = str(datetime.datetime.now())[:-10]
        log_dict = clsd.extra_filters #remove addition of zip - consider logging zip or distance in future
        logging.info(
            f'Ran with filters: {log_dict} at {date_time}')
        return func(*args, **kwargs)
    return wrapper


class ExecSearch:
    pickle_file = Pickle()
    def __init__(self, states, zip_list, regions, house_filter):
        self.zip_list = zip_list
        self.states = states
        self.regions = regions
        self.house_filter = house_filter #this is a list of selected categories (i.e. 'apa' or 'roo')
        self.room_filter = {**clsd.extra_filters, **clsd.distance_filters} 
        self.code_break = ';n@nih;'
        self.header = [f'CL State{self.code_break}CL Region{self.code_break}CL District{self.code_break}Housing Category{self.code_break}Post ID{self.code_break}Repost of (Post ID){self.code_break}Title{self.code_break}URL{self.code_break}Date Posted{self.code_break}Time Posted{self.code_break}Price{self.code_break}Location{self.code_break}Post has Image{self.code_break}Post has Geotag{self.code_break}Bedrooms{self.code_break}Area']

    def search_package(self, state, reg, cat, geotag, area):
        header_list = copy.deepcopy(self.header)
        housing_result = CL_Housing_Select(reg, cat, self.room_filter, self.code_break, geotag)
        if area == "":
            area = reg
            housing_result.small_region()
        else:
            housing_result.large_region(area)
        append_list = housing_result.exec_search(header_list, state.title(), reg, area, cat)
        print(state, reg, cat)
        housing_result.write_to_file(append_list, area, state)

    def search_geotag(self, state, reg, cat, area = ''):
        for i in range(2):
            if i == 0:
                self.search_package(state, reg, cat, False, area) #no geotag search - False
            #else:
                #self.search_package(state, reg, cat, True, area) #geotag search - True

    @my_logger
    def cl_search(self):
        t0 = time.time()
        housing_dict = clsd.cat_dict
        if self.zip_list != []:
            self.room_filter['zip_code'] = self.zip_list[0]
            self.room_filter['search_distance'] = self.zip_list[1]
        for state in self.states:
            if state in self.pickle_file.pickle_read():
                continue
            if 'focus_dist' in eval(f'sr.{state}'):
                for reg, reg_name in eval(f'sr.{state}')["focus_dist"].items():
                    if reg in self.regions or self.regions == []:
                        is_loop = True
                        if reg == 'newyork' or reg == 'boston':
                            housing_dict = clsd.apa_dict
                            self.house_filter = ['aap' if i == 'apa' else i for i in self.house_filter]
                        if reg in self.pickle_file.pickle_read():
                            continue
                        for sub_reg in reg_name:
                            if sub_reg in self.pickle_file.pickle_read():
                                continue
                            for cat in housing_dict:
                                if cat not in self.house_filter:
                                    continue
                                elif self.room_filter['zip_code'] != None and self.room_filter['search_distance'] != None:
                                    self.search_geotag(state, reg, cat)
                                    is_loop = False
                                    break
                                else:
                                    self.search_geotag(state, reg, cat, sub_reg)
                            if not is_loop:
                                break
                            self.pickle_file.pickle_dump(sub_reg)
                        self.house_filter = ['apa' if i == 'aap' else i for i in self.house_filter]
                    self.pickle_file.pickle_dump(reg)
            for reg, reg_name in eval(f'sr.{state}').items():
                if reg in self.regions or self.regions == []:
                    if reg in self.pickle_file.pickle_read():
                        continue
                    else:
                        try:
                            for cat in housing_dict:
                                if cat not in self.house_filter:
                                    continue
                                else:
                                    self.search_geotag(state, reg, cat)
                        except ValueError:
                            print('focus_dict encountered')
                            pass
                self.pickle_file.pickle_dump(reg)
            self.pickle_file.pickle_dump(state)
        t1 = time.time()
        print(f"Run time: {'%.2f' % (t1 - t0)} sec")


def list_shuffle(lst):
    lst_2 = copy.deepcopy(lst)
    random.shuffle(lst_2)
    return lst_2


def execute_search(state_list):
    search_criteria = ExecSearch(state_list, sk.dist_filters, sk.selected_reg, sk.selected_cat)
    search_criteria.cl_search()  


if __name__ == '__main__':
    clear_pickle = (input('Would you like to clear search history?[y/n]: ')).lower()
    if clear_pickle == 'y':
        Pickle().pickle_reset()
    t0 = time.time()
    p1 = multiprocessing.Process(target=execute_search, args=(list_shuffle(sk.state_keys),))
    p2 = multiprocessing.Process(target=execute_search, args=(list_shuffle(sk.state_keys),))
    p3 = multiprocessing.Process(target=execute_search, args=(list_shuffle(sk.state_keys),))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()
    t1 = time.time()
    print(f"Multiprocessing run time: {'%.2f' % (t1 - t0)} sec")