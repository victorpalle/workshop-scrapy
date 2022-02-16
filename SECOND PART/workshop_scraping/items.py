##
## EPITECH PROJECT, 2022
## workshop-scrapy
## File description:
## items
##

import scrapy

class Product(scrapy.Item):
    name = scrapy.Field()
    description = scrapy.Field()
    id = scrapy.Field()
    current_url = scrapy.Field()
    image = scrapy.Field()
    detail_link = scrapy.Field()
    price = scrapy.Field()
    availibity = scrapy.Field()
    flag = scrapy.Field()
    last_updated = scrapy.Field(serializer=str)