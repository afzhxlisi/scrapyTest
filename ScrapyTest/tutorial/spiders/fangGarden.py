#coding:utf-8
import scrapy
import json
from tutorial.items import TiebaItem
import unicodedata
from scrapy.selector import Selector
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
    name = "fangGarden"
    allowed_dmains = ["http://esf.sh.fang.com"]
    start_urls = ["http://esf.sh.fang.com/housing"]

    
    def start_requests(self):
        file = codecs.open('url.txt', 'r', encoding='utf-8')
        lines = file.readlines()
        self.start_urls =lines
        for url in self.start_urls:
            #print url
            yield self.make_requests_from_url("http://esf.sh.fang.com"+url)
    
    #rules = [
    #    Rule(sle(allow=("/p/4479212761\?pn=\d{,4}&ajax=1&t=1455292481894")), follow=True, callback='parse')
    #] 

    def parse(self,response):
        sel =  response.xpath("//div[contains(@class,'ml15')]//dd[2]/a[1]/attribute::href").extract()
        for i in range(len(sel)):
            #print sel[i]
            str = sel[i]
            #print str
            file = codecs.open('garden.txt', 'a', encoding='utf-8')
        
            line = str#json.dumps(next[0], ensure_ascii=False) + "\n"
            file.write(line+ "\n")
            file.close()
            yield scrapy.Request('http://esf.sh.fang.com'+next[0], callback=self.parseNextGarden)
         
         #items = [];
         #for 
        #last = response.xpath("//div[contains(@class,'fanye')]//a[contains(@id,'PageControl1_hlk_last')]/attribute::href").extract()
        #next = response.xpath("//div[contains(@class,'fanye')]//a[contains(@id,'PageControl1_hlk_next')]/attribute::href").extract()
        #print last
        #print next
        #if next != last:
        #if len(next) >0:    
        #for i in range(len(sel)):
            #print sel[i]
            #str = sel[i]
            #print next[0]
            '''file = codecs.open('url.txt', 'a', encoding='utf-8')
        
            line = next[0]#json.dumps(next[0], ensure_ascii=False) + "\n"
            file.write(line+ "\n")
            file.close()'''
            #yield scrapy.Request('http://esf.sh.fang.com'+next[0], callback=self.parseNextGarden)
            #yield scrapy.Request('http://esf.sh.fang.com'+next[0], callback=self.parseHouse)


                #sel =  response.xpath("//div[contains(@class,'quxian')]")[0]
                #print sel
                #href = sel.xpath("//div[contains(@class,'qxName')]//a/attribute::href").extract();
                #print href
                #hrefText = sel.xpath("//div[contains(@class,'content')]//a/text()").extract();
                #print hrefText
                #info =  response.xpath("//dd[contains(@class,'info')]")[0]
                #househref = info.xpath("//p[contains(@class,'mt10')][not(contains(@class,'gray6'))]//a/attribute::href").extract()
                #print househref
                #print(len(househref))
                
    	    #str1 = unicode.encode(str,'utf-8');
    		#item['content'] = "abc"+str1;
                #print url
    	    #print item
                #print item['userId']#=item['userId'].decode()
                #str=json.dumps(dict(item),ensure_ascii=False)+"\n";
                #str=unicode.encode(str,'utf-8');
                #print str
    	    #print item['content']
    	    #return items
                #yield scrapy.Request('http://tieba.baidu.com'+item['content']+'&ajax=1&t=1455292481894', callback=self.parse)
    	    #items.append(item)
                #print len(item);
                
    		#print items
    		#yield scrapy.Request('http://tieba.baidu.com'+str+'&ajax=1&t=1455292481894', callback=self.parse)
    		#print items > a.txt           
    	 #return items
                #if(None!=str):
                 #   yield scrapy.Request('http://esf.sh.fang.com'+str, callback=self.parse)
                 
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
            '''file = codecs.open('url.txt', 'a', encoding='utf-8')
        
            line = next[0]#json.dumps(next[0], ensure_ascii=False) + "\n"
            file.write(line+ "\n")
            file.close()'''
            #scrapy.Request('http://esf.sh.fang.com'+next[0], callback=self.parseHouse)
            yield scrapy.Request('http://esf.sh.fang.com'+next[0], callback=self.parseHouse)
            #yield scrapy.Request('http://esf.sh.fang.com'+next[0], callback=self.parseComunity)
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
            yield scrapy.Request('http://esf.sh.fang.com'+str, callback=self.parseNextHouse)
        #print sel
    
    def parseNextGarden(self,response):
        last = response.xpath("//div[contains(@class,'fanye')]//a[contains(@id,'PageControl1_hlk_last')]/attribute::href").extract()
        next = response.xpath("//div[contains(@class,'fanye')]//a[contains(@id,'PageControl1_hlk_next')]/attribute::href").extract()
        
        sel =  response.xpath("//div[contains(@class,'ml15')]//dd[2]/a[1]/attribute::href").extract()
        for i in range(len(sel)):
            #print sel[i]
            str = sel[i]
            #print str
            file = codecs.open('garden.txt', 'a', encoding='utf-8')
        
            line = str#json.dumps(next[0], ensure_ascii=False) + "\n"
            file.write(line+ "\n")
            file.close()
        
        #print last
        #print next
        #if next != last:
        if len(next) >0:    
        #for i in range(len(sel)):
            #print sel[i]
            #str = sel[i]
            #print last
            #print next[0]
            file = codecs.open('garden.txt', 'a', encoding='utf-8')
            
            line = next[0]#json.dumps(next[0], ensure_ascii=False) + "\n"
            file.writelines(line)
            file.close()
            yield scrapy.Request('http://esf.sh.fang.com'+next[0], callback=self.parseNextGarden)
            #yield scrapy.Request('http://esf.sh.fang.com'+str, callback=self.parseHouseDetail)
            #yield scrapy.Request('http://esf.sh.fang.com'+line, callback=self.parseHouse)
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