from operator import itemgetter 
from multithread_search_cl import Pickle
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
    print('%s |%s| %s%% %s' % (prefix, bar, percent, suffix) + f" CPU {psutil.cpu_percent()}%", end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()

def timer():
    max_reg = 481
    value = 0

    while value != max_reg:
        value = len(Pickle().pickle_read('region'))
        printProgressBar(value, max_reg, prefix = '  Progress:', suffix = '::', length = 25)
        sys.stdout.write("\033[K")
        time.sleep(1)


if __name__ == '__main__':
    timer()