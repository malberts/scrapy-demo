from scrapy.loader import ItemLoader
from scrapy.loader.processors import (
    Compose,
    Join,
    TakeFirst,
)
from summa.summarizer import summarize


class Strip(object):
    """
    Removes blank and non-blank whitespace lines from a list.
    """

    def __init__(self, strip_whitespace=True):
        self.strip_whitespace = strip_whitespace

    def __call__(self, values):
        if self.strip_whitespace:
            return [value for value in values if value.strip()]
        else:
            return [value for value in values if value != '']


class Summarize(object):
    """
    Summarizes a field using the summa library.
    """

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __call__(self, value):
        return summarize(value, *self.args, **self.kwargs)


class SHBlogItemLoader(ItemLoader):
    """
    ItemLoader for SHBLogItem.
    """
    summary_in = Compose(
        Strip(),
        Join(),
        Summarize(words=75)
    )
    date_out = TakeFirst()
