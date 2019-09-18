import time
from craigslist import CraigslistHousing
def func1():
    x = CraigslistHousing(site = 'sfbay',category='apa',area='eby')
    t0 = time.time()
    for i in x.get_results(sort_by='newest'):
        pass
    t1 = time.time()
    print(t1-t0)
#appending to list in list comprehension is nearly 2x faster than simpy iterating over get_results()
def func2():
    x = CraigslistHousing(site = 'sfbay',category='apa',area='eby')
    t0 = time.time()
    y = [i for i in x.get_results(sort_by='newest')]
    t1 = time.time()
    print(t1-t0)
#creating a direct list from the generator has the same performance as func2
def func3():
    x = CraigslistHousing(site = 'sfbay',category='apa',area='eby')
    t0 = time.time()
    y = list(x.get_results(sort_by='newest'))
    t1 = time.time()
    print(t1-t0)