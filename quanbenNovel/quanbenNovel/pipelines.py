# -*- coding: utf-8 -*-
import os
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class QuanbennovelPipeline(object):
    def process_item(self, item, spider):
        dirPath = r'novels' + '\\' + item['categoryName'] + '\\' + item['bookName']
        filePath = dirPath + '\\' + item['chapterName'] + '.txt'
        if not os.path.exists(dirPath):
            os.makedirs(dirPath)
        with open(filePath, 'w', encoding='utf-8')as file:
            file.write(item['chapterContent'])
        return item
