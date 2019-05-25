import requests
from bs4 import BeautifulSoup
import pickle
import os.path
import pandas as pd


class Stoloto():
    def __init__(self, url):
        self.url = url
        self.path = './db_' + self.url.split('/')[3] + '.dat'
        self.draw_ball= {}


    def get_html(self):
        r = requests.get(self.url)
        return r.text


    def get_date(self):

        all_ball = []
        draw_date = []
        soup = BeautifulSoup(self.get_html(), 'lxml')
        month = soup.findAll('div', class_='month')
        for h in month:
            ball = []
            elem = h.find_all('div', class_='elem')
            draw = [int(i.find('div', class_='draw').text) for i in elem]
            draw_date = [i.find('div', class_='draw_date').text[:-3] for i in elem]
            for i in elem:
                try:
                    b = i.find('div', class_='container cleared').find('span', class_='zone').find_all('b')
                    ball = [int(z.text) for z in b]
                except Exception:
                    print('Ahhhhhh')

                all_ball.append(ball)

        date = pd.to_datetime(draw_date)
        col = ['Ball_' + str(i) for i in range(1, len(all_ball[0]) + 1)]
        df = pd.DataFrame(all_ball, index=date, columns=col)
        s = df.to_dict(orient='index')
                # self.draw_ball[draw] = ball

        # if not os.path.exists(self.path):
        #     open(self.path, 'wb').close()
        #
        # if os.path.getsize(self.path) == 0:
        #     with open(self.path, 'wb') as fw:
        #         pickle.dump(self.draw_ball, fw)
        # with open(self.path, 'rb') as fr:
        #     read_data = pickle.load(fr)
        # read_data.update(self.draw_ball)
        # with open(self.path, 'wb') as fw:
        #     pickle.dump(read_data, fw)
        return s

top3 = Stoloto('https://www.stoloto.ru/top3/archive')
print(top3.get_date())