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

    # Get lottery draw number & date
    draw_number = [int(i.find('div', class_='draw').text) for i in start]
    date = [i.find('div', class_='draw_date').text[:-3] for i in start]

    dop_ball = []
    draw_ball = []
    dict_draws = dict.fromkeys(i for i in draw_number)
    for i in start:
        c = []
        b = i.find('div', class_='container cleared').find_all('span')
        ball = b[0].find_all('b')
        dop_ball.append(int(b[1].find('b').text))
        for i in ball:
            c.append(int(i.text))
        draw_ball.append(c)

    for k in range(50):
        dict_draws[draw_number[k]] = [date[k], draw_ball[k], dop_ball[k]]
    return dict_draws


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
