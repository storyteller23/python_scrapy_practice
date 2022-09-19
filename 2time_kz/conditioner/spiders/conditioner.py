import scrapy
from scrapy import Request
from scrapy.utils.project import get_project_settings

class ConditionerSpider(scrapy.Spider):
    name = 'spidername'
    start_urls = ['url']
    cat_1 = 'Кондиционер'
    cat_2 = 'Категория 2'
    page_count = 0
    settings = get_project_settings()
    cookies = settings.get('COOKIES')
    def start_requests(self):
        for page_number in range(1, self.page_count+1):
            req = Request(self.start_urls[0] + str(page_number), cookies = self.cookies, callback=self.parse)
            yield req


    def parse(self, response):
        for item_page in response.css('.b-product-gallery__title::attr("href")').extract():
            yield response.follow(item_page, callback=self.parse_item_data, cookies=self.cookies)
    
    def parse_item_data(self, response):
        name = response.css('.b-title span::text').get().strip()
        url = response.request.url

        tables = response.css('table')[1:]
        left = []
        right = []
        for table in tables:
            elems = [el.strip() for el in table.css('td::text').extract() if el.strip() != ""]
            left += [elems[i] for i in range(0, len(elems), 2)]
            right += [elems[i] for i in range(1, len(elems), 2)]

        yield {
            'Название': name,
            'Категория': self.cat_1,
            'Категория 2': self.cat_2,
            'Атрибуты': dict(zip(left, right)),
            'Ссылка': url,
        }
