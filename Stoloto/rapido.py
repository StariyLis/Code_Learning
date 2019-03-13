import requests
from bs4 import BeautifulSoup
from pprint import pprint as pp

# file = 'Z:/PycharmProjects/CSV_file/data_draw.json'


def get_html():
    req = requests.get('https://www.stoloto.ru/rapido/archive')
    return req.text


def get_data():
    soup = BeautifulSoup(get_html(), 'lxml')
    data = soup.find_all('div', {'class': 'elem'})

    # Дни проведения тиража
    draw_date = [date.find('div', {'class': 'draw_date'}).text[:-3] for date in data]
    list_ball_draw = []
    # Выпавшие номера
    ball_date = [date.find('div', {'class': 'container cleared'}).find_all('b') for date in data]

    for i in ball_date:
        ball = []
        for j in i:
            ball.append(int(j.text))
        list_ball_draw.append(ball)
    all_data_list = []
    ch_nech = []
    all_data_list.append(['Дата и время', '1-й', '2-й', '3-й', '4-й', '5-й', '6-й',
                          '7-й', '8-й', '', 'Доп', '', '',  'Чётных', 'Нечётных'])
    all_data_list.append(draw_date)
    all_data_list.append(list_ball_draw)
    for i in list_ball_draw:
        ch = 0
        nech = 0
        for j in i[:-1]:
            if j % 2 == 0:
                ch +=1
            else:
                nech += 1
            c_nc = [ch, nech]
        ch_nech.append(c_nc)
    all_data_list.append(ch_nech)
    return all_data_list


def main():
    pp(get_data())


if __name__ == '__main__':
    main()
