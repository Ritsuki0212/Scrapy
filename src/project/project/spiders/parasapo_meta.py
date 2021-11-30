from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from project.items import ProjectItem


class parasapoMetaSpider(CrawlSpider):
    name = 'parasapoMeta'
    allowed_domains = ['www.parasapo.tokyo']    # クロールを許可するドメイン
    start_urls = ["https://www.parasapo.tokyo/"]  # クロールを開始するページのURL

    # 2016~2022以外の/en/scheduleページは省く
    rules = [Rule(LinkExtractor(deny=(r'/en/schedule/\?year=(?!.*2016|2017|2018|2019|2020|2021|2022).*$')), callback='parse_page', follow=True)]

    def parse_page(self, response):
        item = ProjectItem()
        item['URL'] = response.url
        item['title'] = response.css('title::text').get()
        item['description'] = response.xpath('//meta[@name="description"]/@content').extract()
        item['robots'] = response.xpath('//meta[@name="robots"]/@content').extract()
        item['og_locale'] = response.xpath('//meta[@property="og:locale"]/@content').extract()
        item['og_type'] = response.xpath('//meta[@property="og:type"]/@content').extract()
        item['og_title'] = response.xpath('//meta[@property="og:title"]/@content').extract()
        item['og_description'] = response.xpath('//meta[@property="og:description"]/@content').extract()
        item['og_url'] = response.xpath('//meta[@property="og:url"]/@content').extract()
        item['og_site_name'] = response.xpath('//meta[@property="og:site_name"]/@content').extract()
        item['og_image'] = response.xpath('//meta[@property="og:imege"]/@content').extract()
        yield item