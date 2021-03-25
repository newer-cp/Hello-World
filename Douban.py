#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @ Time      :2021/3/21 11:39
# @ Author    :CP
# @ File      :Douban.py
# @ Fuction   :


import requests
from lxml import html

url_source = 'https://movie.douban.com/top250?start=0&filter='
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
import os

cookies = {"cookie": ''}
# 获取链接函数
from bs4 import BeautifulSoup
import pandas as pd

name_list = []
for n in range(0, 10):
    url_source = 'https://movie.douban.com/top250?start=' + str(n * 25) + '&filter='
    response = requests.get(url_source, headers=headers, cookies=cookies).text
    soup = BeautifulSoup(response, "lxml")
    list_all = soup.find_all('div', class_='info')

    soup = BeautifulSoup(response, "lxml")
    list_all = soup.find_all('div', class_='info')

    for i in list_all:
        names = i.find("div", class_='hd').a.text.strip()
        names = names.replace("\n", " ").replace("\xa0", " ")
        score = i.find('span', class_='rating_num').text.strip()
        info = i.find('div', class_='bd').p.text.strip()
        info = info.replace("\n", " ").replace("\xa0", " ")
        info = ' '.join(info.split())
        name_list.append([names, score, info])

    df = pd.DataFrame(name_list, columns=['电影名称', '评分 ', '信息'], index=None)
    df.to_csv("douban.csv",encoding='utf-8_sig')

