#Run sc.execute_search()
import search_cl as sc 

clear_pickle = (input('Would you like to clear search history?[y/n]: ')).lower()
if clear_pickle == 'y':
    sc.Pickle().pickle_reset()
sc.execute_search()