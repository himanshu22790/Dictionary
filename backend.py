import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

import sys, os 
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)



data = json.load(open(resource_path('data.json')))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys(), cutoff=0.8)) > 0:
        yn = input('Did you mean %s instead? Please enter Y/N to confirm' % get_close_matches (w, data.keys())[0])
         #0 is to check suggestions starting with the first word of the input
        if yn == 'Y':
             return data[get_close_matches (w, data.keys())[0]]
    else:
        return 'The word you are trying to search does not exists, please double check your input.'

