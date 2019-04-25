#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import pickle
import os
import sys

j_file = 'draw_data.dat'
url = 'https://www.stoloto.ru/rapido/archive'
path_file = j_file


def get_html(url):
    r = requests.get(url)
    return r.text


def get_data():
    soup = BeautifulSoup(get_html(url), 'lxml')
    start = soup.find_all('div', class_='elem')

    all_draws = {}

    for data in start:
        dict_draw = dict.fromkeys(['Дата и время', '1-й Шар', '2-й Шар', '3-й Шар', '4-й Шар', '5-й Шар', '6-й Шар',
                                   '7-й Шар', '8-й Шар', 'Доп. Шар'])
        # Get lottery draw number & date
        draw_number = int(data.find('div', class_='draw').text)
        dict_draw['Дата и время'] = data.find('div', class_='draw_date').text[:-3]

        b = data.find('div', class_='container cleared').find_all('span')
        dict_draw['Доп. Шар'] = int(b[1].find('b').text)
        ball = b[0].find_all('b')
        dict_draw['1-й Шар'] = int(ball[0].text)
        dict_draw['2-й Шар'] = int(ball[1].text)
        dict_draw['3-й Шар'] = int(ball[2].text)
        dict_draw['4-й Шар'] = int(ball[3].text)
        dict_draw['5-й Шар'] = int(ball[4].text)
        dict_draw['6-й Шар'] = int(ball[5].text)
        dict_draw['7-й Шар'] = int(ball[6].text)
        dict_draw['8-й Шар'] = int(ball[7].text)

        all_draws[draw_number] = dict_draw
    return all_draws


def write_data():
    d = get_data()
    if not os.path.exists(path_file):
        open(j_file, 'wb').close()
    if os.path.getsize(path_file) == 0:
        with open(j_file, 'wb') as wr_file:
            pickle.dump(d, wr_file)
    else:
        with open(j_file, 'rb') as rd_file:
            read_data = pickle.load(rd_file)
            d.update(read_data)
            with open(j_file, 'wb') as wr_file:
                pickle.dump(d, wr_file)

    return read_data


# def send_message():
    # os.system('notify-send "{}"'.format(len(write_data())))


def main():
    # send_message()
    print(len(write_data()))
    print(write_data())
    print(len(get_data()))
    print(get_data())


if __name__ == '__main__':
    main()
