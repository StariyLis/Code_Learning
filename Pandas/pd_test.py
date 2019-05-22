import numpy as np
import pandas as pd
from datetime import datetime, date
import string



s_date = pd.date_range('2019-05-05', '2019-06-05')
ps = pd.Series(list(s_date))

print(ps)