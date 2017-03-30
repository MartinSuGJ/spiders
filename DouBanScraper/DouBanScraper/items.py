# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
from scrapy.contrib.loader.processor import Join, MapCompose, TakeFirst


class DoubanMovieItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movie_type_id = Field()
    movie_type = Field()
    movie_title = Field()
    movie_url = Field()
    movie_cover_url = Field()
    movie_rank = Field()
    movie_id = Field()
    movie_region = Field()
    movie_actors = Field()
    movie_release_date = Field()
    movie_vote_count = Field()
