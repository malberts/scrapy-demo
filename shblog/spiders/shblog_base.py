from scrapy import Spider
from scrapy.loader import ItemLoader

from ..items import SHBlogItem


class SHBlogBaseSpider(Spider):
    def parse_post_item(self, response):
        """Parses an individual blog post item."""
        loader = ItemLoader(item=SHBlogItem(), response=response)
        loader.add_value('url', response.url)
        loader.add_css('title', '#hs_cos_wrapper_name::text')
        loader.add_css('date', '.byline .date a::text')
        loader.add_css('author', '.byline .author a::text')
        loader.add_css('content', '#hs_cos_wrapper_post_body')
        yield loader.load_item()
