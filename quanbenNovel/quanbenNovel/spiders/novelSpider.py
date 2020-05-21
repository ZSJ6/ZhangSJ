import scrapy
from ..items import NovelItem

class NovelSpider(scrapy.Spider):
    name = 'quanben'
    start_urls = ['https://www.quanben.net/']
    allowed_domains = ['quanben.net']
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}

    def start_requests(self):
        yield scrapy.Request("https://www.quanben.net/", headers=self.headers)

    def parse(self, response):
        categorys = response.xpath('//*[@id="header"]/div[3]/ul/li')
        print(categorys)
        for category in categorys:
            categoryUrl = category.xpath('./a/@href').extract()[0]
            categoryUrl = 'https://www.quanben.net' + categoryUrl
            categoryName = category.xpath('./a/text()').extract()[0]
            print(categoryName, categoryUrl)
            yield scrapy.Request(categoryUrl, headers=self.headers, meta={"categoryName": categoryName},
                                 callback=self.getNext)

    def getNext(self, response):
        categoryName = response.meta["categoryName"]
        nextUrl = response.xpath("//a[@class='next']/@href").extract()[0]
        urls = response.xpath('//*[@id="content"]/div/div[2]/ul/li/span[2]/a/@href').extract()
        for url in urls:
            yield scrapy.Request('https://www.quanben.net' + url, headers=self.headers,
                                 meta={"categoryName": categoryName}, callback=self.getBooks)
        if not response.xpath("//a[@class='next']/@href").extract():
            pass
        else:
            yield scrapy.Request('https://www.quanben.net' + nextUrl, headers=self.headers,
                                 meta={"categoryName": categoryName}, callback=self.getNext)

    def getBooks(self, response):
        categoryName = response.meta["categoryName"]

        bookName = response.xpath('//*[@id="container"]/div[1]/div/h1/text()').extract()[0]
        chapters = response.xpath('//*[@id="main"]/div/dl/dd/a')
        for chapter in chapters:
            chapterName = chapter.xpath('./text()').extract()[0]
            chapterUrl = chapter.xpath('./@href').extract()[0]
            yield scrapy.Request('https://www.quanben.net'+chapterUrl, headers=self.headers,meta={'bookName': bookName, 'categoryName': categoryName, 'chapterName': chapterName},callback=self.getContent)

    def getContent(self, response):
        categoryName = response.meta['categoryName']
        bookName = response.meta['bookName']
        chapterName = response.meta['chapterName']
        chapterContent = ''.join(response.xpath('//*[@id="BookText"]/text()').extract())

        item = NovelItem()
        item['categoryName'] = categoryName
        item['bookName'] = bookName
        item['chapterName'] = chapterName
        item['chapterContent'] = chapterContent

        return item
