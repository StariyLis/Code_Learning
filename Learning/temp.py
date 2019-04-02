import pickle
import os
from datetime import datetime
from pprint import pprint as pp
import sqlite3

path = '/home/stariylis/PycharmProjects/Learning_Code/Learning/draw_data.dat'

with open(path, 'rb') as rf:
    data = pickle.load(rf)
time_change = datetime.fromtimestamp(os.path.getmtime(path)).strftime('%d-%m-%Y %H:%M:%S')
print(len(data))
print(time_change)