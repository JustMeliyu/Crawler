# -*- coding: utf-8 -*- 

__author__ = "Road36"
__date__ = "19-5-29"

"""
Describe:
"""
from scrapy import cmdline
import scrapy
# from scrapy.loader import ItemLoader
from tools.logger import logger
from Crawler.items import BookItem
from Crawler.items import ComonItemLoader
from bs4 import BeautifulSoup


class DoubanSpider(scrapy.Spider):
    custom_settings = {
        "ITEM_PIPELINES": {
            'Crawler.pipelines.DoubanPipeline': 300,
        },
        "FEED_URI": "/home/ly/code/my_project/Crawler/Resources/report/test.csv",
        "FEED_FORMAT": 'csv'
    }

    ORIGIN_URL = "https://book.douban.com"
    name = "douban"
    allowed_domains = ["book.douban.com"]
    start_urls = [
        "https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4",
        # "https://book.douban.com",
        # "http://www.dmozdir.org/"
    ]

    def __init__(self):
        super(DoubanSpider, self).__init__()
        self.page_count = 0

    # def start_requests(self):
    #     yield scrapy.Request('https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4', self.parse)
    #     yield scrapy.Request('http://www.dmozdir.org/', self.parse)

    def logged_in(self, response):
        # here you would extract links to follow and return Requests for
        # each of them, with another callback
        pass

    def parse(self, response):
        filename = response.url.split("/")[-2]
        logger.info("filename is {0}".format(filename))
        for book in response.xpath("//li[@class='subject-item']"):
            content = ComonItemLoader(BookItem(), selector=book)

            content.add_css("book_name", "div.info h2 a::attr(title)")
            content.add_css("auth_info", "div.info div.pub::text")
            content.add_css("point", "div.star.clearfix span.rating_nums::text")
            content.add_css("person_num", "div.star.clearfix span.pl::text")
            content.add_css("resume", "div.info p::text")
            content.add_css("book_detail_url", "div.info h2 a::attr(href)")
            ci2 = content.load_item()
            # logger.info("!!!!!!!{0}".format(ci2))
            yield ci2

        # next_page = response.css("div.paginator span.next a::attr(href)").extract_first()
        # if next_page and self.page_count < 3:
        #     yield scrapy.Request(self.ORIGIN_URL + next_page, callback=self.parse)
        #     self.page_count += 1
        # with open("Resources/report/" + filename, 'wb') as f:
        #     f.write(response.body)


if __name__ == '__main__':
    # ds = DoubanSpider()
    # ds.parse()
    cmdline.execute("scrapy crawl douban".split())
