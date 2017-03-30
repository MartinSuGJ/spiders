# -*- coding: utf-8 -*-

# Define here the spiders for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose, TakeFirst
from AllMacWallpaperScraper.items import WallpaperItem
from scrapy import Request
import urllib
from AllMacWallpaperScraper import settings
import json
import re

class WallpaperSpider(BaseSpider):
    name = 'AllMacWallpaper'
    domain = 'http://www.allmacwallpaper.com'
    allowed_domains = ['allmacwallpaper.com']

    start_urls = ["http://www.allmacwallpaper.com/"]

    def parse(self, response):
        images = response.xpath('//div[@class="lists clearfix"]/dl/dt')
        for image in images:
            img_url = self.domain + image.xpath('.//a/@href').extract()[0]
            yield Request(img_url, callback = self.parse_image)

        next_page = self.domain + response.xpath('//div[@class="pageList"]/a[@class="next"]/@href').extract()[0]
        yield Request(next_page, callback=self.parse)

    def parse_image(self, response):
        wallpaper = WallpaperItem()
        save_dir = settings.SAVE_MOVIE_PATH
        file_url = response.xpath('//div[@class="downloadList"]')[2].xpath('.//a/@href').extract()[0]
        file_url = self.domain + file_url
        file_name = save_dir + re.search('.*wallpapers/(.*?)-2880', file_url).group(1) + '.jpg'
        wallpaper['image_urls'] = [file_url]
        wallpaper["iamge_name"] = re.search('.*wallpapers/(.*?)-2880', file_url).group(1)
        # urllib.urlretrieve(file_url, file_name)
        print 'Downloaded %s' % (file_name)
        yield wallpaper
