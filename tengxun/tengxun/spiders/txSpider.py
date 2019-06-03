# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy import Request
import time

class TxspiderSpider(CrawlSpider):
    name = 'txSpider'
    allowed_domains = ['ke.qq.com']
    start_urls = ['https://ke.qq.com/course/list?mt=1001&price_min=0&price_max=0']

    'https: // ke.qq.com / course / list?page = 2'
    rules = (
        Rule(LinkExtractor(allow=('\&page=\d+',),unique=True), # 匹配页数
            follow=True,
            # callback='test',
            # process_links='process_links',
        ),
        Rule(LinkExtractor(allow=('/course/\d+',), unique=True),  # 匹配二级页面
             follow=True,
             callback='test',

             ),
    )



    @staticmethod
    def test(response):  # 解析二级页面
        name = response.xpath('//div[@class="course-title"]/h3/text()').extract_first() # 课程名称
       
        learn = response.xpath('//div[@class="course-hints"]/span[1]/span/text()').extract_first()  # 最近在学
        join = response.xpath('//div[@class="course-hints"]/span[2]/span/text()') .extract_first() # 累计报名
        good = response.xpath('//span[@class="hint-data"]/span/text()').extract_first()  # 好评

        if good is None:
            good = response.xpath('//div[@class="course-hints"]/span[3]/span/text()').extract_first().strip()
        yield {
            '课程名称': name,
            '最近在学': learn,
            '累计报名': join,
            '好评': good
        }
        pass
        # '//div[@class="tt-cover-name"]/a/@title'  #教育机构名字
        # '//ul[@class="tree-list"]/li[1]//span/text()' #好评
        # '//ul[@class="tree-list"]/li[2]//span/text()'#课程数
        # '//ul[@class="tree-list"]/li[2]//span/text()' # 学习人数
        # comment = response.xpath('//h2[@class="tabs-tt"]/span[@class="num js-comment-total"]/text()').extract_first() #评论数量

       

