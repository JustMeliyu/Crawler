# -*- coding: utf-8 -*- 

__author__ = "Road36"
__date__ = "19-5-29"

"""
Describe:
"""
import scrapy
from tools.logger import logger
from Crawler.items import CrawlerItem


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["chinadmoz.org"]
    start_urls = [
        "http://www.chinadmoz.org/",
        "http://www.dmozdir.org/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
            ci = CrawlerItem()
            title = response.xpath('/html/head/title/text()').extract()
            ci['title'] = title
            logger.info("111111111111111111{0}".format(title))
            yield ci


if __name__ == '__main__':
    ds = DmozSpider()
    # ds.parse()


