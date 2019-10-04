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
base_dir = os.path.dirname(os.path.abspath(__file__))

#1) CATCH EXCEPTIONS AND RUN AGAIN
class CL_Housing_Select:
    def __init__(self, inst_site, inst_category, inst_filters, code_break, geotag=False):
        self.geotag = geotag
        self.inst_site = inst_site
        self.inst_category = inst_category
        self.inst_filters = inst_filters
        self.code_break = code_break

    def small_region(self):
        try:
            self.cl_instance = CraigslistHousing(site=self.inst_site,category=self.inst_category,filters=self.inst_filters)
        except ConnectionError as e:
            handle_error(e)
            self.cl_instance = None

    def large_region(self, inst_area):
        try:
            self.cl_instance = CraigslistHousing(site=self.inst_site,category=self.inst_category,filters=self.inst_filters,area=inst_area)
        except ConnectionError as e:
            handle_error(e)
            self.cl_instance = None

    def exec_search(self, header_list, state, region, sub_region, category):
        try:
            header_list.extend([f"{state.title()}{self.code_break}{region}{self.code_break}{sub_region}{self.code_break}{category}{self.code_break}{i['id']}{self.code_break}{i['repost_of']}{self.code_break}{i['name']}{self.code_break}{i['url']}{self.code_break}{i['datetime'][0:10]}{self.code_break}{i['datetime'][11:]}{self.code_break}{i['price']}{self.code_break}{i['where']}{self.code_break}{i['has_image']}{self.code_break}{i['geotag']}{self.code_break}{i['bedrooms']}{self.code_break}{i['area']}" for i in self.cl_instance.get_results(sort_by='newest', geotagged=self.geotag)])
            return header_list
        except (AttributeError, OSError) as e:
            handle_error(e)
            return None

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
                handle_error(e)
                pass
        os.chdir(base_dir)


class Pickle:
    #LOOK INTO EOFERROR FILE NOT FOUND
    def pickle_reset(self):
        with open("completed_search.txt", "wb") as pickle_set:
            pickle.dump({'state':set(),'region':set(),'temp_region':set(),'geotag':''}, pickle_set)

    def pickle_read(self, category):
        time.sleep(random.uniform(.00001,.03))
        with open("completed_search.txt", "rb") as pickle_set:
            try:
                return pickle.load(pickle_set)[category]
            except EOFError as e:
                handle_error(e)

    def pickle_remove(self, category, item_to_remove):
        with open("completed_search.txt", "rb") as pickle_set:
            try:
                pickle_file = pickle.load(pickle_set)
            except EOFError as e:
                handle_error(e)
        with open("completed_search.txt", "wb") as pickle_set:
            if item_to_remove == 'ALL':
                if type(pickle_file[category]) == set:
                    pickle_file[category] = set() 
                else:
                    pickle_file[category] = ''
            else:
                pickle_file[category].remove(item_to_remove) 
            pickle.dump(pickle_file, pickle_set)

    def pickle_dump(self, category, item_to_write):
        with open("completed_search.txt", "rb") as pickle_set:
            try:
                pickle_file = pickle.load(pickle_set)
            except EOFError as e:
                handle_error(e)
        with open("completed_search.txt", "wb") as pickle_set:
            if type(pickle_file[category]) == set:
                pickle_file[category].add(item_to_write) 
            else:
                pickle_file[category] = item_to_write
            pickle.dump(pickle_file, pickle_set)


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
    def __init__(self, states, zip_list, regions, house_filter):
        self.zip_list = zip_list
        self.states = states
        self.regions = regions
        self.house_filter = house_filter #this is a list of selected categories (i.e. 'apa' or 'roo')
        self.room_filter = {**clsd.extra_filters, **clsd.distance_filters} 
        self.code_break = ';n@nih;'
        self.header = [f'CL State{self.code_break}CL Region{self.code_break}CL District{self.code_break}Housing Category{self.code_break}Post ID{self.code_break}Repost of (Post ID){self.code_break}Title{self.code_break}URL{self.code_break}Date Posted{self.code_break}Time Posted{self.code_break}Price{self.code_break}Location{self.code_break}Post has Image{self.code_break}Post has Geotag{self.code_break}Bedrooms{self.code_break}Area']

    def timeout(self):
        time.sleep(random.uniform(.00001,.03))

    def search_package(self, state, reg, cat, geotag, area):
        header_list = copy.deepcopy(self.header)
        housing_result = CL_Housing_Select(reg, cat, self.room_filter, self.code_break, geotag)
        if area == "":
            area = reg
            housing_result.small_region()
        else:
            housing_result.large_region(area)
        if not housing_result.cl_instance:
            pass
        else:
            append_list = housing_result.exec_search(header_list, state.title(), reg, area, cat)
            if not append_list:
                pass
            else:
                #print(state, reg, cat)
                housing_result.write_to_file(append_list, area, state)

    def search_geotag(self, state, reg, cat, area = ''):
        self.search_package(state, reg, cat, Pickle().pickle_read('geotag'), area)
            

    @my_logger
    def cl_search(self):
        time.sleep(.001)
        t0 = time.time()
        housing_dict = clsd.cat_dict
        if self.zip_list != []:
            self.room_filter['zip_code'] = self.zip_list[0]
            self.room_filter['search_distance'] = self.zip_list[1]
        for state in self.states:
            self.timeout()
            if state in Pickle().pickle_read('state'):
                continue
            if 'focus_dist' in eval(f'sr.{state}'):
                focus_items = list(eval(f'sr.{state}')["focus_dist"].items())
                random.shuffle(focus_items)
                for reg, reg_name in focus_items:
                    if reg in self.regions or self.regions == []:
                        is_loop = True
                        self.timeout()
                        if reg in Pickle().pickle_read('region') or reg in Pickle().pickle_read('temp_region'):
                            continue
                        Pickle().pickle_dump('temp_region',reg)
                        for sub_reg in reg_name:
                            if sub_reg in Pickle().pickle_read('region'):
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
                            Pickle().pickle_dump('region', sub_reg)
                        Pickle().pickle_remove('temp_region', reg)    
                    Pickle().pickle_dump('region', reg)
            state_items = list(eval(f'sr.{state}').items())
            random.shuffle(state_items)
            for reg, reg_name in state_items:
                if reg in self.regions or self.regions == []:
                    self.timeout()
                    if reg in Pickle().pickle_read('region') or reg in Pickle().pickle_read('temp_region'):
                        continue
                    Pickle().pickle_dump('temp_region', reg)
                    try:
                        for cat in housing_dict:
                            if cat not in self.house_filter:
                                continue
                            else:
                                self.search_geotag(state, reg, cat)
                    except ValueError:
                        pass
                    Pickle().pickle_remove('temp_region', reg)
                Pickle().pickle_dump('region', reg)
            Pickle().pickle_dump('state', state)
        t1 = time.time()
        #print(f"Run time: {'%.2f' % (t1 - t0)} sec")


def list_shuffle(lst):
    lst_2 = copy.deepcopy(lst)
    random.shuffle(lst_2)
    return lst_2


def handle_error(error):
    print(f'There was an error:: {error} - nothing written to file.')
    logging.basicConfig(filename=f'{base_dir}/CL_Mining_Error.log', level = logging.INFO)
    logging.info(f'Time:: {datetime.datetime.today()}\nError:: {error}')
        

def execute_search(state_list):
    search_criteria = ExecSearch(state_list, sk.dist_filters, sk.selected_reg, sk.selected_cat)
    search_criteria.cl_search()  


def main():
    t0 = time.time()

    pool = multiprocessing.Pool()
    try:
        for i in range(24):
            pool.imap_unordered(execute_search, (list_shuffle(sk.state_keys),))
    except Exception:
        pool.close()
        pool.terminate()
    else:
        pool.close()
        pool.join()

    '''pool = multiprocessing.Pool()
    for i in range(24):
        pool.apply_async(execute_search, args = (list_shuffle(sk.state_keys), ))
    pool.close()
    pool.join()'''

    t1 = time.time()
    delta_t = t1 - t0
    print(f"Multiprocessing run time: {'%.2f' % (delta_t)} sec")


if __name__ == '__main__':
    clear_pickle = (input('Would you like to clear search history?[y/n]: ')).lower()
    if clear_pickle == 'y':
        Pickle().pickle_reset() if input('Are you sure?[y/n]: ') == 'y' else None
    geo_tag = (input('Would you like to search for geotagged results?\nThe performance will significantly decline.[y/n]: ')).lower() #ADD TO PICKLE FILE
    if geo_tag == 'y':
        Pickle().pickle_dump('geotag',True)
    else:
        Pickle().pickle_dump('geotag',False)
    Pickle().pickle_remove('temp_region', 'ALL')
    
    main()