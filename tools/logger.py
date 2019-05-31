# -*- coding: utf-8 -*- 

__author__ = "Road36"
__date__ = "19-5-29"

"""
Describe:
日志模块
"""
import logging
from logging.handlers import TimedRotatingFileHandler
from logging import Formatter
PATH = '/home/ly/code/my_project/Crawler/'

numeric_level = getattr(logging, "INFO", None)
if not isinstance(numeric_level, int):
    raise ValueError('Invalid log level:%s' % "LOG_LEVEL")

formatter = Formatter('%(asctime)s|%(levelname)s|%(module)s|%(process)d|system|%(funcName)s||success||%(message)s|',
                      '%Y-%m-%d %H:%M:%S')
logging.basicConfig(level=numeric_level)
logger = logging.getLogger("Crawler")
timeRotatingHandler = TimedRotatingFileHandler(PATH + '%s.log' % "Crawler", when='midnight')
timeRotatingHandler.setFormatter(formatter)
timeRotatingHandler.suffix = "_%Y%m%d.log"
logger.addHandler(timeRotatingHandler)
