# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()


class BookItem(scrapy.Item):
    # 豆瓣书籍信息
    book_name = scrapy.Field()
    auth_name = scrapy.Field()
    press = scrapy.Field()
    publication_date = scrapy.Field()
    price = scrapy.Field()
    point = scrapy.Field()
    person_num = scrapy.Field()
    resume = scrapy.Field()
    book_detail_url = scrapy.Field()
