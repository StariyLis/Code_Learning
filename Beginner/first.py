import requests
from bs4 import BeautifulSoup
from collections import Counter


class Stoloto():
    def __init__(self, url):
        self.url = url
        print('Класс ' + self.url.split('/')[3] + ' создан')


    def get_html(self):
        r = requests.get(self.url)
        return r.text


    def get_date(self):
        draw_ball= {}
        draw = []
        date = []
        time = []
        ball = []
        soup = BeautifulSoup(self.get_html(), 'lxml')
        month = soup.findAll('div', class_='month')
        for h in month:
            elem = h.find_all('div', class_='elem')
            for i in elem:
                draw = int(i.find('div', class_='draw').text)
                date = i.find('div', class_='draw_date').text.split()[0]
                time = i.find('div', class_='draw_date').text.split()[1]
                try:
                    b = i.find('div', class_='container cleared').find('span', class_='zone').find_all('b')
                    ball = [int(z.text) for z in b]

                except Exception:
                    print('Ahhhhhh')
                draw_ball[draw] = ball

        return draw_ball


lotto_5x36plus = Stoloto('https://www.stoloto.ru/5x36plus/archive')
lotto_6x45 = Stoloto('https://www.stoloto.ru/6x45/archive')

print(lotto_5x36plus.get_date())