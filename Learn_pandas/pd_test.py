from string import ascii_letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

my_series1 = pd.Series([0, 1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e', 'f'])
my_series2 = pd.Series([5, 6, 7, 8, 9, 10], index=['g', 'h', 'i', 'j', 'k', 'l'])


for i in my_series2.values:
    print(i)
print([0, 1, 2, 3, 4, 5])