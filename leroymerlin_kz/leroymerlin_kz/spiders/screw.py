import json

import scrapy
from scrapy import FormRequest
from scrapy.utils.project import get_project_settings

class ScrewSpider(scrapy.Spider):
    name = 'screw'
    start_urls = ['https://leroymerlin.kz/api/internal/component/search:result/json']
    page_count = 42
    settings = get_project_settings()
    cookies = settings.get('COOKIES')
    form_data = {'csrf_token': '099c155e50a0451d022cf8e55bbfbf0e',
                'q': 'винт',
                'currentPage': '1',
                'perPage': '30',
                'sortField': 'POPULARITY',
                'sortDirection': 'desc',
            }
    cat_1 = 'Винт'

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
        items = data['tabs']['products']['result']['items']
        for item in items:
            name = item['UF_NAME_RU']
            if 'винт' not in name.lower():
                continue
            url = 'https://leroymerlin.kz' + item['URL']

            left, right = [], []
            if 'PROPS_VALUES' in item:
                records = list(item['PROPS_VALUES'].values())
                left = [record['NAME'] for record in records if 'NAME' in record]
                right = [record['VALUE'] for record in records if 'VALUE' in record]

            yield {
                'Название': name,
                'Категория': self.cat_1,
                'Атрибуты': dict(zip(left, right)),
                'Ссылка': url,
            }


