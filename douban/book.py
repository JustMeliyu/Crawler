# -*- coding: utf-8 -*- 

__author__ = "Road36"
__date__ = "19-5-29"

"""
Describe:
抓取豆瓣读书
"""
from bs4 import BeautifulSoup
import requests
from tools.write_excel import generate_excel
from tools.common import get_func_time
import numpy as np
from tools.logger import logger
from datetime import datetime


@get_func_time
def read_book(url):
    f = requests.get(url)  # Get该网页从而获取该html内容
    soup = BeautifulSoup(f.content, "lxml")  # 用lxml解析器解析该网页的内容, 好像f.text也是返回的html

    n1 = datetime.now()
    title = ['书名', '作者', '出版社', '出版日期', '价格', '评分', '参与参分人', '简述', '详情链接地址']
    result = np.array([title], dtype=str)
    # result = [title]
    book_info = soup.find_all('li', class_='subject-item')
    for k in book_info:  # ,找到div并且class为pl2的标签

        book_name = k.find('h2').a['title']
        book_detail_url = k.find('h2').a['href']
        auth_info = k.find('div', class_='pub').string
        auth_info = auth_info.rsplit("/", 3)
        auth_info = list(map(lambda x: x.strip(), auth_info))

        book_point = k.find("span", class_="rating_nums").string
        person = k.find("span", class_="pl").string
        person = person.strip()[:-4][1:]
        resume = k.p.string

        current_info = [book_name] + auth_info + [book_point, person, resume, book_detail_url]
        result = np.append(result, [current_info], axis=0)
        # result.append(current_info)

    generate_excel("豆瓣读书", "小说", "./", result)
    n2 = datetime.now()
    logger.info((n2 - n1).total_seconds())


if __name__ == '__main__':
    # read_book("https://book.douban.com/chart")0.476913
    read_book("https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4")

