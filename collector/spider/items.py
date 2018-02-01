# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class HotSpot(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    brief = scrapy.Field()
    read = scrapy.Field()
    comments = scrapy.Field()
    like = scrapy.Field()
