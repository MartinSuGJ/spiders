import sys
sys.path.append('/Users/guangjun/Desktop/scrapy/living_social/living_social')

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose, TakeFirst
from scraper_app.items import LivingSocialDeal

class LivingSocialSpider(BaseSpider):
    """Spider for regularly updated livingsocial.com site, San Francisco Page"""
    name = "livingsocial"
    allowed_domains = ["livingsocial.com"]
    start_urls = ["http://www.livingsocial.com/cities/15-san-francisco"]

    deals_list_xpath = '//li[@dealid]'
    item_fields = {
        'title': './/a/div[@class="deal-details"]/h2/text()',
        'link': './/a/@href',
        'location': './/a/div[@class="deal-details"]/p[@class="location"]/text()',
        'original_price': './/a/div[@class="deal-prices"]/div[@class="deal-strikethrough-price"]/div[@class="strikethrough-wrapper"]/text()',
        'price': './/a/div[@class="deal-prices"]/div[@class="deal-price"]/text()',
        'end_date': './/a/div[@class="deal-details"]/p[@class="dates"]/text()'
    }

    def parse(self, response):
        """
        Default callback used by Scrapy to process download response

        Testing contracts:
        @url http://www.livingsocial.com/cities/15-san-francisco
        @returns items 1
        @scrapes title link
        :param response:
        :return:
        """
        selector = HtmlXPathSelector(response)

        # iterate over deals
        for deal in selector.select(self.deals_list_xpath):

            loader = XPathItemLoader(LivingSocialDeal(), selector=deal)

            # define processors
            loader.default_input_processor = TakeFirst()
            loader.default_input_processor = MapCompose(unicode.strip)
            loader.default_input_processor = Join()
            loader.defalut_output_processor = TakeFirst()

            # iterate over fields and add xpaths to the loader
            for field, xpath in self.item_fields.iteritems():
                loader.add_xpath(field, xpath)
            yield loader.load_item()
