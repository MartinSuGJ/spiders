# Scrapy settings for tutorial project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'livingsocial'

SPIDER_MODULES = ['scraper_app.spiders']

ITEM_PIPELINES = {
    'scraper_app.pipelines.LivingSocialPipeline': 300
    }

DATABASE = {
    'drivername': 'postgres',
    'host': 'localhost',
    'port': '5432',
    'username': 'guangjun',  # fill in your username here
    'password': '0',  # fill in your password here
    'database': 'scrape'
}
