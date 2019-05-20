import pickle
from datetime import datetime
import os

path_list = ['db_top3.dat', 'db_6x45.dat', 'db_5x36plus.dat']


for path in path_list:
    with open(path, 'rb') as rf:
        read = pickle.load(rf)
    time_change = datetime.fromtimestamp(os.path.getmtime(path)).strftime('%d-%m-%Y %H:%M:%S')
    print(len(read))
    print(time_change)
