# scrapy-demo

> When you're too busy scraping to read ScrapingHub's blog about scraping.

## What does it do?
It scrapes the blog entries on https://blog.scrapinghub.com and summarizes
the main content to demo various Scrapy features:
* [Plain HTML Spider](https://doc.scrapy.org/en/latest/topics/spiders.html#scrapy-spider)
* [Sitemap Spider](https://doc.scrapy.org/en/latest/topics/spiders.html#sitemapspider)
* [Item](https://doc.scrapy.org/en/latest/topics/items.html)
* [ItemLoader](https://doc.scrapy.org/en/latest/topics/loaders.html)
* [ItemLoader Processors](https://doc.scrapy.org/en/latest/topics/loaders.html#declaring-input-and-output-processors)
* [Pipelines](https://doc.scrapy.org/en/latest/topics/item-pipeline.html)
* [Contracts](https://doc.scrapy.org/en/latest/topics/contracts.html)
* [Basic shub integration](https://shub.readthedocs.io/en/stable/deploying.html)

## Requirements
* Python 3.6
* [requirements.txt](requirements.txt) for production
* [requirements-dev.txt](requirements-dev.txt) for development

## Running the spiders
There are 2 spiders in this demo. They do the same thing, except the one
scrapes the HTML landing page and the other one starts with the sitemap.

To use the HTML page scraper:

`scrapy crawl shblog_html`

To use the sitemap scraper:

`scrapy crawl shblog_sitemap`
