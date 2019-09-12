#Script to run loop every 15 minutes
#Works, uncomment print(execute()) in execute_search.py if not using this script
import search_cl as sc 
import time

while True:
    print(sc.execute_search())
    time.sleep(900)
