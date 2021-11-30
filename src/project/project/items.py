# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    URL = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    robots = scrapy.Field()
    og_locale = scrapy.Field()
    og_type = scrapy.Field()
    og_title = scrapy.Field()
    og_description = scrapy.Field()
    og_url = scrapy.Field()
    og_site_name = scrapy.Field()
    og_image = scrapy.Field()
    pass