import json
import time
import scrapy
from scrapy import Request
from scrapy.selector import Selector
from ..items import HotSpot


class JsSpider(scrapy.Spider):
    name = "jianshu"
    start_urls = "https://www.jianshu.com/c/20f7f4031550?utm_medium=index-collections&utm_source=desktop"

    headers = {
        "Host": "www.jianshu.com",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://www.jianshu.com/sign_in",
        "Cookie": "_ga=GA1.2.1556006355.1513931099; "
                  "read_mode=day; default_font=font2; "
                  "sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221607d535db96f1-0b1918587a9474-3a3e5f04-1049088-1607d535dba901%22%2C%22%24device_id%22%3A%221607d535db96f1-0b1918587a9474-3a3e5f04-1049088-1607d535dba901%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.bing.com%2F%22%2C%22%24latest_referrer_host%22%3A%22www.bing.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_utm_source%22%3A%22desktop%22%2C%22%24latest_utm_medium%22%3A%22index-collections%22%2C%22%24latest_utm_campaign%22%3A%22maleskine%22%2C%22%24latest_utm_content%22%3A%22note%22%7D%2C%22first_id%22%3A%22%22%7D; "
                  "Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1516971275,1517224882,1517361777,1517383062; "
                  "Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1517386710; "
                  "locale=zh-CN; remember_user_token=W1s5MDU5NDUyXSwiJDJhJDExJC5KLmZKbnFnSzV6d0VVemMxMGxVc2UiLCIxNTE3Mzg2Njg5LjU3MjgxOSJd--f1382dc041bef2c686228019b00bad2b81bab0e4;"
                  " _m7e_session=e6a2227b5cfd73596622328d0ac75ee9",
        "Connection": "keep-alive"
    }

    def start_requests(self):

        yield (Request(self.start_urls, callback=self.parse, headers=self.headers));

    def parse(self, response):
        # filename = "hot.html"
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        contents = Selector(response).xpath('//ul[@class="note-list"]//div[@class="content"]').extract()
        name = "hotSpot/hotSpot_" + time.strftime('%Y-%m-%d', time.localtime(time.time())) + ".txt"
        for content in enumerate(contents):
            hotSpot = HotSpot()
            title = Selector(text=content[1]).xpath('//a[@class="title"]/text()').extract()
            link = Selector(text=content[1]).xpath('//a[@class="title"]/@href').extract()
            brief = Selector(text=content[1]).xpath('//p[@class="abstract"]/text()').extract()
            meta = Selector(text=content[1]).xpath('//div[@class="meta"]').extract();
            metas = meta[0].split('\n')
            for s in metas:
                if (s.find('ic-list-read"></i>') > 0):
                    sss = s.split(' ')
                    hotSpot['read'] = sss[len(sss) - 1]
                if (s.find('ic-list-comments"></i>') > 0):
                    sss = s.split(' ')
                    hotSpot['comments'] = sss[len(sss) - 1]
                if (s.find('ic-list-like"></i>') > 0):
                    sss = s.rstrip('</span>').split(' ')
                    hotSpot['like'] = sss[len(sss) - 1]
            hotSpot['title'] = title[0]
            hotSpot['link'] = link[0]
            hotSpot['brief'] = brief[0]
            hotSpotDic = hotSpot.__dict__
            with open(name, 'a') as f:
                f.write(json.dumps(hotSpotDic))
                f.write("\n")
                f.close()
