from operator import itemgetter 
from multithread_search_cl import Pickle
from search_information import SelectionKeys as sk
import progressbar
import sys
import pickle
import time
import psutil

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 0, length = 100, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('%s |%s| %s%% %s' % (prefix, bar, percent, suffix) + f" {iteration}/{total} States : CPU {psutil.cpu_percent()}%", end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()

def timer():
    max_reg = len(sk.state_keys)
    value = 0

    try:
        while value != max_reg:
            value = len(Pickle().pickle_read('state'))
            printProgressBar(value, max_reg, prefix = '  Progress:', suffix = ':', length = 25)
            sys.stdout.write("\033[K")
            time.sleep(1)
    except KeyboardInterrupt as e:
        print(f'{e} Exiting protocol...')

if __name__ == '__main__':
    timer()