import re
import requests
from bs4 import BeautifulSoup as BS


def all_cl(url='https://www.craigslist.org/about/sites'):
    response = requests.get(url)
    soup = BS(response.content, 'html.parser')
    y = str(soup)
    z = y.split('<h4>')
    return z


def run_dict_search(z):
    us_can = input("are you looking for us or canada?[y/n]: ")
    for i in range(1,len(z)):
        s = z[i]
        state = re.findall('(.*)</h4>', s)
        state_write = '_'.join(state[0].split(' '))
        result = re.findall('//(.*).craigslist', s)
        focus = '' # for focus_dist if any
        if len(result) > 1:
            res = ''
            prov_link = re.findall('href="(.*)/">', s)
            for j in enumerate(result):
                try:
                    response = requests.get(prov_link[j[0]])
                    soup = BS(response.content, 'html.parser')
                    title_specifics = re.findall('<h2 class="area">(.*)</h2>', str(soup))[0]
                    res += f"'{j[1]}': '{title_specifics}',\n\t"
                    if 'sublinks' in str(soup):
                        area = re.findall('<ul class="sublinks">(.*)</ul>', str(soup))[0].split('<li>')
                        area = [re.findall('href="/(.*)/"', i) for i in area]
                        area.remove([])
                        area = [j for i in area for j in i]
                        focus += (f"'{j[1]}': {area},\n\t\t")
                except Exception as error:
                    print(f'{j} with exception {error}')
            if us_can.lower() == 'y':
                us_can_sub = ': '
                us_can_var = "'"
                us_can_cont = ","
                us_can_indent = "\t"
            else:
                us_can_sub = ' = '
                us_can_var = ""
                us_can_cont = ""
                us_can_indent = ""
            try:
                if focus[:-4] != '':
                    print(f"{us_can_var}{state_write.lower()}{us_can_var}{us_can_sub}"'{'+res+
                          f"'focus_dist': "'{' + focus[:-4] + '\n\t\t}'+'\n'+us_can_indent+'}'+us_can_cont)
                else:
                    print(f"{us_can_var}{state_write.lower()}{us_can_var}{us_can_sub}"'{'+res[:-3]+'\n'+us_can_indent+'}'+us_can_cont)
            except Exception:
                pass
        else:
            print(f"{us_can_var}{state_write.lower()}{us_can_var}{us_can_sub}"+'{'+f"'{result[0]}': '{result[0].title()}'"+'\n'+us_can_indent+'}'+us_can_cont)

            
if __name__ == "__main__":
    run_dict_search(all_cl())