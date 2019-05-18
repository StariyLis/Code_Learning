import requests
from bs4 import BeautifulSoup
import pickle
import os.path


class Stoloto():
    def __init__(self, url):
        self.url = url
        self.path = './db_' + self.url.split('/')[3] + '.dat'
        self.draw_ball= {}


    def get_html(self):
        r = requests.get(self.url)
        return r.text


    def get_date(self):

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
                self.draw_ball[draw] = ball

        if not os.path.exists(self.path):
            with open(self.path, 'wb') as fw:
                pickle.dump(self.draw_ball, fw)
        else:
            if os.path.getsize(self.path) != 0:
                with open(self.path, 'rb') as fr:
                    read_data = pickle.load(fr)
        read_data.update(self.draw_ball)
        return len(read_data)


top3 = Stoloto('https://www.stoloto.ru/top3/archive')
print(top3.get_date())