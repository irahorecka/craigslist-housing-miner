from bs4 import BeautifulSoup as BS
import requests

def return_body(url):
    cl_content = {}
    response = requests.get(url)
    soup = BS(response.content, 'html.parser')
    body = soup.find('section', id='postingbody')
    # We need to massage the data a little bit because it might include
    # some inner elements that we want to ignore.
    try:
        body_text = (getattr(e, 'text', e) for e in body
                    if not getattr(e, 'attrs', None))
    except TypeError:
        cl_content['body'] = 'This posting has been deleted by its author.'
        cl_content['imgs'] = None
        cl_content['lat'], cl_content['lon'] = None, None
        return cl_content

    cl_content['body'] = ''.join(body_text).strip().replace('\n','<br>')

    # Add images' urls.
    image_tags = soup.find_all('img')
    # If there's more than one picture, the first one will be repeated.
    image_tags = image_tags[1:] if len(image_tags) > 1 else image_tags
    images = []
    for img in image_tags:
        img_link = img['src'].replace('50x50c', '600x450')
        images.append(img_link)
    cl_content['imgs'] = images

    attrgroups = soup.find_all('p', {'class': 'attrgroup'})
    attrs = []
    for attrgroup in attrgroups:
        for attr in attrgroup.find_all('span'):
            attr_text = attr.text.strip()
            if attr_text:
                attrs.append(attr_text)
    # Find long lat
    post_map = soup.find('div', {'id': 'map'})
    cl_content['lat'], cl_content['lon'] = float(post_map.attrs['data-latitude']), float(post_map.attrs['data-longitude'])
    return cl_content

class States:
    state_keys = ['alabama', 'arizona', 'arkansas', 'california', 'colorado', 'connecticut', 'delaware', 'district_of_columbia', 'florida', 'georgia', 
        'idaho', 'illinois', 'indiana', 'iowa', 'kansas', 'kentucky', 'louisiana', 'maine', 'maryland', 'massachusetts', 'michigan', 'minnesota', 
        'mississippi', 'missouri', 'montana', 'nebraska', 'nevada', 'new_hampshire', 'new_jersey', 'new_mexico', 'new_york', 'north_carolina', 'north_dakota', 
        'ohio', 'oklahoma', 'oregon', 'pennsylvania', 'rhode_island', 'south_carolina', 'south_dakota', 'tennessee', 'texas', 'utah', 'vermont', 'virginia', 
        'washington', 'west_virginia', 'wisconsin', 'wyoming']