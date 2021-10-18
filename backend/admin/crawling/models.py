import pandas as pd
from sklearn import preprocessing
from admin.common.models import ValueObject, Printer, Reader
from icecream import ic
import numpy as np
import csv
from selenium import webdriver
from bs4 import BeautifulSoup
import datetime as dt
from konlpy.tag import Okt
from nltk.tokenize import word_tokenize
import nltk
import re


class Crawling(object):
    def __init__(self):
        pass

    def process(self):
        # nltk.download()
        vo = ValueObject()
        vo.context = 'admin/crawling/data/'
        # self.naver_movie()
        # self.tweet()
        self.samsung_report(vo)

    def samsung_report(self, vo):
        okt = Okt()
        okt.pos('삼성전자 글로벌센터 전자사업부', stem=True)
        vo.fname = 'kr-Report_2018.txt'
        with open(vo.context+vo.fname, 'r', encoding='UTF-8') as f:
            texts = f.read()
        print(texts)


    def naver_movie(self):
        vo = ValueObject()
        vo.context = 'admin/crawling/data/'
        vo.url = 'http://movie.naver.com/movie/sdb/rank/rmovie.nhn'
        driver = webdriver.Chrome(f'{vo.context}/chromedriver')
        driver.get(vo.url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        all_div = soup.findAll('div', {'class': 'tit3'})
        arr = [div.a.string for div in all_div]
        # for i in arr:
        #     print(i)
        # driver.close()

        # index = [i+1 for i in range(len(arr))]
        # with open(vo.context + 'new_data/with_save.csv', 'w', encoding='UTF-8') as f:
        #     w = csv.writer(f)
        #     list(map(lambda row: w.writerow(row), zip(index, arr)))
            # w.writerow(dt.keys())
            # w.writerow(dt.values())

        dt = {i+1: val for i, val in enumerate(arr)}
        rank = pd.DataFrame.from_dict(dt, orient='index', columns=['movie'])
        rank.to_csv(vo.context+'new_data/with_save.csv')
        driver.close()

    def tweet(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = webdriver.Chrome('admin/crawling/data/chromedriver', options=options)

        start_date = dt.date(year=2018, month=12, day=1)
        until_date = dt.date(year=2018, month=12, day=2)  # 시작날짜 +1
        end_date = dt.date(year=2018, month=12, day=2)
        query = 'obama'
        total_tweets = []
        url = f'https://twitter.com/search?q={query}%20' \
              f'since%3A{str(start_date)}%20until%3A{str(until_date)}&amp;amp;amp;amp;amp;amp;lang=eg'
        while not end_date == start_date:
            driver.get(url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            last_height = driver.execute_script("return document.body.scrollHeight")
            while True:
                daily_freq = {'Date': start_date}
                word_freq = 0
                tweets = soup.find_all('p', {'class': 'TweetWextSize'})
                driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                new_height = driver.execute_script('return document.body.scrollHeight')
                if new_height != last_height:
                    soup = BeautifulSoup(driver.page_source, 'html.parser')
                    tweets = soup.find_all('p', {'class', 'TweetTextSize'})
                    word_freq = len(tweets)
                else:
                    daily_freq['Frequency'] = word_freq
                    word_freq = 0
                    start_date = until_date
                    until_date = dt.timedelta(days=1)
                    daily_freq = {}
                    total_tweets.append(tweets)
                    break
                last_height = new_height
        query_df = pd.DataFrame(columns=['id', 'message'])
        number = 1
        for i in range(len(total_tweets)):
            for j in range(len(total_tweets[i])):
                query_df = query_df.append({'id': number, 'message': (total_tweets[i][j]).text},
                                           ignore_index=True)
                number = number + 1
        print(query_df.head())