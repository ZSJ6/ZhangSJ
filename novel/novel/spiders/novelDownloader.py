import scrapy
import time


class NovelSpider(scrapy.Spider):
    name = 'novel'
    start_urls = ['https://www.quanben.net/']
    allowed_domains = ['www.quanben.net']
    custom_settings = {'LOG_LEVEL': 'DEBUG','LOG_FILE': '5688_log_%s.txt' % time.time(),"DEFAULT_REQUEST_HEADERS": {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        }
    }

    def parse(self, response):
        for book in response.css('item-img'):
            name = book.xpath('//h5/a').extract_first()
            book_url = book.xpath('//h5/a/@href').extract_first()
        print(name, book_url)