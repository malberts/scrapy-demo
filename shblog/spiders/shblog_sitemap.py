# -*- coding: utf-8 -*-
from scrapy.spiders import SitemapSpider

from .shblog_base import SHBlogBaseSpider


class SHBlogSitemapSpider(SHBlogBaseSpider, SitemapSpider):
    name = 'shblog_sitemap'
    user_agent = 'shblog_sitemap (+https://github.com/malberts/scrapy-demo/)'
    allowed_domains = ['blog.scrapinghub.com']
    sitemap_urls = ['https://blog.scrapinghub.com/sitemap.xml']
    sitemap_rules = [
        # Require at least one character in the URL in order to exclude the homepage.
        ('blog.scrapinghub.com/.+', 'parse_post_item')
    ]
