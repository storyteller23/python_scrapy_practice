import json

import scrapy
from scrapy import FormRequest
from scrapy.utils.project import get_project_settings

class SelftappingSpider(scrapy.Spider):
    name = 'selftapping'
    start_urls = ['https://leroymerlin.kz/api/internal/vue/catalogue_section_listing/405']
    page_count = 16
    form_data = {'csrf_token': '099c155e50a0451d022cf8e55bbfbf0e',
                'currentPage': '1',
                'perPage': '30',
                'collection':'' ,
                'sortField': 'POPULARITY',
                'sortDirection': 'desc',
    }
    settings = get_project_settings()
    cookies = settings.get('COOKIES')

    cat_1 = 'Саморез'

    def start_requests(self):
        for i in range(1, self.page_count + 1):
            data = self.form_data
            data['currentPage'] = str(i)
            req = FormRequest(
                self.start_urls[0],
                method='POST',
                cookies=self.cookies,
                formdata=data,
                callback=self.parse,
                )
            yield req

    def parse(self, response):
        data = json.loads(response.text)
        items = data['products']
        for item in items:
            yield response.follow(item['URL'], callback=self.parse_selftapping_data, cookies=self.cookies)

    def parse_selftapping_data(self, response):
        name = response.css('.product__h1-mobile::text').get()
        url = response.request.url
        values = [el.strip() for el in response.css('tbody td::text').extract() if el.strip() != '']
        left = [values[i] for i in range(0, len(values), 2)]
        right = [values[i] for i in range(1, len(values), 2)]
        attrs = dict(zip(left, right))
        yield {
            'Название': name,
            'Категория': self.cat_1,
            'Атрибуты': attrs,
            'Ссылка': url,
        }