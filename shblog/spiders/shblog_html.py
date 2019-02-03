# -*- coding: utf-8 -*-
from .shblog_base import SHBlogBaseSpider


class SHBlogHtmlSpider(SHBlogBaseSpider):
    name = 'shblog_html'
    user_agent = 'shblog_html (+https://github.com/malberts/scrapy-demo/)'
    allowed_domains = ['blog.scrapinghub.com']
    start_urls = ['https://blog.scrapinghub.com/']

    def parse(self, response):
        """Parses a page with blog post items."""
        # Get the post links.
        post_links = response.css('.post-item a.more-link::attr(href)')
        for link in post_links:
            yield response.follow(link, callback=self.parse_post_item)

        # Get the link to older blog posts.
        older_link = response.css('a.next-posts-link::attr(href)').get()
        if older_link:
            yield response.follow(older_link, callback=self.parse)
