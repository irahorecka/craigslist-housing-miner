"""py file to search these selected subcategories in Craigslist Housing.
Omit items from selected_cat if undesired."""

class SelectionKeys:
    selected_cat = [
        "apa",
        "swp",
        "off",
        "prk",
        "reb",
        "reo",
        "roo",
        "sub",
        "vac",
        "hou",
        "rew",
        "sha",
        "sbw"
    ]  # e.g. ['apa', 'roo'] - multiprocessing_cl.py will handle boston and newyork exceptions
