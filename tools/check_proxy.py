# -*- coding: utf-8 -*- 

__author__ = "Road36"
__date__ = "19-5-31"

"""
Describe:
"""
import requests
from tools.common import logger


class CheckProxy:
    TEST_URL = 'http://www.baidu.com'
    TIMEOUT = 2

    def __init__(self):
        self.UseProxiesList = []
        self.InvalidProxiesList = []

    def is_valid_batch(self, proxys):
        """批量测试代理是否可用"""
        i = 1
        for proxy in proxys:
            logger.info('正在发送第 {0} 个请求。\n\r'.format(i))
            i += 1
            self.is_valid_batch(proxy)

        logger.info('InvalidProxiesList: {0}'.format(len(self.InvalidProxiesList)))
        logger.info('***已经有 {0} 个代理被淘汰***'.format(len(self.InvalidProxiesList)))
        logger.info('UseProxiesList: {0}'.format(self.UseProxiesList))
        logger.info('可用代理数量 {0}'.format(len(self.UseProxiesList)))

    def is_valid(self, proxy):
        proxies = {"http": "http://" + proxy, "https": "http://" + proxy, }
        try:
            requests.get(self.TEST_URL, proxies=proxies, timeout=self.TIMEOUT)
        except Exception as e:
            logger.error(repr(e))
            return False
        else:
            logger.info("it's works {0}".format(proxy))
            return True
