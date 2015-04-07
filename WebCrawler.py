__author__ = 'aferraz'

from scrapy import Spider, Item, Field

from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import log, signals
#from testspiders.spiders.followall import FollowAllSpider
from scrapy.utils.project import get_project_settings
from scrapy.exceptions import DropItem


class Post(Item):
    title = Field()

class BlogSpider(Spider):
    name, start_urls = 'blogspider', ['http://blog.scrapinghub.com']

    def parse(self, response):
        return [Post(title=e.extract()) for e in response.css("h2 a::text")]

items = []
def add_item(item):
    items.append(item)

spider = BlogSpider()
settings = get_project_settings()
crawler = Crawler(settings)
crawler.signals.connect(add_item, signals.item_passed)
crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
crawler.configure()
crawler.crawl(spider)
crawler.start()
#log.start(loglevel=log.DEBUG)
reactor.run()

print items
