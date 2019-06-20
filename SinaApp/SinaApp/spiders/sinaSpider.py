# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from SinaApp.items import SinaappItem
'https://eniu.com/xuan?market%5B%5D=hsa'
class SinaspiderSpider(scrapy.Spider):
    name = 'sinaSpider'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://vip.stock.finance.sina.com.cn/mkt/#sz_a',
                  'http://vip.stock.finance.sina.com.cn/mkt/#sz_b',
                  'http://vip.stock.finance.sina.com.cn/mkt/#sh_a',
                  'http://vip.stock.finance.sina.com.cn/mkt/#sh_b',
                  'http://vip.stock.finance.sina.com.cn/mkt/#hs_a',
                  'http://vip.stock.finance.sina.com.cn/mkt/#hs_b'

                  ]
    def __init__(self):
        super(SinaspiderSpider,self).__init__(name='sinaSpider')
        self.driver = webdriver.Chrome() 
        pass

    def parse(self, response):
        info = response.xpath('//div[@id="tbl_wrap"]//tbody/tr')
        for item in info:
            no = item.xpath('.//th[@class="sort_down"]/a/text()').extract_first()
            name = item.xpath('.//th[2]/a/text()').extract_first()
            a = item.xpath('.//td[1]/text()').extract_first()    # 最新价
            b = item.xpath('.//td[2]/text()').extract_first()    # 涨跌额
            c = item.xpath('.//td[3]/text()').extract_first()    # 涨跌幅
            d = item.xpath('.//td[4]/text()').extract_first()    #买入
            e = item.xpath('.//td[5]/text()').extract_first()    #卖出
            f = item.xpath('.//td[6]/text()').extract_first()    # 昨收
            g = item.xpath('.//td[7]/text()').extract_first()    #今开
            h = item.xpath('.//td[8]/text()').extract_first()    #最高
            i = item.xpath('.//td[9]/text()').extract_first()    #最低
            j = item.xpath('.//td[10]/text()').extract_first()   #成交量
            k = item.xpath('.//td[11]/text()').extract_first()   #成交额
            # # print(len(name))
            # yield {
            #     '编号':no,
            #     '名字':name,
            #     '最新价':a,
            #     '涨跌额':b,
            #     '涨跌幅':c,
            #     '买入':d,
            #     '卖出':e,
            #     '昨收':f,
            #     '今开':g,
            #     '最高':h,
            #     '最低':i,
            #     '成交量':j,
            #     '成交额':k
            # }
            print(no,name,a,b,c,d,e,f,g,h,i,j,k)
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
