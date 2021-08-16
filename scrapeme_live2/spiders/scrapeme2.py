import scrapy
from scrapy.http.request import Request
from ..items import ScrapemeLive2Item

class Scrapeme2Spider(scrapy.Spider):
    name = 'scrapeme2'
    #allowed_domains = ['scrapeme.live/shop/']
    #start_urls = ['http://scrapeme.live/shop//']

    def start_requests(self):
        url = 'https://scrapeme.live/shop/page/{}/'
        for i in range(1,11):
            yield scrapy.Request(url=url.format(i), callback=self.parse_page)

    def parse_page(self,response):
        products = response.xpath('//a[@class="woocommerce-LoopProduct-link woocommerce-loop-product__link"]/@href').extract()
        for product_url in products:
            yield scrapy.Request(url=product_url, callback=self.parse_product)
    def parse_product(self, response):
        rows=response.xpath('//div[@class="summary entry-summary"]')
        for row in rows:
            name = row.xpath('h1/text()').extract()
            desc = row.xpath('div/p/text()').extract()
            stock = row.xpath('p[@class="stock in-stock"]/text()').extract()
            price = row.xpath('p[@class="price"]/span/text()').extract()
            sku = row.xpath('div[@class="product_meta"]/span[@class="sku_wrapper"]/span[@class="sku"]/text()').extract()
            cat = row.xpath('div[@class="product_meta"]/span[@class="posted_in"]/a/text()').extract()
            tags = row.xpath('div[@class="product_meta"]//span[@class="tagged_as"]/a/text()').extract()
            items = ScrapemeLive2Item()
            items['Name'],items['Description'],items['Stock'],items['Price'],items['SKU'],items['Category'],items['Tags'] = ''.join(name), ''.join(desc), ''.join(stock), ''.join(price), ''.join(sku), ','.join(cat), ','.join(tags)
        yield items