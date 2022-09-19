import scrapy
from scrapy import Request
import re

COOKIES = {'ccc':'Yx2gqLJa2rManQgDc1qOE5mSofPYDC_F48rWCEVObf3CQSR_e_F7rejwDAIh8cyvT-Zvq0Dy8uimYGj0bTsdMQ=='} 

class WheelsSpider(scrapy.Spider):
    name = 'wheels'
    start_urls = ['https://promby.deal.by/product_list/page_']
    page_count = 80
    cat_1 = 'Круг'

    def start_requests(self):
        for page_number in range(1, self.page_count):
            yield Request(self.start_urls[0] + str(page_number), callback=self.parse, cookies=COOKIES)

    def parse(self, response):
        if response.status != 200:
            COOKIES['ccc'] = input('Введите новый ключ:')
            yield response.follow(response.url, callback=self.parse, cookies=COOKIES)
        for url in response.css('.cs-goods-title::attr("href")').getall():
            if 'krug' in url:
                yield response.follow(url, callback=self.parse_wheel_data, cookies=COOKIES)
    
    def parse_wheel_data(self, response):
        if response.status != 200:
            COOKIES['ccc'] = input('Введите новый ключ:')
            yield response.follow(response.url, callback=self.parse, cookies=COOKIES)
        name = response.css('.cs-title__product::text').get()
        url = response.url
        cat_1 = self.cat_1
        cat_2 = ''
        left = [el.strip() for el in response.css('.b-product-info__cell:nth-child(1)::text').getall() if el.strip() != ""]
        right = [el.strip() for el in response.css('.b-product-info__cell+ .b-product-info__cell::text').getall() if el.strip() != ""]
        records = dict(zip(left, right))
        if 'Назначение' in records:
            cat_2 = records['Назначение']

        if "Шлифматериал" not in records:
            spec_attr = response.css('.cs-page__row p+ p::text').re('Шлифматериал.*')
            if len(spec_attr) != 0:
                find = re.findall(r'\w+', " ".join(spec_attr))
                records["Шлифматериал"] = find[-2] + ' ' + find[-1]
        
        yield {
            "Название": name,
            "Категория": cat_1,
            "Категория 2": cat_2,
            "Атрибуты": records,
            "Ссылка": url, 
        }
        
    