# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import dateparser

from scrapy.exceptions import DropItem


class SHBlogTitlePipeline(object):
    """
    Exclude items without a title, because they probably aren't blog posts.
    """
    def process_item(self, item, spider):
        if not item.get('title'):
            raise DropItem(f"Missing title in {item}")
        return item


class SHBlogDatePipeline(object):
    """
    Convert dates to Python dates and reformat.
    """
    def process_item(self, item, spider):
        item['date'] = dateparser.parse(item.get('date')).strftime('%Y-%m-%d')
        return item
