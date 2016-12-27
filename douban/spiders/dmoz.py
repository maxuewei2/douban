#coding:utf-8
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from douban.items import DItem


class DoubanSpider(CrawlSpider):
    name = "douban"
    allowed_domains = ["douban.com"]
    start_urls = [
        "https://www.douban.com/people/oranjeruud/",
    ]
    rules = (
        #将所有符合正则表达式的url加入到抓取列表中
        Rule(SgmlLinkExtractor(allow = (r'^https:\/\/www\.douban\.com\/people\/[^\/\n]+(|\/)$',)), callback = 'parse_page',follow="true"),
        #将所有符合正则表达式的url请求后下载网页代码, 形成response后调用自定义回调函数
        #Rule(SgmlLinkExtractor(allow = (r'http://movie\.douban\.com/subject/\d+', )), callback = 'parse'),
        )

    def parse_page(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """

        sel = Selector(response)
        item=DItem()
        bd = sel.css('#profile > div.infobox > div.bd')
        if not bd:
            return
        userinfo=bd.css('div.basic-info > div.user-info')
        if not userinfo:
            return
        
        place=userinfo.css('a::text')
        if not place:
            item['place'] =""
        else:
            item['place'] =place.extract_first().strip()
        
        nametimecss=userinfo.css('div.pl ::text')
        if not nametimecss:
            return
        nametime=nametimecss.extract()#.extract_first().strip()
        if not nametime:
            return
        if len(nametime)==2:
            item['name']=nametime[0]
            item['time']=nametime[1]
        else:
            return
        userintro=sel.css('#intro_display')
        if not userintro:
            return
        content = '\n'.join(userintro.xpath('string(.)').extract())
        if not content:
            item['intro']=""
        else:
            item['intro']=content
        #item['url'] = dd.xpath('a/@href').extract_first().strip()
        return item
        
