import pandas as pd
from sklearn import preprocessing
from admin.common.models import ValueObject, Printer, Reader
from icecream import ic
import numpy as np
import csv
from selenium import webdriver
from bs4 import BeautifulSoup


class Crawling(object):
    def __init__(self):
        pass

    def process(self):
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