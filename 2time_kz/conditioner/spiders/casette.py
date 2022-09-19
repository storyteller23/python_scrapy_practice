from http.cookiejar import Cookie
import scrapy
from scrapy import Request

COOKIES = {'cid': '240311863788971586840111305234818211381', 'csrf_token_company_site':'4ae900e5ed894a86bf314b3d910589ee', 'companies_visited_products':'74445068.92431949.99140723.98583613.79616453.77042883.100356864.78438900.78433345.73820337', 'ccc':'YxXS6F84kAj5kTEIvZiWvwKXuqLW6AR4v2p3y-Q7R49FanGynun-SO8Qe7rr5kgZT8958-lF6-rLc1k6F4Tduw==',}

PAGE_COUNT = 2


class CasetteConditionerSpider(scrapy.Spider):
    name = 'casette'
    start_urls = ['https://2time.kz/g7026204-konditsionery-kassetnye/page_']

    def start_requests(self):
        for page_number in range(1, PAGE_COUNT+1):
            req = Request(self.start_urls[0] + str(page_number), cookies = COOKIES, callback=self.parse)
            yield req


    def parse(self, response):
        for item_page in response.css('.b-product-gallery__title::attr("href")').extract():
            yield response.follow(item_page, callback=self.parse_item_data, cookies=COOKIES)
    
    def parse_item_data(self, response):
        name = response.css('.b-title span::text').get().strip()
        url = response.request.url
        cat_1 = 'Кондиционер'
        cat_2 = 'Кассетные'
        tables = response.css('table')[1:]
        left = []
        right = []
        for table in tables:
            elems = [el.strip() for el in table.css('td::text').extract() if el.strip() != ""]
            left += [elems[i] for i in range(0, len(elems), 2)]
            right += [elems[i] for i in range(1, len(elems), 2)]

        yield {
            'Название': name,
            'Категория': cat_1,
            'Категория 2': cat_2,
            'Атрибуты': dict(zip(left, right)),
            'Ссылка': url,
        }
