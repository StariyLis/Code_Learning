import requests
from bs4 import BeautifulSoup
import time


def get_html():
    while True:
        req = requests.get('https://www.stoloto.ru/5x36plus/archive')
        if req.status_code != 200:
            print('Ошибка, Код ответа: %s', rs.status)
            time.sleep(15)
            continue
        return req.text


def get_data():
    list_b = []
    ch_nch = []
    soup = BeautifulSoup(get_html(), 'lxml')
    date = soup.findAll('div', 'draw_date')
    draw_date = [i.text for i in date[1:]]

    div = soup.findAll('div', {'class': 'container cleared'})
    for i in div:
        b = i.find_all('b')
        b_1 = []
        for j in b[:-1]:
            b_1.append(int(j.text))
        list_b.append(b_1)

    for j in range(len(list_b)):
        ch = 0
        nch = 0
        for i in list_b[j]:
            if i % 2 == 0:
                ch += 1
            else:
                nch += 1
            d_ch_nch = [ch, nch]
        ch_nch.append(d_ch_nch)

    return ch_nch


# def ch_nech():
#
#     ar_top = get_data()[1]

#     return ch_nch


def main():
    # data = ch_nech()
    print(get_data())


if __name__ == '__main__':
    main()

['Дата и время', '1-й', '2-й', '3-й', '4-й', '5-й', '', '', 'Чётных', 'Нечётных', '', '1', '2', '3', '4',
             '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22',
             '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36']