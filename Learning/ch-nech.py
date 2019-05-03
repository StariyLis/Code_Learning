import matplotlib.pyplot as plt
import pickle
import pandas as pd
ch_nch = []

with open('C:/Users\Stari\PycharmProjects\Learning_Code\Learning\draw_data.dat', 'rb') as rf:
    data = pickle.load(rf)

# for i in data.values():
#     ch = 0
#     nch = 0
#     for j in i[1]:
#         if j % 2 == 0:
#             ch += 1
#         else:
#             nch += 1
#     ch_nch.append([ch, nch])

    df = pd.DataFrame(data.values())
    print(df['Доп. Шар'])
    plt.plot(df['1-й Шар'], 'yo', df['2-й Шар'], 'ro')
    plt.show()
def start():
    print(ch_nch)


if __name__ == '__main__':
    start()
