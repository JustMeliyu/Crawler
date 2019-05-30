# -*- coding: utf-8 -*- 

__author__ = "Road36"
__date__ = "19-5-29"

"""
Describe:
通用模块, 一些常用方法
"""

from datetime import datetime, date, time
from functools import wraps
from tools.logger import logger
import json
import requests
import traceback


class APIEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, time):
            return obj.isoformat()
        '''
        elif isinstance(obj,ObjectId):
            return str(obj)
        '''
        return json.JSONEncoder.default(self, obj)


def max_connect(func):
    @wraps(func)
    def _max_connect(*args, **kwargs):
        _max = 5
        connect = 0
        e = None
        while connect < _max:
            try:
                func(*args, **kwargs)
            except Exception as e:
                logger.error(repr(e))
                connect += 1
                logger.error("connect is {0}".format(connect))
            else:
                break
        if connect == _max:
            logger.info(func.__name__)
            logger.info("finally error is {0}".format(repr(e)))
    return _max_connect


def get_func_time(func):
    @wraps(func)
    def _get_func_time(*args, **kwargs):
        now1 = datetime.now()
        result = func(*args, **kwargs)
        now2 = datetime.now()
        logger.info("func is {0}, time spending is {1}".format(func.__name__, (now2 - now1).total_seconds()))
        return result
    return _get_func_time


def request_sys(req_url, request_data, method, reqheaders):
    logger.info("request_data is {0}".format(request_data))
    logger.info("headers is {0}".format(reqheaders))
    try:
        if 'GET' == method:
            result = requests.get(url=req_url, params=request_data, headers=reqheaders)
            logger.info("res content is {0}".format(result))
            return json.loads(result)
        elif 'POST' == method:
            reqheaders['Accept'] = 'application/json'
            if reqheaders.get('Content-Type') == 'application/json':
                request_data = json.dumps(request_data, cls=APIEncoder)
            result = requests.post(url=req_url, data=request_data, headers=reqheaders).content
            logger.info("res content is {0}".format(result))
            return json.loads(result)
        else:
            logger.info("method error, current method is {0}".format(method))
    except Exception as e:
        logger.error('request_order_sys access error:%s' % (traceback.format_exc(e),))
    return None


def is_thread_finish(thread_pool):
    while True:
        for t in thread_pool:
            if not t.isAlive():
                # logger.info("t{0} is finished".format(t.getName()))
                thread_pool.pop(thread_pool.index(t))
        if not thread_pool:
            break
    logger.info("all thread finish")


def write_json_file(file_path, data):
    with open(file_path, 'w') as load_f:
        json.dump(data, load_f, ensure_ascii=False)


@get_func_time
def run_method(func, *args, **kwargs):
    logger.info("current func is {0}".format(func.__name__))
    result = func(*args, **kwargs)
    logger.info(result)
    return result


def strip(varchar):
    for v in range(len(varchar)):
        varchar[v] = varchar[v].strip() + "success"
    return varchar
