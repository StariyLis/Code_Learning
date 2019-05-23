import pandas as pd

data = pd.read_pickle('./db_5x36plus.dat')
col = [str(i) + '-й шар' for i in range(1, (len(list(data.values())[0]) + 1))]
df_5x36 = pd.DataFrame(data.values(), index=data.keys(), columns=col)

print(df_5x36)