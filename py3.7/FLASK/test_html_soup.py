from bs4 import BeautifulSoup as BS
import requests
from lxml import html

def return_body(url):
    page = requests.get(url)
    soup = BS(page.text, features="lxml")
    for imgtag in soup.find_all('img'):
        print(imgtag['src'])
    print(soup.find(id='postingbody')) #returns html format
    '''tree = html.fromstring(page.content)
    post = tree.xpath('//section[@id="postingbody"]/text()')
    print(post)'''

