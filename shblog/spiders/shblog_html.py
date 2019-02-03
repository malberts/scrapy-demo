# -*- coding: utf-8 -*-
from .shblog_base import SHBlogBaseSpider


class SHBlogHtmlSpider(SHBlogBaseSpider):
    name = 'shblog_html'
    user_agent = 'shblog_html (+https://github.com/malberts/scrapy-demo/)'
    allowed_domains = ['blog.scrapinghub.com']
    start_urls = ['https://blog.scrapinghub.com/']

    def parse(self, response):
        """
        Parses a page with a list of blog post items.

        @url https://blog.scrapinghub.com/
        @returns items 0 0
        @returns requests 11 11
        """
        # Get the post links.
        post_links = response.css('.post-item a.more-link::attr(href)')
        for link in post_links:
            yield response.follow(link, callback=self.parse_post_item)

        # Get the link to older blog posts.
        older_link = response.css('a.next-posts-link::attr(href)').get()
        if older_link:
            yield response.follow(older_link, callback=self.parse)

    def parse_post_item(self, response):
        """
        Parses an individual blog post item.

        @url https://blog.scrapinghub.com/2010/06/26/hello-world
        @returns items 1 1
        @returns requests 0 0
        @scrapes title date author summary tags
        """
        yield from super().parse_post_item(response)
