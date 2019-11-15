#a .py file to outline selection parameters when scraping CL api.

class SelectionKeys:
    selected_cat = ['apa', 'swp', 'off', 'prk', 'reb', 'reo', 'roo', 'sub', 'vac', 'hou', 'rew', 'sha', 'sbw'] # e.g. ['apa', 'roo'] - search_cl.py will handle boston and newyork exceptions