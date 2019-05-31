# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#
from scrapy.exceptions import DropItem
from tools.logger import logger
from tools.check_proxy import CheckProxy


class DoubanPipeline(object):
    # @classmethod
    # def from_settings(cls, settings):
    #     """一般用于获取setting中的信息"""
    #     logger.info("=============================="*3)

    def process_item(self, item, spider):
        logger.info("current spider is {0}".format(spider.name))
        ai = item['auth_info'].rsplit("/", 3)
        item['auth_name'] = ai[0].strip()
        item['press'] = ai[1].strip()
        item['publication_date'] = ai[2].strip()
        item['price'] = ai[3].strip()
        logger.info("-----------------------{0}".format(item['person_num']))
        del item['auth_info']
        return item

    def open_spide(self, spider):
        """run with spider open"""
        logger.info("3333333333333333333333333333")

    def close_spide(self, spider):
        """run with spider close"""
        logger.info("2222222222222222222222222222")


class ProxyPipeline(object):
    # @classmethod
    # def from_settings(cls, settings):
    #     """一般用于获取setting中的信息"""
    #     logger.info("=============================="*3)
    def __init__(self):
        # self.LEVEL = "高匿名"
        self.LEVEL = "透明"

    def process_item(self, item, spider):
        logger.info("current spider is {0}".format(spider.name))
        if item['level'] != self.LEVEL:
            logger.error("LevelError. current ip {0} level is {1}".format(item['ip'], item['level']))
            raise DropItem

        if float(item['speed']) > 2:
            logger.error("SpeedError. current ip {0} contect time {1} is too long {1}".format(item['ip'], item['speed']))
            raise DropItem

        cp = CheckProxy()
        if not cp.is_valid(item['ip'] + item['port']):
            logger.error("ConnectError. current ip {0} is invalid".format(item['ip']))
            raise DropItem
        logger.info("SUCCESS")
        return item

    def open_spide(self, spider):
        """run with spider open"""
        logger.info("3333333333333333333333333333")

    def close_spide(self, spider):
        """run with spider close"""
        logger.info("2222222222222222222222222222")
