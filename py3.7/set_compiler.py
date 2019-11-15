import pprint as pprint
from cl_information import Countries as countries


"""
A script to compress every state (or province) in
cl_information.Countries into a tuple format to be 
parsed by multiprocessing_cl.py

Copy print output and set in compiled_set.Search
class where appropriate
"""

country_list = [country for country in countries.__dict__ if country[0:2] != '__']

for country in country_list:
    input('')
    tot_list = []
    tot_crushed = []
    area_list = []
    area_crushed = []
    try:
        for province in eval(f'countries.{country}'):
            item = eval(f'countries.{country}["{province}"]')
            if 'focus_dist' not in item:
                tot_list.append([(province,k) for k,v in item.items()])
            else:
                tot_list.append([(province,k) for k,v in item.items() if k != 'focus_dist' and k not in item['focus_dist']])
                area_list.append([(province,k,v2) for k,v in item['focus_dist'].items() for v2 in v])
    except AttributeError:
        tot_list.append([(country,k) for k,v in eval(f"countries.{country}.items()")])
    for i in tot_list:
        tot_crushed.extend(i)
    for i in area_list:
        area_crushed.extend(i)

    tot_crushed.extend(area_crushed)
    tot_set = set(tot_crushed)

    pprint.pprint(f'{country} = {tot_set}'.replace('{','[').replace('}',']'))
    #print(len(tot_set))