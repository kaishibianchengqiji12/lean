# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import logging

import requests
import scrapy
from scrapy import signals
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
import random
from scrapy.downloadermiddlewares.retry import RetryMiddleware
from scrapy.utils.response import response_status_message
import re
import urllib.request
import random
import time
class ZhwcizuSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ZhwcizuDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class MyUserAgentMiddleware(UserAgentMiddleware):
    '''
    设置User-Agent
    '''

    def __init__(self, user_agent):
        self.user_agent = user_agent

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            user_agent=crawler.settings.get('MY_USER_AGENT')
        )

    def process_request(self, request, spider):
        agent = random.choice(self.user_agent)
        request.headers['User-Agent'] = agent


# class TooManyRequestsRetryMiddleware(RetryMiddleware):
#
#     def __init__(self, crawler):
#         super(TooManyRequestsRetryMiddleware, self).__init__(crawler.settings)
#         self.crawler = crawler
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         return cls(crawler)
#
#     def process_response(self, request, response, spider):
#         if request.meta.get('dont_retry', False):
#             return response
#         elif response.status == 429:
#             self.crawler.engine.pause()
#             time.sleep(60)  # If the rate limit is renewed in a minute, put 60 seconds, and so on.
#             self.crawler.engine.unpause()
#             reason = response_status_message(response.status)
#             return self._retry(request, reason, spider) or response
#         elif response.status in self.retry_http_codes:
#             reason = response_status_message(response.status)
#             return self._retry(request, reason, spider) or response
#         return response
#


# class ProxyMiddleware(object):
#     def process_request(self, request, spider):
#         # url = "http://http.tiqu.qingjuhe.cn/getip?num=1&type=1&pack=49124&port=11&lb=1&pb=4&regions="
#
#         # response = requests.get(url)
#         list1 = ['58.218.214.134:17639', '59.58.59.94:4363', '58.218.92.30:14071', '58.218.214.148:16746', '113.128.26.251:4364', '58.218.214.137:18877', '58.218.92.78:14968', '223.241.55.216:4382', '58.218.92.68:16499', '58.218.214.149:14422', '58.218.214.132:12561', '182.244.123.156:4328', '114.99.9.169:4376', '115.208.42.71:4380', '58.218.214.147:18053', '60.160.81.149:4386', '58.218.214.139:17630', '58.218.214.151:17005', '58.218.92.87:13110', '110.82.149.196:4358', '223.215.175.91:4345', '58.218.92.89:19682', '58.218.92.79:13903', '58.217.55.228:4307', '114.230.67.171:4326', '58.218.92.76:19463',  '58.218.214.144:18733', '58.218.214.153:15422', '1.199.193.5:4351', '58.218.92.94:15929', '58.218.214.135:16817', '58.218.214.140:12654', '59.58.57.190:4335', '60.166.160.151:4327', '58.218.214.132:14665', '58.218.92.90:13918', '222.220.118.94:4331', '58.218.92.69:19629', '58.218.214.154:17764', '114.235.203.247:4343', '218.95.112.84:4313', '106.125.237.72:4345', '58.218.92.73:17844', '58.218.92.174:19866', '58.218.214.151:13645', '114.99.7.232:4375', '58.218.214.135:14275', '114.99.2.233:4335', '58.218.214.156:18842', '58.218.92.73:18633', '58.218.92.168:12304', '58.218.214.154:16074', '112.194.71.250:4378', '114.99.10.143:4375', '58.218.92.94:12677', '58.218.214.153:16596', '58.218.214.133:16154', '58.218.214.136:15722', '27.190.82.75:4382', '58.218.92.78:17957', '122.188.243.215:4354', '58.218.214.152:18019', '58.218.92.81:15571', '58.218.92.174:14029', '140.255.201.4:4326', '144.0.103.169:4313', '36.57.78.249:4327', '58.218.214.147:17303', '58.218.92.76:12116', '58.218.214.136:15006', '58.218.214.152:18574', '58.218.92.170:17053', '58.218.92.91:18976', '58.218.92.172:13163', '114.99.22.53:4332', '112.114.131.206:4328', '58.218.92.170:19566', '58.218.214.137:15938', '175.42.128.184:4354', '58.218.214.143:14271', '58.218.92.74:14773', '58.218.92.168:13540', '58.218.214.156:16332', '58.218.214.140:17289', '116.154.11.170:4351', '58.218.92.158:14556', '58.218.92.172:16338', '117.69.200.21:4352', '183.3.177.70:4305', '36.57.68.95:4327', '222.90.47.177:4375', '183.51.190.227:4387', '59.62.28.230:4336']
#
#         kk = random.choice(list1)
#         request.meta['proxy'] = 'https://' + kk
#         #print(response.text)




