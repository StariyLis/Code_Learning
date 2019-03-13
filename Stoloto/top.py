import requests
from bs4 import BeautifulSoup
from pprint import pprint as pp


def get_html():
    req = requests.post('https://www.stoloto.ru/top3/archive')
    return req.text


def get_data():
    all_data = []
    soup = BeautifulSoup(get_html(), 'lxml')
    data = soup.find('div', {'class': 'month'}).find_all('div', 'elem')

    draw_date = [i.find('div', 'draw_date').text[:-3] for i in data]

    numbers = [num.find('div', 'container cleared') for num in data]
    b = [num.find_all('b') for num in numbers]
    balls = []
    for i in list(b):
        ball = []
        ball.append(int(i[0].text))
        ball.append(int(i[1].text))
        ball.append(int(i[2].text))

        balls.append(ball)

    ch_nch = []
    for i in balls:
        ch = 0
        nch = 0
        for j in i:
            if j % 2 == 0:
                ch += 1
            else:
                nch += 1
            d_ch_nch = [ch, nch]
        ch_nch.append(d_ch_nch)
    all_data.append(['Дата и время', '1-й', '2-й', '3-й', '', '', 'Чётных', 'Нечётных'])
    all_data.append(draw_date)
    all_data.append(balls)
    all_data.append(ch_nch)
    return all_data


def main():
    date_time = get_data()

    pp(date_time)


if __name__ == '__main__':
    main()


