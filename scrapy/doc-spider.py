import pprint
import subprocess

from scrapy.spiders import Spider
from scrapy.selector import HtmlXPathSelector


class DocSpider(Spider):
    name = "docspider"
    allowed_domains = ["arxiv.org"]
    start_urls = ['http://arxiv.org/list/cs.AI/recent']

    def parse(self, response):
        item = HtmlXPathSelector(response)
        # todo: strip html
        # todo: add other fields
        # todo: download articles
        titles = item.xpath('//*[@id="dlpage"]/dl/dd/div/div[contains(@class,"list-title")]/text()').extract()
        papers = item.xpath(
            '//*[@id="dlpage"]/dl/dt/span[contains(@class, "list-identifier")]/a[@title="Download PDF"]/@href').extract()
        print len(titles)
        print len(papers)
        title_list = []
        for t in titles:
            if t != '\n':
                t = t.replace("\n", "")
                print t
                title_list.append(t)
        print len(title_list), len(papers)
        i = 0
        list_map = {}
        for p in papers:
            base = "https://arxiv.org"
            print title_list[i], base + p
            subprocess.call('wget -U "Mozilla" {}.pdf'.format(base + p), shell=True)
            list_map[p.replace("/pdf/", "")] = title_list[i]
            i += 1
        print pprint.pprint(list_map)

# todo: create Knn of document classifications
# todo: export graph of findings
