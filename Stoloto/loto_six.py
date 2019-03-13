import requests
from bs4 import BeautifulSoup
import time
from pprint import pprint as pp


def get_html():
    while True:
        req = requests.get('https://www.stoloto.ru/6x45/archive')
        if req.status_code != 200:
            print('Ошибка, Код ответа: %s', req.status)
            time.sleep(15)
            continue
        return req.text


def get_data():
    list_b = []
    draw_date = []
    draw = []
    soup = BeautifulSoup(get_html(), 'lxml')
    date = soup.findAll('div', 'draw_date')

    for i in date[1:]:
        draw_date.append(i.text)
    date = soup.findAll('div', 'draw')
    for i in date[1:]:
        draw.append(i.text[1:-1])
    div = soup.findAll('div', {'class': 'container cleared'})
    for i in div:
        b = i.find_all('b')
        b_1 = []
        for j in b:
            b_1.append(int(j.text))
        list_b.append(b_1)
    all_data_list = []
    ch_nch = []
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
    all_data_list.append(
        ['Дата и время', '1-й', '2-й', '3-й', '4-й', '5-й', '6-й', '', '', 'Чётных', 'Нечётных', '', '1', '2', '3',
         '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22',
         '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40',
         '41', '42', '43', '44', '45'])
    all_data_list.append(draw_date)
    all_data_list.append(list_b)
    all_data_list.append(ch_nch)
    return all_data_list


def main():
    # draw_date, list_b = get_data()
    pp(get_data())


if __name__ == '__main__':
    main()
