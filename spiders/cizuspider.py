# -*- coding: utf-8 -*-
import scrapy
from ..items import ZhwcizuItem
import re


class CizuspiderSpider(scrapy.Spider):
    name = 'cizuspider'
    allowed_domains = ['zh.glosbe.com']
    #start_urls = ['https://zh.glosbe.com/zh/en/胆怯']

    def start_requests(self):
        with open(r"E:\xiangmu\zhwcizu\中文呢缺哈.txt", 'r', encoding="utf-8") as f:
            df = f.readlines()
            print(df)
            for line in df:
                line = re.sub(r"[\n]", "", line)
                start_url = 'https://zh.glosbe.com/zh/en/{}'.format(line)
                yield scrapy.Request(url=start_url, meta={"line": line})

    def parse(self, response):
        print(response.request.headers['User-Agent'])
        print(response.request.meta['proxy'])
        item = ZhwcizuItem()
        word = response.meta["line"]
        print(word)
        item["word_group"] = word
        #item["word_group"] = "aa"
        flag_element = response.xpath("//div[@id='phraseTranslation']/div")
        flag_t = flag_element.xpath("./h3/span[2]/span/@data-url-mp3").extract_first()
        if flag_t:
            item["chinese_voice"] = "https://zh.glosbe.com" + flag_element.xpath("./h3/span[2]/span/@data-url-mp3").extract_first()
        else:
            item["chinese_voice"] = ""
        list_li = flag_element.xpath("./ul/li")
        list1 = []
        if list_li:
            with open("cizuyoulizi40.txt", "a", encoding="utf-8") as f:
                f.write(word + "\n")
            for ind, i in enumerate(list_li):
                locals()['dict' + str(ind)] = dict()
                english_word = i.xpath("./div[@class='text-info']/strong[@class=' phr']/text()").extract_first()
                if english_word:
                    locals()['dict' + str(ind)]["english_word"] = english_word
                else:
                    locals()['dict' + str(ind)]["english_word"] = ""
                english_voice = i.xpath("./div[@class='text-info']/span[@class='audioPlayer-container']/span/@data-url-mp3").extract_first()
                if english_voice:
                    english_voice = "https://zh.glosbe.com" + english_voice
                    locals()['dict' + str(ind)]["english_voice"] = english_voice
                else:
                    locals()['dict' + str(ind)]["english_voice"] = ""
                word_property = i.xpath("./div[@class='text-info']/div[@class='gender-n-phrase']/text()").extract_first()
                if word_property is not None:
                    word_nature = re.findall(r"[a-zA-Z]+", word_property)
                    locals()['dict' + str(ind)]["word_property"] = word_nature[0]
                else:
                    locals()['dict' + str(ind)]["word_property"] = ""

                chinese_example = i.xpath("./div[@class='examples']/div[@class='row-fluid']/div[1]").xpath("string(.)").extract_first()
                if chinese_example is not None:
                    locals()['dict' + str(ind)]["chinese_example"] = chinese_example
                else:
                    locals()['dict' + str(ind)]["chinese_example"] = ""
                english_example = i.xpath("./div[@class='examples']/div[@class='row-fluid']/div[2]").xpath("string(.)").extract_first()
                if english_example is not None:
                    locals()['dict' + str(ind)]["english_example"] = english_example
                else:
                    locals()['dict' + str(ind)]["english_example"] = ""

                list1.append(locals()['dict' + str(ind)])
                # if english_word and word_property and english_voice is not None:
                #     word_nature = re.findall(r"[a-zA-Z]+", word_property)
                #     item["word_property"] = word_nature[0]
                #     english_voice = "https://zh.glosbe.com" + english_voice
                #     locals()['dict' + str(ind)]["word_property"] = word_nature[0]+"--"+english_word+"--"+english_voice
                #     print(english_word)
                #     print(locals()['dict' + str(ind)])
                #     list1.append(locals()['dict' + str(ind)])
                #
                # else:
                #     locals()['dict' + str(ind)]["word_property"]
                # pass

        if list1:
            item["all_example"] = list1
        else:
            item["all_example"] = ""
            with open("mcizuyoulizi40.txt", "a", encoding="utf-8") as f:
                f.write(word + "\n")
        print(item)
        yield item

