# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapemeLive2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Name = scrapy.Field()
    Description = scrapy.Field()
    Price = scrapy.Field()
    Stock = scrapy.Field()
    SKU = scrapy.Field()
    Category = scrapy.Field()
    Tags = scrapy.Field()
