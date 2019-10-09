from lxml import html
import requests
import csv

def return_body(url):
    page = requests.get(url)
    tree = html.fromstring(page.content)

    post = tree.xpath('//section[@id="postingbody"]/text()') #extract craigslist post body
    return ('n@nn@ih'.join(post[1:])) #print craigslist post body

class States:
    state_keys = ['alabama', 'arizona', 'arkansas', 'california', 'colorado', 'connecticut', 'delaware', 'district_of_columbia', 'florida', 'georgia', 
        'idaho', 'illinois', 'indiana', 'iowa', 'kansas', 'kentucky', 'louisiana', 'maine', 'maryland', 'massachusetts', 'michigan', 'minnesota', 
        'mississippi', 'missouri', 'montana', 'nebraska', 'nevada', 'new_hampshire', 'new_jersey', 'new_mexico', 'new_york', 'north_carolina', 'north_dakota', 
        'ohio', 'oklahoma', 'oregon', 'pennsylvania', 'rhode_island', 'south_carolina', 'south_dakota', 'tennessee', 'texas', 'utah', 'vermont', 'virginia', 
        'washington', 'west_virginia', 'wisconsin', 'wyoming']