# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#
from scrapy.exceptions import DropItem
from tools.logger import logger
import time


class CrawlerPipeline(object):
    # @classmethod
    # def from_settings(cls, settings):
    #     """一般用于获取setting中的信息"""
    #     pass

    def process_item(self, item, spider):
        logger.info("------------------------------"*3)
        item['auth_name'] = []
        item['press'] = []
        item['publication_date'] = []
        item['price'] = []

        for ai in item['auth_info']:
            ai = ai.rsplit("/", 3)
            item['auth_name'].append(ai[0].strip())
            item['press'].append(ai[1].strip())
            item['publication_date'].append(ai[2].strip())
            item['price'].append(ai[3].strip())
        del item['auth_info']
        logger.info("=+++++++++={0}".format(item['auth_name']))
        # if item['price'].endwith("元"):
        #     item['price'] = item['price'].rstrip("元")
        #     logger.info("price is {0}".format(item['price']))
        # else:
        #     raise DropItem("price format error")
        return item

    def open_spide(self, spider):
        """run with spider open"""
        logger.info("3333333333333333333333333333")

    def close_spide(self, spider):
        """run with spider close"""
        logger.info("2222222222222222222222222222")
