# -*- coding: utf-8 -*- 

__author__ = "Road36"
__date__ = "19-5-29"

"""
Describe:
"""

import requests
from Crawler.config.config import IPPOOLS


class GetUseProxies:

    def __init__(self):
        self.UseProxiesList = []
        self.InvalidProxiesList = []

    def check_proxy(self):
        """测试代理是否可用"""
        i = 1
        for proxy in IPPOOLS:
            print('正在发送第%s个请求。\n\r' % i)
            i += 1
            proxies = {"http": "http://" + proxy, "https": "http://" + proxy, }
            try:
                requests.get('http://www.baidu.com', proxies=proxies, timeout=2)
                self.UseProxiesList.append(proxy)
            except Exception as e:
                print(repr(e))
                self.InvalidProxiesList.append(proxy)

        print('InvalidProxiesList: {0}'.format(len(self.InvalidProxiesList)))
        print('***已经有 {0} 个代理被淘汰***'.format(len(self.InvalidProxiesList)))
        print('UseProxiesList:', self.UseProxiesList)
        print('可用代理数量 {0}'.format(len(self.UseProxiesList)))


if __name__ == "__main__":
    s = GetUseProxies()
    s.check_proxy()

