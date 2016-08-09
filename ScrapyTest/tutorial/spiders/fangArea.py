#coding:utf-8
import scrapy
import json
from tutorial.items import TiebaItem
import unicodedata
from scrapy.selector import Selector
from tutorial.spiders import fangDitrict
from __builtin__ import str
try:
    from scrapy.spider import Spider
except:
    from scrapy.spider import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle
import codecs
import MySQLdb

class FangSpider(scrapy.Spider):
    name = "fangArea"
    allowed_dmains = ["http://esf.sh.fang.com"]
    start_urls = ["http://esf.sh.fang.com/housing"]

    #rules = [
    #    Rule(sle(allow=("/p/4479212761\?pn=\d{,4}&ajax=1&t=1455292481894")), follow=True, callback='parse')
    #] 

    def parse(self,response):
        sel =  response.xpath("//div[contains(@class,'quxian')]")[0]
        #print sel
        href = sel.xpath("//div[contains(@class,'qxName')]/a/attribute::href").extract();
        #print href
        for i in range(1,len(href)):
            str = href[i]
            
            yield scrapy.Request('http://esf.sh.fang.com'+str, callback=self.parseDistrict)


    def parseDistrict(self,response):
        sel =  response.xpath("//div[contains(@class,'shangQuan')]//p[contains(@id,'shangQuancontain')]//a")
        #print sel
        if(len(sel)>0):
            sel = sel[0]
        #else:
            #print response
        href = sel.xpath("//div[contains(@class,'shangQuan')]//p[contains(@id,'shangQuancontain')]//a/attribute::href").extract()
        hreftext = sel.xpath("//div[contains(@class,'shangQuan')]//p[contains(@id,'shangQuancontain')]//a/text()").extract()
        #print len(href)
        #print hreftext
        for i in range(len(href)):
            file = codecs.open('url.txt', 'a', encoding='utf-8')
        
            line = href[i]
            file.write(line+ "\n")
            file.close()            
            yield scrapy.Request('http://esf.sh.fang.com'+href[i], callback=self.parseComunity)
            
    def parseComunity(self,response):
        #sel =  response.xpath("//div[contains(@class,'ml15')]//dd[2]/a[1]/attribute::href").extract()
        last = response.xpath("//div[contains(@class,'fanye')]//a[contains(@id,'PageControl1_hlk_last')]/attribute::href").extract()
        next = response.xpath("//div[contains(@class,'fanye')]//a[contains(@id,'PageControl1_hlk_next')]/attribute::href").extract()
        #print last
        #print next
        #if next != last:
        if len(next) >0:    
        #for i in range(len(sel)):
            #print sel[i]
            #str = sel[i]
            #print last
            file = codecs.open('url.txt', 'a', encoding='utf-8')
        
            line = next[0]#json.dumps(next[0], ensure_ascii=False) + "\n"
            file.write(line+ "\n")
            file.close()
            #scrapy.Request('http://esf.sh.fang.com'+next[0], callback=self.parseHouse)
            #yield scrapy.Request('http://esf.sh.fang.com'+next[0], callback=self.parseHouse)
            yield scrapy.Request('http://esf.sh.fang.com'+next[0], callback=self.parseComunity)
            #self.parseComunity(self,scrapy.Request('http://esf.sh.fang.com'+next[0], callback=self.parseComunity))
            #FangSpider.parseComunity(self,Response('http://esf.sh.fang.com'+next[0]))
            #parseComunity('http://esf.sh.fang.com'+next[0],)
            #print sel        
            
    def parseHouse(self,response):
        sel =  response.xpath("//div[contains(@class,'ml15')]//dd[2]/a[1]/attribute::href").extract()
        for i in range(len(sel)):
            #print sel[i]
            str = sel[i]
            #print str
            yield scrapy.Request('http://esf.sh.fang.com'+str, callback=self.parseHouseDetail)
        #print sel
        
    def parseHouseDetail(self,response):
        sel =  response.xpath("//dd[contains(@class,'info')]")[0]
        price = sel.xpath("//span[contains(@class,'price')]/text()").extract()
        #print price
        area = sel.xpath("//div[contains(@class,'area')]/p[1]/text()").extract()
        #print area
        addr = sel.xpath("//p[contains(@class,'mt10')]/a/span/text()").extract()
        #print addr
        length = min( len(price),len(area),len(addr))
        file = codecs.open('tencent.json', 'a', encoding='utf-8')
        for i in range(length):
            line = json.dumps(price[i], ensure_ascii=False) 
            file.write(line)
            line = json.dumps(area[i], ensure_ascii=False)
            file.write(line) 
            line = json.dumps(addr[i], ensure_ascii=False) + "\n"
            file.write(line)
        file.close()