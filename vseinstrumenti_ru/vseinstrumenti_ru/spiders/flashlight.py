from urllib.request import Request
import scrapy
from scrapy_splash import SplashRequest

class FlashlightSpider(scrapy.Spider):
    name = 'flashlight'
    start_urls = ['https://www.vseinstrumenti.ru/electrika_i_svet/svetilniki/fonari/']
    cat_1 = 'Фонарь'

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, callback=self.parse) 

    def parse(self, response):
        for url in response.css('.-grid-item .link::attr("href")').getall():
            if 'aksessuary' in url or 'pushlight' in url:
                continue
            yield SplashRequest(url, callback=self.parse_first_page)
    
    def parse_first_page(self, response):
        for flashlight_link in response.css('.middle .title a::attr("href")').getall():
            yield SplashRequest(
                'https://www.vseinstrumenti.ru' + flashlight_link,
                callback=self.parse_flashlight_data
            )

        
        page_count = response.css('.pagination::attr("data-max-page")')

        if page_count != []:
            for page_number in range(2, int(page_count.get())+1):
                yield SplashRequest(
                    response.url + 'page' + str(page_number),
                    callback=self.parse_any_page
                )
    
    def parse_any_page(self, response):
        for flashlight_link in response.css('.middle .title a::attr("href")').getall():
            yield SplashRequest(
                'https://www.vseinstrumenti.ru' + flashlight_link,
                callback=self.parse_flashlight_data
            )

            
    def parse_flashlight_data(self, response):
        name = response.css('.-product-card .title::text').get()
        cat_1 = self.cat_1
        left = [el.strip() for el in response.css('.option .text::text').getall() if el.strip() != '']
        right = [el.strip() for el in response.css('.dotted-list .value *::text').getall() if el.strip() != '']
        records = dict(zip(left, right))
        url = response.url
        cat_2 = ''
        if 'Тип' in records:
            cat_2 = records['Тип'].title()

        yield {
            "Название": name,
            "Категория": cat_1,
            "Категория 2": cat_2,
            "Атрибуты": records,
            "Ссылка": url
        }