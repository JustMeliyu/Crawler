# -*- coding: utf-8 -*- 

__author__ = "Road36"
__date__ = "19-5-29"

"""
Describe:
"""
from scrapy import cmdline
import scrapy
from scrapy.loader import ItemLoader
from tools.logger import logger
from Crawler.items import CrawlerItem, BookItem
from bs4 import BeautifulSoup
from tools.common import strip
import pdb


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["book.douban.com"]
    start_urls = [
        "https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4",
        # "https://book.douban.com",
        # "http://www.dmozdir.org/"
    ]

    # def start_requests(self):
    #     yield scrapy.Request('http://www.chinadmoz.org/', self.parse)
    #     yield scrapy.Request('http://www.dmozdir.org/', self.parse)

    def logged_in(self, response):
        # here you would extract links to follow and return Requests for
        # each of them, with another callback
        pass

    def parse(self, response):
        filename = response.url.split("/")[-2]
        logger.info("filename is {0}".format(filename))
        # pdb.set_trace()
        content = ItemLoader(BookItem(), response=response)

        content.add_css("book_name", "div.info h2 a::attr(title)")
        content.add_css("auth_info", "div.info div.pub::text")
        content.add_css("point", "div.star.clearfix span.rating_nums::text")
        content.add_css("person_num", "div.star.clearfix span.pl::text")
        content.add_css("resume", "div.info p::text")
        content.add_css("book_detail_url", "div.info h2 a::attr(href)")
        # content.add_xpath("book_name", "/html/head/title/text()")

        ci2 = content.load_item()
        # logger.info("!!!!!!!{0}".format(ci2))
        yield ci2

        # logger.info("+++++++++{0}".format(ci2.book_name))
        #
        # content = response.body
        # book_info = content
        # soup = BeautifulSoup(content, "lxml")
        #
        # logger.info("================={0}".format(soup.title.string))
        #
        # ci = CrawlerItem()
        # title = response.xpath('/html/head/title/text()').extract()
        # ci['title'] = title
        # logger.info("111111111111111111{0}".format(title))
        #
        with open(filename, 'wb') as f:
            f.write(response.body)
        # yield ci


if __name__ == '__main__':
    # ds = DoubanSpider()
    # ds.parse()
    cmdline.execute("scrapy crawl douban".split())
