from lxml import html
import requests
import csv

def return_body(url):
    page = requests.get(url)
    tree = html.fromstring(page.content)

    post = tree.xpath('//section[@id="postingbody"]/text()') #extract craigslist post body
    return ('n@nn@ih'.join(post[1:])) #print craigslist post body