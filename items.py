# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhwcizuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    word_group = scrapy.Field()
    chinese_voice = scrapy.Field()
    english_word = scrapy.Field()
    english_voice = scrapy.Field()
    word_property = scrapy.Field()  # 词组词性
    all_example = scrapy.Field()  # 词组所有列子
    chinese_example = scrapy.Field()  # 中文列子
    english_example = scrapy.Field()  # 英文例子
