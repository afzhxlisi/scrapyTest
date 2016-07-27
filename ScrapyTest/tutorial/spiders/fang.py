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
    name = "fang"
    allowed_dmains = ["http://esf.sh.fang.com"]
    start_urls = ["http://esf.sh.fang.com/house-a025-b05235/kw%c6%d6%b6%ab%b6%fe%ca%d6%b7%bf/"]

    #rules = [
    #    Rule(sle(allow=("/p/4479212761\?pn=\d{,4}&ajax=1&t=1455292481894")), follow=True, callback='parse')
    #] 

    def parse(self,response):
         #items = [];
         #for 

                sel =  response.xpath("//dd[contains(@class,'info')]")[0]
                item = TiebaItem()
                item['userId'] = sel.xpath("//span[contains(@class,'price')]/text()").extract()
                print item['userId']
                item['level'] = sel.xpath("//div[contains(@class,'area')]/p[1]/text()").extract()
                print item['level']
                item['content'] = sel.xpath("//p[contains(@class,'mt10')]/a/span/text()").extract()
                print item['content']
                item['page'] = sel.xpath("//div[contains(@class,'fanye')]/a[contains(@class,'pageNow')]/text()").extract()
                links = sel.xpath("//div[contains(@class,'fanye')]/text()").extract()
                print item['page']
                str = None
                if(len(links)>0):
                    str =links[0]
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
                file = codecs.open('tencent.json', 'a', encoding='utf-8')
                line = json.dumps(dict(item), ensure_ascii=False) + "\n"
                file.write(line)
                file.close()
                '''try:
                    conn=MySQLdb.connect(host='localhost',user='root',passwd='wang',db='test',port=3306,charset='utf8')
                    cur=conn.cursor()
                    cur.execute('select ifnull(max(id),0) id from tieba')
                    result=cur.fetchone()
                    idN = result[0]+1
                    length = len(item['userId'])
                    #print length 
                    #print idlength 
                    #print len(item['content'])
                    values=[]
                    insertStr =''
                    contentIndex =0
                    for i in range(length):
                        #o = str(i)+'_'+str(contentIndex)
                        #print i
                        #print contentIndex
                        while(item['content'][contentIndex].isspace()):
                            contentIndex=contentIndex+1
                        #print str(i)+str(contentIndex)
                        values.append((idN+i,item['userId'][i],item['content'][contentIndex]))
                        #print item['content'][contentIndex]
                        contentIndex=contentIndex+1
                        
                        #print idN+i
                        #print item['userId']
                        #print item['content']
                        #values.append(item['userId'][i])
                        #values.append(item['level'][i])
                        #values.append(item['content'][i].encode("utf-8") )
                        #contentStr = item['content'][i]
                        #print contentStr
                        #values.append(contentStr)
                        #values.append(.decode('unicode_escape'))
                        
                        insertStr+='(%s,%s,%s),'
                    insertStr = insertStr[0:len(insertStr)-1]
                    #values.append((1,'糯米','糯米'))
                    #print insertStr
                    #print values
                    #insertVal = [];
                    #insertVal.append(('1','1','1'))
                    #insertVal.append(values[0])
                    #insertVal.append(values[1])
                    #insertVal.append(values[2])
                    #insertVal.append(values[3])
                    #cur.executemany('insert into test values'+insertStr,values)
                    #print values
                    cur.executemany('insert into tieba(id,userId,content) values  (%s,%s,%s)',values)
                    conn.commit()
                    cur.close()
                    
                    conn.close()
                except MySQLdb.Error,e:
                     print "Mysql Error %d: %s" % (e.args[0], e.args[1])
                #MySQLdb.connect("")
                '''
    		#print items
    		#yield scrapy.Request('http://tieba.baidu.com'+str+'&ajax=1&t=1455292481894', callback=self.parse)
    		#print items > a.txt           
    	 #return items
                if(None!=str):
                    yield scrapy.Request('http://tieba.baidu.com'+str+'&ajax=1&t=1455292481894', callback=self.parse)
