from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.linkextractors.regex import RegexLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule


class FallbackLinkExtractor(object):
    def __init__(self, extractors):
        self.extractors = extractors

    def extract_links(self, response):
        for lx in self.extractors:
            links = lx.extract_links(response)
            return links


class MySpider(CrawlSpider):
    name = 'example'

    rules = [Rule(FallbackLinkExtractor([
        LxmlLinkExtractor(),
        SgmlLinkExtractor(),
        RegexLinkExtractor(),
    ]), callback='parse_page', follow=True)]

    def parse_page(self, response):
        pass

    parse_start_url = parse_page
