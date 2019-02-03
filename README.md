# scrapy-demo

> When you're too busy scraping to read ScrapingHub's blog about scraping.

## What does it do?
It scrapes the blog entries on https://blog.scrapinghub.com and summarizes
the main content to demo various Scrapy features:
* Plain HTML and Sitemap Spiders
* Item
* ItemLoader
* ItemLoader Processors
* Pipelines
* Contracts
* Basic ScrapingHub integration

## Requirements
* Python 3.6
* [requirements.txt](requirements.txt) for production
* [requirements-dev.txt](requirements-dev.txt) for development

## Running
To use the HTML page scraper:
`scrapy crawl shbot_html`

To use the sitemap scraper:
`scrapy crawl shbot_sitemap`
