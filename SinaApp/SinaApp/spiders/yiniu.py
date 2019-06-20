# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from SinaApp.items import SinaappItem
'https://eniu.com/xuan?market%5B%5D=hsa'
class YinuispiderSpider(scrapy.Spider):
    name = 'yiniuSpider'
    allowed_domains = ['eniu.com']
    start_urls = ['https://eniu.com/xuan?market%5B%5D=hsa']
    def __init__(self):
        super(YinuispiderSpider,self).__init__(name='yiniuSpider')
        self.driver = webdriver.Chrome()
        pass

    def parse(self, response):
        info = response.xpath('//table[@id="table"]//tbody/tr')
        for item in info:
            a = item.xpath('.//td[1]/a/text()').extract_first()    # 代码
            b = item.xpath('.//td[2]/a/text()').extract_first()    # 名称
            c = item.xpath('.//td[3]/a/text()').extract_first()    # 市盈率
            d = item.xpath('.//td[4]/a/text()').extract_first()    #市净率
            e = item.xpath('.//td[5]/a/text()').extract_first()    # 股息率
            f = item.xpath('.//td[6]/a/text()').extract_first()    # 历史ROE
            g = item.xpath('.//td[7]/a/text()').extract_first()    #近三年ROE
            h = item.xpath('.//td[8]/a/text()').extract_first()    #近五年ROE
            i = item.xpath('.//td[9]/a/text()').extract_first()    #市值

            # # print(len(name))
            yield {
                '代码':a,
                '名称':b,
                '市盈率':c,
                '市净率':d,
                '股息率':e,
                '历史ROE':f,
                '近三年ROE':g,
                '近五年ROE':h,
                '市值':i
            }
            # print(no,name,a,b,c,d,e,f,g,h,i,j,k)
            # sina = SinaappItem()
            # sina['a']=no
            # sina['b'] = name
            # sina['c'] = a
            # sina['d'] = b
            # sina['e'] = c
            # sina['f'] = d
            # sina['g'] = e
            # sina['h'] = f
            # sina['i'] = g
            # sina['j'] = h
            # sina['k'] = i
            # sina['l'] = j
            # sina['m'] = k
            # yield sina

        pass
