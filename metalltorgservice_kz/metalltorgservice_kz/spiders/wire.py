import scrapy
from scrapy import Request 

from scrapy.utils.project import get_project_settings

class WireSpider(scrapy.Spider):
    name = 'wire'
    start_urls = ['https://www.metalltorgservice.kz/catalog/k-7029768-provoloka']
    settings = get_project_settings()
    cookies = settings.get('COOKIES')

    def start_requests(self):
        yield Request(self.start_urls[0], callback=self.parse, cookies=self.cookies)

    def parse(self, response):
        try:
            for wire_link in response.css('.title-.js-title- a::attr("href")').extract():
                yield response.follow(wire_link, callback=self.parse_wire_data, cookies=self.cookies)
        except:
            yield response.follow(response.request.url, callback=self.parse, cookies=self.cookies)
        
        next_page = response.css('.b-pagination_headItemNext::attr("data-to")')
        if len(next_page) != 0:
            yield response.follow(next_page.get(), callback=self.parse, cookies=self.cookies)

    def parse_wire_data(self, response):
        try:
            name = response.css(".js-breadcrumbs-item span::text")[-2].get().strip()
        except:
            yield response.follow(response.request.url, callback=self.parse_wire_data, cookies=self.cookies)
        cat_1 = 'Проволока'
        cat_2 = response.css('.js-breadcrumbs-item:nth-child(5) span::text').get().strip()
        left = []
        right = []

        for attr_name_block in response.css('.company-product-card-traits__name::text'):
            attr_name = attr_name_block.get()
            if attr_name.strip() != "":
                left.append(attr_name.strip())

        for attr_value_block in response.css('.company-product-card-traits__value *::text'):
            attr_value = attr_value_block.get()
            if attr_value.strip() != "":
                right.append(attr_value.strip())
    
        records = dict(zip(left, right))
        url = response.request.url

        yield {
            "Название": name,
            "Категория": cat_1,
            "Категория 2": cat_2,
            "Атрибуты": records,
            "Ссылка": url,
        }
        