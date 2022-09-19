from gc import callbacks
from os import scandir
from unicodedata import category
from unittest.mock import NonCallableMagicMock
import scrapy

class PuskateliSpider(scrapy.Spider):
    name = "puskateli"

    start_urls = ["https://e-kc.ru/cena?keyword=%D0%BF%D1%83%D1%81%D0%BA%D0%B0%D1%82%D0%B5%D0%BB%D1%8C&page=1"]

    def parse(self, response):
        for url in response.css("#idTab1 .text a::attr('href')").extract():
            yield response.follow(url, callback=self.parse_data)
        
        next_page = response.css(".next_page_link::attr('href')")

        if next_page is not None:
            yield response.follow(next_page.get(), callback=self.parse)
        
    
    def parse_data(self, response):
        name = response.css("h1::text").get()
        category_1 = "Пускатель"
        category_2 = ""
        if 'электромагнитный' in name:
            category_2 = 'Электромагнитный'
        elif 'магнитный' in name:
            category_2 = 'Магнитный'
        left = []
        right = []
        for li in response.css("#idTab2 li"):
            left.append(li.css('label::text').get().strip())
            right.append(li.css('span::text').get().strip())
        records = dict(zip(left, right))
        url = response.request.url

        yield {
            "Название": name,
            "Категория": category_1,
            "Категория 2": category_2,
            "Атрибуты": records,
            "Ссылка": url,
        }
