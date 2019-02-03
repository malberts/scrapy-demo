from scrapy import Spider

from ..items import SHBlogItem
from ..loaders import SHBlogItemLoader


class SHBlogBaseSpider(Spider):
    def parse_post_item(self, response):
        """Parses an individual blog post item."""
        loader = SHBlogItemLoader(item=SHBlogItem(), response=response)
        loader.add_value('url', response.url)
        loader.add_css('title', '#hs_cos_wrapper_name::text')
        loader.add_css('date', '.byline .date a::text')
        loader.add_css('author', '.byline .author a::text')
        loader.add_css('summary', '#hs_cos_wrapper_post_body ::text')
        loader.add_css('tags', '.post-topic .topic-link::text')
        yield loader.load_item()
