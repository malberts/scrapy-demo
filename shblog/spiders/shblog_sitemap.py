# -*- coding: utf-8 -*-
from scrapy.spiders import SitemapSpider

from .shblog_base import SHBlogBaseSpider


class SHBlogSitemapSpider(SHBlogBaseSpider, SitemapSpider):
    name = 'shblog_sitemap'
    user_agent = 'shblog_sitemap (+https://github.com/malberts/scrapy-demo/)'
    allowed_domains = ['blog.scrapinghub.com']
    sitemap_urls = ['https://blog.scrapinghub.com/sitemap.xml']
    sitemap_rules = [
        ('', 'parse_post_item')
    ]

    def parse_post_item(self, response):
        """
        Parses an individual blog post item.

        @url https://blog.scrapinghub.com/2010/06/26/hello-world
        @returns items 1 1
        @returns requests 0 0
        @scrapes title date author summary tags
        """
        yield from super().parse_post_item(response)
