# -*- coding: utf-8 -*- 

__author__ = "Road36"
__date__ = "19-5-31"

"""
Describe:
"""
from scrapy import cmdline
import scrapy
# from scrapy.loader import ItemLoader
from tools.logger import logger
from Crawler.items import ProxyItem
from Crawler.items import ComonItemLoader
from bs4 import BeautifulSoup


class ProxySpider(scrapy.Spider):
    custom_settings = {
        "ITEM_PIPELINES": {
            'Crawler.pipelines.ProxyPipeline': 300,
        },
        "FEED_URI": "/home/ly/code/my_project/Crawler/Resources/report/ippool.json",
        "FEED_FORMAT": 'json'
    }

    ORIGIN_URL = "https://www.kuaidaili.com/free/inha/"
    name = "proxy"
    allowed_domains = ["kuaidaili.com"]
    start_urls = [
        "https://www.kuaidaili.com/free/inha/",
        # "https://book.douban.com",
        # "http://www.dmozdir.org/"
    ]

    def __init__(self):
        super(ProxySpider, self).__init__()
        self.page_count = 2

    # def start_requests(self):
    #     yield scrapy.Request('https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4', self.parse)
    #     yield scrapy.Request('http://www.dmozdir.org/', self.parse)

    def logged_in(self, response):
        # here you would extract links to follow and return Requests for
        # each of them, with another callback
        pass

    def parse(self, response):
        for proxy in response.css("table.table.table-bordered.table-striped tbody tr"):

            content = ComonItemLoader(ProxyItem(), selector=proxy)
            # list > table > tbody > tr:nth-child(1) > td:nth-child(1)
            content.add_css("ip", "td:nth-child(1)::text")
            content.add_css("port", "td:nth-child(2)::text")
            content.add_css("level", "td:nth-child(3)::text")
            content.add_css("http_type", "td:nth-child(4)::text")
            content.add_css("location", "td:nth-child(5)::text")
            content.add_css("speed", "td:nth-child(6)::text")
            ci2 = content.load_item()
            # logger.info("!!!!!!!{0}".format(ci2))
            yield ci2

        if self.page_count < 4:
            # next_page = "free/intr/{0}/".format(self.page_count)
            yield scrapy.Request(self.ORIGIN_URL + str(self.page_count), callback=self.parse)
            self.page_count += 1
        # with open("Resources/report/" + filename, 'wb') as f:
        #     f.write(response.body)


if __name__ == '__main__':
    # ds = DoubanSpider()
    # ds.parse()
    cmdline.execute("scrapy crawl proxy".split())
