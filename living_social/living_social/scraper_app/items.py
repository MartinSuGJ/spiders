from scrapy.item import Item, Field
from scrapy.contrib.loader.processor import Join, MapCompose, TakeFirst

def filter_price(value):
    value = value.strip()
    return value


class LivingSocialDeal(Item):
    """Livingsocial container (dictionary-like object) for scraped data"""
    title = Field(
        output_processor = TakeFirst(),
    )
    link = Field(
        output_processor = TakeFirst(),
    )
    location = Field(
        output_processor = TakeFirst(),
    )
    original_price = Field(
        input_processor = MapCompose(filter_price),
        output_processor = TakeFirst(),
    )
    price = Field(
        input_processor = MapCompose(filter_price),
        output_processor = TakeFirst(),
    )
    end_date = Field(
        output_processor = TakeFirst(),
    )
