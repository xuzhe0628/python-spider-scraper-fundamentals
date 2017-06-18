# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

class MoviePipeline(object):
    # action that will be taken when the crawler started
    def open_spider(self, spider):
        # connect to local mongodb on port 27018, default port is 27017
        self.client = pymongo.MongoClient("mongodb://localhost:27018")
        # connect to database test
        self.test = self.client['test']
        # connect to collection Movie
        self.movie = self.test['Movie']
    
    def process_item(self, item, spider):
        # insert the item to mongodb
        self.movie.insert_one(item)
        return item

    def close_spider(self, spider):
        pass