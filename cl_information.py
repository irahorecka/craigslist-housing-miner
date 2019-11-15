#ALL CL FILTERS AND STATES' CRAIGSLIST REGIONS IN DICTIONARY

class Filters:
    #A file to store room filters, rooming categories, and state keys in dictionaries
    #extra_filters is a general filter sheet for specifics - not all housing categories adhere to every part of this filter
    #e.g. you will not look for max_bedrooms for a room/share craigslist posts
    #create selectors in the future to limit which filters are mutable by the user per category they choose
    extra_filters = {'private_room' : None, #bool
        'private_bath' : None, #bool
        'cats_ok' : None, #bool
        'dogs_ok' : None, #bool
        'min_price' : None,
        'max_price' : None,
        'min_ft2' : None,
        'max_ft2' : None,
        'min_bedrooms' : None,
        'max_bedrooms' : None,
        'min_bathrooms' : None,
        'max_bathrooms' : None,
        'no_smoking' : None, #bool
        'is_furnished' : None, #bool
        'wheelchair_acccess' : None, #bool
        'has_image' : None #bool
    }

    distance_filters = {'search_distance': None,
        'zip_code': None
    }

    cat_dict = {'apa':'apts & housing for rent',
        'swp':'housing swap',
        'off':'office & commercial',
        'prk':'parking & storage',
        'reb':'real estate - by broker',
        'reo':'real estate - by owner',
        'roo':'rooms & shares',
        'sub':'sublets & temporary',
        'vac':'vacation rentals',
        'hou':'wanted: apts',
        'rew':'wanted: real estate',
        'sha':'wanted: room & share',
        'sbw':'wanted: sublet & temp'}