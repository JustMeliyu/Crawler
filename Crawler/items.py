# -*- coding: utf-8 -*-

# Define here the models for your scraped items
# items 是保存数据的容器    ItemLoader 是提供填充容器数据的机制
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst


class ComonItemLoader(ItemLoader):
    default_input_processor = MapCompose(lambda x: x.strip())
    default_output_processor = TakeFirst()


class CrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()


class BookItem(scrapy.Item):
    # 豆瓣书籍信息
    book_name = scrapy.Field(
        # input_processor=MapCompose(lambda x: x + "success"),
        # output_processor=TakeFirst()  # 取第一个元素
    )
    auth_info = scrapy.Field(
        # input_processor=MapCompose(_get_info),
    )
    auth_name = scrapy.Field()
    press = scrapy.Field()
    publication_date = scrapy.Field()
    price = scrapy.Field(
        input_processor=MapCompose(lambda x: x.strip.rstrip("元"))
    )
    point = scrapy.Field()
    person_num = scrapy.Field(
        input_processor=MapCompose(lambda x: x.strip()[:-4][1:])
    )
    resume = scrapy.Field(
        input_processor=MapCompose(lambda x: x.strip())
    )
    book_detail_url = scrapy.Field()


class ProxyItem(scrapy.Item):
    # 代理IP信息
    ip = scrapy.Field()
    port = scrapy.Field()
    level = scrapy.Field(
        input_processor=MapCompose(lambda x: x.strip())
    )
    http_type = scrapy.Field()
    location = scrapy.Field()
    speed = scrapy.Field(
        input_processor=MapCompose(lambda x: x.rstrip("秒"))
    )
