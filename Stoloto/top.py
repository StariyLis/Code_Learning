import requests
from bs4 import BeautifulSoup
import pandas as pd




def get_html():
    req = requests.post('https://www.stoloto.ru/top3/archive')
    return req.text


def get_data():
    all_ball = {}
    soup = BeautifulSoup(get_html(), 'lxml')
    data = soup.find('div', class_='month').find_all('div', 'elem')
    for g in data:
        number_draw = int(g.find('div', class_='draw').find('a').text)
        column = {}

        try:
            ball = g.find('div', class_='container cleared').find('span', class_='zone').find_all('b')

            column['Шар_1'] = int(ball[0].text)
            column['Шар_2'] = int(ball[1].text)
            column['Шар_3'] = int(ball[2].text)
        except AttributeError:
            print('Ждём-с')
        column['Дата и время'] = g.find('div', class_='draw_date').text[:-3]
        all_ball[number_draw] = column
    # ch_nch = []
    # for i in balls:
    #     ch = 0
    #     nch = 0
    #     for j in i:
    #         if j % 2 == 0:
    #             ch += 1
    #         else:
    #             nch += 1
    #         d_ch_nch = [ch, nch]
    #     ch_nch.append(d_ch_nch)
    # all_data.append(draw_date)
    # all_data.append(balls)
    # all_data.append(ch_nch)
    return all_ball


def main():
    date_time = pd.DataFrame(get_data().values(), index=get_data().keys())
    print(date_time[['Шар_1','Шар_2','Шар_3']])


if __name__ == '__main__':
    main()


