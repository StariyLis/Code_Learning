import pickle

ch_nch = []

with open('/home/stariylis/PycharmProjects/Learning_Code/Learning/draw_data.dat', 'rb') as rf:
    data = pickle.load(rf)

for i in data.values():
    ch = 0
    nch = 0
    for j in i[1]:
        if j % 2 == 0:
            ch += 1
        else:
            nch += 1
    ch_nch.append([ch, nch])


def start():
    print(ch_nch)


if __name__ == '__main__':
    start()
