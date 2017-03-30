# -*- coding: utf-8 -*-

# Scrapy settings for DouBanScraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'DouBanScraper'

SPIDER_MODULES = ['DouBanScraper.spiders']
NEWSPIDER_MODULE = 'DouBanScraper.spiders'

# Avoid being banned
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.54 Safari/536.5'

# seting where to save the data
SAVE_MOVIE_PATH = './Data/movie/'

# Database Setting
DATABASE = {
    'drivername': 'postgres',
    'host': 'localhost',
    'port': '5432',
    'username': 'guangjun',
    'password': '0',
    'database': 'douban'
}

ITEM_PIPELINES = {
    'DouBanScraper.pipelines.DoubanscraperPipeline' : 300
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'DouBanScraper (+http://www.yourdomain.com)'
