import requests
from bs4 import BeautifulSoup
from collections import Counter


class Stoloto():
    def __init__(self, url):
        self.url = url
        print('Класс ' + self.url.split('/')[3] + ' создан')


    def get_html(self):
        r = requests.get(self.url).text
        return r

    def get_date(self):
        draw_date = {}
        draw = []
        date = []
        ball_draw = []
        ball = []
        soup = BeautifulSoup(self.get_html(), 'lxml')
        month = soup.findAll('div', class_='month')
        for h in month:
            elem = h.find_all('div', class_='elem')
            draw = [int(i.find('div', class_='draw').text) for i in elem]
            date = [i.find('div', class_='draw_date').text for i in elem]
            for d in elem:
                b = d.find('div', class_='container cleared').find('span', class_='zone').find_all('b')
                ball_draw = [int(z.text) for z in b]
                ball.append(ball_draw)
        return draw, date, ball

# lotto_5x36plus = Stoloto('https://www.stoloto.ru/5x36plus/archive')
# print(lotto_5x36plus.get_date()[2])
top3 = Stoloto('https://www.stoloto.ru/top3/archive')
print(top3.get_date()[2])
# rapido = Stoloto('https://www.stoloto.ru/rapido/archive')
# print(rapido.get_date()[2])