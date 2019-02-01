# -*- coding: utf-8 -*-
import scrapy


class SHBlogHtmlSpider(scrapy.Spider):
    name = 'shblog_html'
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
    
    def parse_post_item(self, response):
        """Parses an individual blog post item."""
        yield {
            'title': response.css('#hs_cos_wrapper_name::text').get(),
            'date': response.css('.byline .date a::text').get(),
            'author': response.css('.byline .author a::text').get(),
            'content': response.css('.post-body').get(),
        }
