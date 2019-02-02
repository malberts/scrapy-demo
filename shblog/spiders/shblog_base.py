from scrapy import Spider

from ..items import SHBlogItem


class SHBlogBaseSpider(Spider):
    def parse_post_item(self, response):
        """Parses an individual blog post item."""
        yield SHBlogItem(
            url=response.url,
            title=response.css('#hs_cos_wrapper_name::text').get(),
            date=response.css('.byline .date a::text').get(),
            author=response.css('.byline .author a::text').get(),
            content=response.css('.post-body').get(),
        )
