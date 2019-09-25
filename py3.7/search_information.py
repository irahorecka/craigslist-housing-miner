#a .py file to outline selection parameters when scraping CL api.

class SelectionKeys:
    state_keys = ['alabama', 'arizona', 'arkansas', 'california', 'colorado', 'connecticut', 'delaware', 'district_of_columbia', 'florida', 'georgia', 
        'idaho', 'illinois', 'indiana', 'iowa', 'kansas', 'kentucky', 'louisiana', 'maine', 'maryland', 'massachusetts', 'michigan', 'minnesota', 
        'mississippi', 'missouri', 'montana', 'nebraska', 'nevada', 'new_hampshire', 'new_jersey', 'new_mexico', 'new_york', 'north_carolina', 'north_dakota', 
        'ohio', 'oklahoma', 'oregon', 'pennsylvania', 'rhode_island', 'south_carolina', 'south_dakota', 'tennessee', 'texas', 'utah', 'vermont', 'virginia', 
        'washington', 'west_virginia', 'wisconsin', 'wyoming']
    selected_reg = [] # e.g. ['sfbay','losangeles']
    selected_cat = ['apa'] # e.g. ['apa', 'roo'] - search_cl.py will handle boston and newyork exceptions
    district_list = [] # e.g. ['oakland','berkeley']
    dist_filters = [] # [zipcode, miles from zip]