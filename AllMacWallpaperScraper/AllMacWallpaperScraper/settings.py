# -*- coding: utf-8 -*-

# Scrapy settings for AllMacWallpaperScraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'AllMacWallpaperScraper'

SPIDER_MODULES = ['AllMacWallpaperScraper.spiders']
NEWSPIDER_MODULE = 'AllMacWallpaperScraper.spiders'

# Avoid being banned
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.54 Safari/536.5'

# seting where to save the data
SAVE_MOVIE_PATH = '/Users/guangjun/Desktop/Guangjun/Wallpapers/'


ITEM_PIPELINES = {
    'scrapy.contrib.pipeline.images.ImagesPipeline': 1
}

IMAGES_STORE = '/Users/guangjun/Desktop/Guangjun/Wallpapers/' #用来存储下载的图片
IMAGES_EXPIRES = 90        # 90天的图片失效期限
IMAGES_MIN_HEIGHT = 100    # 图片的最小高度
IMAGES_MIN_WIDTH = 100     # 图片的最小宽度

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'AllMacWallpaperScraper (+http://www.yourdomain.com)'
