# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy import Request
from Work.items import WorkItem
import time
import json
import re
reg = re.compile('\d+')

class WorkSpider(CrawlSpider):
    name = 'jingdong'
    allowed_domains = ['item.jd.com','p.3.cn']
    start_urls = ['https://search.jd.com/Search?keyword=%E7%89%9B%E4%BB%94%E8%A3%A4%E7%94%B7&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&page=1']

    rules = (
        Rule(LinkExtractor(allow=('\d+.html'),unique=True),
             follow=True,
             callback='parse_item',
             # process_links='process_links',
             ),
    )
    obj = WorkItem()
    @staticmethod
    def parse_item(response):  # 二级页面的解析
        time.sleep(2)
        try:
            # 解析数据
            name = response.xpath('//div[@class="mt"]/h3/a/@title').extract_first()
            shop_name = response.xpath('//div[@class="sku-name"]/text()').extract_first().strip()
            price = response.xpath('//span[@class="p-price"]/span[2]/text()').extract_first()
            parse = response.xpath('//ul[@class="parameter2 p-parameter-list"]/li/text()').extract_first()
            ID = response.xpath('//ul[@class="parameter2 p-parameter-list"]/li[2]/text()').extract_first()
            id = reg.findall(ID)
            s_img = response.xpath( '//*[@id="choose-attr-1"]/div[2]/div[2]/a/img/@src').extract_first()

            # WorkSpider.obj['name'] = response.xpath('//div[@class="mt"]/h3/a/@title').extract_first()
            # WorkSpider.obj['shop_name'] = response.xpath('//div[@class="sku-name"]/text()').extract_first().strip()
            # price = response.xpath('//span[@class="p-price"]/span[2]/text()').extract_first()
            # WorkSpider.obj['parse'] = response.xpath('//ul[@class="parameter2 p-parameter-list"]/li/text()').extract_first()
            # ID = response.xpath('//ul[@class="parameter2 p-parameter-list"]/li[2]/text()').extract_first()
            # id= reg.findall(ID)
            # WorkSpider.obj['s_img'] = response.xpath('//*[@id="choose-attr-1"]/div[2]/div[2]/a/img/@src').extract_first()
            print(name,shop_name,price,parse,s_img,ID )
            # print(s_img)
            # print('https://p.3.cn/prices/mgets?skuIds=J_'+id[0])
            # yield Request('http://p.3.cn/prices/mgets?skuIds=J_'+id[0],callback=WorkSpider.get_price)
            pass
        except  Exception as ex:
            print(ex.args)
        pass

    @staticmethod
    def get_price(response):
        # s_price= json.loads(response.text)[0]['p']
        WorkSpider.obj['s_price'] = json.loads(response.text)[0]['p']
        # print(s_price)
        yield WorkSpider.obj


        pass
