import scrapy
from redditScraper.items import RedditScraperItem

# pylint: disable=print-statement

class RedditSpider(scrapy.Spider):
    name = 'reddit_spider'

    def start_requests(self):
        urls = ['https://www.reddit.com/r/worldnews/']
        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)

    def parse(self, response):
        
        # Title of artile
        titles = response.xpath('//div[2]/div/p[1]/a/text()').extract()
        # Url of artile
        urls = response.xpath('//div[2]/div/p[1]/a/@href').extract()        
        # Name of source
        sources = response.xpath('//div[2]/div/p[1]/span/a/text()').extract()
        # Time posted on Reddit
        times = response.xpath('//div[2]/div/p[2]/time/@title').extract()

        # Making Reddit Scraper Item
        item = RedditScraperItem()
        for i, title in enumerate(titles):
            item['title'] = title
            item['url'] = urls[i]
            item['source'] = sources[i]
            item['time'] = times[i]
            yield item