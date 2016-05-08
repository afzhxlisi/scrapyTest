import scrapy

from tutorial.items import TiebaItem

class TiebaSpider(scrapy.Spider):
    name = "tieba"
    allowed_dmains = ["tieba.baidu.com"]
    start_urls = ["http://http://tieba.baidu.com/p/4338882389?pn=1&ajax=1&t=1455292481894"]

    def parse(self,response):
        for sel in response.xpath('//ul/li'):
            item = TiebaItem()
            userid = sel.xpath('a/text()').extract()
            level = sel.xpath('a/@href').extract()
            content = sel.xpath('text()').extract()
            yield item
