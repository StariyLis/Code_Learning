import requests
from bs4 import BeautifulSoup
import pandas as pd
pd.set_option('display.max_columns', 10)

def get_html():
    while True:
        req = requests.get('https://www.stoloto.ru/5x36plus/archive')
        if req.status_code != 200:
            print('Ошибка, Код ответа: %s', req.status)
            continue
        return req.text


def get_data():



    soup = BeautifulSoup(get_html(), 'lxml')
    elem = soup.findAll('div', 'elem')
    all_data = {}

    list_ball = []
    ball =[]
    for i in elem:
        draw_data = {}
        # draw_data = dict.fromkeys(['Дата и время', '1-й', '2-й', '3-й', '4-й', '5-й', 'Доп.шар', 'Чётные', 'Нечётные'])
        draw_data['0 Дата и время'] = i.find('div', class_='draw_date').text
        draw = int(i.find('div', class_='draw').find('a').text)
        div = i.find('div', class_='numbers').findAll('div', class_='container cleared')

        for k in div:
            b = k.find_all('b')
            ball = [int(a.text) for a in b[:-1]]
            draw_data['1-й'] = int(b[0].text)
            draw_data['2-й'] = int(b[1].text)
            draw_data['3-й'] = int(b[2].text)
            draw_data['4-й'] = int(b[3].text)
            draw_data['5-й'] = int(b[4].text)
            draw_data['Доп.шар'] = int(b[5].text)
            draw_data['Все шары тиража'] = ball

            ch = 0
            nch = 0

            for ball_ch in b[:-1]:
                if int(ball_ch.text) % 2 == 0:
                    ch += 1
                else: nch += 1
                draw_data['Чётные'] = ch
                draw_data['Нечётные'] = nch
        list_ball.append(ball)
        all_data[draw] = draw_data

    return all_data



def main():
    print('\n\tPandas.DataFrame\n')
    df = pd.DataFrame(get_data().values(), index=get_data().keys())
    print(df)
    # print('\n\tPandas.Series\n')
    # df['Ball'] = pd.Series(get_data()[1])
    # print(df)



if __name__ == '__main__':
    main()
