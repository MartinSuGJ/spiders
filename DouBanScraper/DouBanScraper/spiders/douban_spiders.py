# -*- coding: utf-8 -*-

# Define here the spiders for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose, TakeFirst
from DouBanScraper.items import DoubanMovieItem
from scrapy import Request
import json
import re

class DoubanMovieSpider(BaseSpider):
    name = 'DoubanMovie'
    allowed_domains = ["https://movie.douban.com/"]

    def start_requests(self):
        urls = []
        for i in range(1, 32, 1):
            for j in range(100,0,-10):
                url = "https://movie.douban.com/j/chart/top_list?type=" + str(i) + '&interval_id=' + str(j) + '%3A' + str(j-10) + '&action=&start=0&limit=2000'
                urls.append(url)
                yield Request(url=url, callback=self.parse)


    def parse(self, response):
        movie_dict = json.loads(response.body)
        for movie in movie_dict:
            movie_item = DoubanMovieItem()
            match = re.search('.*type=(.*?)&.*', response.url)
            if match:
                movie_item['movie_type_id'] = match.group(1)
            else:
                movie_item['movie_type_id'] = '99'
            movie_item['movie_type'] = movie["types"]
            movie_item['movie_title'] = movie['title']
            movie_item['movie_url'] = movie["url"]
            movie_item['movie_cover_url'] = movie["cover_url"]
            movie_item['movie_rank'] = movie["rank"]
            movie_item['movie_id'] = movie["id"]
            movie_item['movie_region'] = movie["regions"]
            movie_item['movie_actors'] = movie["actors"]
            movie_item['movie_release_date'] = movie["release_date"]
            movie_item['movie_vote_count'] = movie["vote_count"]
            yield movie_item
