# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
import chromDriver_options
import os

def get_track(distance,t):
    track = []
    current = 0
    #mid = distance * t / (t+1)
    mid = distance * 3 / 4
    #print(mid)
    v = 6.8
    while current < distance:
        if current < mid:
            a = 2
        else:
            a = -3
        v0 = v
        v = v0 + a * t
        move = v0 * t + 1/2 * a * t * t
        current += move
        #print(current)
        track.append(round(move))
    return track


class SeleniumMiddleware:
    
    def __init__(self):
        self.browser = chromDriver_options.WebDriver().driver_instance
        self.browser.maximize_window() 

    @classmethod
    def from_crawler(cls, crawler):  # 关闭浏览器
        s = cls()
        crawler.signals.connect(s.spider_closed, signal=signals.spider_closed)
        return s