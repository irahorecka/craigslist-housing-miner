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
    def __init__(self, inst_site, inst_category, inst_filters, code_break,geotag=False):
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
        header_list.extend(["{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}".format(state.title(),self.code_break,region,self.code_break,sub_region,self.code_break,category,self.code_break,i['id'],self.code_break,i['repost_of'],self.code_break,i['name'],self.code_break,i['url'],self.code_break,i['datetime'][0:10],self.code_break,i['datetime'][11:],self.code_break,i['price'],self.code_break,i['where'],self.code_break,i['has_image'],self.code_break,i['geotag'],self.code_break,i['bedrooms'],self.code_break,i['area']) for i in self.cl_instance.get_results(sort_by='newest', geotagged=self.geotag)])
        return header_list

    def write_to_file(self, write_list, inst_site_name, inst_state_name):
        date = datetime.date.today()
        new_dir = '{}/Data/{}'.format(base_dir, date)
        if not os.path.exists(new_dir):
                os.makedirs(new_dir)
        else: 
            pass
        os.chdir(new_dir)
        title = '{}_geotag_{}_all_craigslist_housing_{}_{}.csv'.format(date,self.geotag,inst_site_name,inst_state_name.title())
        with open(title, 'w', newline = '') as rm_csv:
            writer = csv.writer(rm_csv, delimiter = ',')
            writer.writerows([i.split(self.code_break) for i in write_list])
        rm_csv.close()
        os.chdir(base_dir)


def my_logger(func):
    logging.basicConfig(filename='{}.log'.format(func.__name__), level = logging.INFO)

    def wrapper(*args, **kwargs):
        date_time = str(datetime.datetime.now())[:-10]
        logging.info(
            'Ran with filters: {} at {}'.format(clsd.room_filters,date_time))
        return func(*args, **kwargs)

    return wrapper


class ExecSearch:
    def __init__(self, states, filters):
        self.states = states
        self.code_break = ';n@nih;'
        self.header = ['CL State{}CL Region{}CL District{}Housing Category{}Post ID{}Repost of (Post ID){}Title{}URL{}Date Posted{}Time Posted{}Price{}Location{}Post has Image{}Post has Geotag{}Bedrooms{}Area'.format(self.code_break,self.code_break,self.code_break,self.code_break,self.code_break,self.code_break,self.code_break,self.code_break,self.code_break,self.code_break,self.code_break,self.code_break,self.code_break,self.code_break,self.code_break)]
        self.filter = filters

    @my_logger
    def cl_search(self):
        t0 = time.time()
        housing_dict = clsd.cat_dict

        for state in self.states:
            focus_list = [] 
            if 'focus_dist' in eval('sr.{}'.format(state)):
                for reg, reg_name in eval('sr.{}'.format(state))["focus_dist"].items():
                    if reg == 'newyork' or reg == 'boston':
                        housing_dict = clsd.apa_dict
                    for sub_reg in reg_name:
                        for cat, cat_name in housing_dict.items():
                            if cat not in self.filter:
                                continue
                            else:
                                for i in range(2):
                                    header_list = copy.deepcopy(self.header)
                                    if i == 0:
                                        housing_result = CL_Housing_Select(reg, cat, clsd.room_filters, self.code_break, geotag=False)
                                    else:
                                        housing_result = CL_Housing_Select(reg, cat, clsd.room_filters, self.code_break, geotag=True)
                                    housing_result.large_region(sub_reg)
                                    append_list = housing_result.exec_search(header_list, state.title(), reg, sub_reg, cat_name)
                                    print(state, sub_reg, cat)
                                    housing_result.write_to_file(append_list, sub_reg, state)
                focus_list.append(reg)
            for reg, reg_name in eval('sr.{}'.format(state)).items():
                if reg in focus_list:
                    continue
                else:
                    try:
                        for cat, cat_name in housing_dict.items():
                            if cat not in self.filter:
                                continue
                            else:
                                for i in range(2):
                                    header_list = copy.deepcopy(self.header)
                                    if i == 0:  
                                        housing_result = CL_Housing_Select(reg, cat, clsd.room_filters, self.code_break, geotag=False)
                                    else:
                                        housing_result = CL_Housing_Select(reg, cat, clsd.room_filters, self.code_break, geotag=True)
                                    housing_result.small_region()
                                    append_list = housing_result.exec_search(header_list, state.title(), reg, sub_reg, cat_name)
                                    print(state, reg, cat)
                                    housing_result.write_to_file(append_list, reg_name, state)
                    except ValueError:
                        print('focus_dict encountered')
                        pass
            t1 = time.time()
            print("Run time: {} sec".format('%.2f' % (t1 - t0)))

def execute_search():
    search_criteria = ExecSearch(sk.state_keys, sk.category_filters)
    search_criteria.cl_search()