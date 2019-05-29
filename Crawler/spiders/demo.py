# -*- coding: utf-8 -*- 

__author__ = "Road36"
__date__ = "19-5-29"

"""
Describe:
"""
import scrapy
from scrapy.spiders.crawl import CrawlSpider, Rule
from tools.logger import logger
from Crawler.items import CrawlerItem
from bs4 import BeautifulSoup


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["chinadmoz.org"]
    OffsiteMiddleware = True
    # start_urls = [
    #     "http://www.chinadmoz.org/",
    #     "http://www.dmozdir.org/"
    # ]

    def start_requests(self):
        yield scrapy.Request('http://www.chinadmoz.org/', self.parse)
        yield scrapy.Request('http://www.dmozdir.org/', self.parse)

    def logged_in(self, response):
        # here you would extract links to follow and return Requests for
        # each of them, with another callback
        pass

    def parse(self, response):
        filename = response.url.split("/")[-2]
        content = response.body
        soup = BeautifulSoup(content, "lxml")
        logger.info("================={0}".format(soup.title.string))

        ci = CrawlerItem()
        title = response.xpath('/html/head/title/text()').extract()
        ci['title'] = title
        logger.info("111111111111111111{0}".format(title))

        with open(filename, 'wb') as f:
            f.write(content)


if __name__ == '__main__':
    ds = DmozSpider()
    # ds.parse()


