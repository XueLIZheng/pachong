# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from SinaApp.optmysql import Sql

class SinaappPipeline(object):
    def process_item(self, item, spider):
        try:
            Sql.inster_table(item)
        except Exception as e:
            print(e.args)
        return item
    def close_spider(self):
        Sql.closemysql()
        pass
