import scrapy
from bs4 import BeautifulSoup as bs 
from scrapy import Request

class CutterSpider(scrapy.Spider):
    name = 'cutter'
    start_urls = ['https://licota.kz/search/?search=%D1%84%D1%80%D0%B5%D0%B7%D0%B0&page=']
    page_count = 16

    def start_requests(self):
        for page_number in range(1, self.page_count+1):
            request = Request(self.start_urls[0] + str(page_number), callback=self.parse)
            yield request

    def parse(self, response):
        soup = bs(response.text, 'lxml')
        links = [h4.find("a").get('href') for h4 in soup.find_all("h4")]
        for cutter_link in links:
            yield response.follow(cutter_link, callback=self.parse_cutter_data)

    def parse_cutter_data(self, response):
        soup = bs(response.text, 'lxml')
        name = soup.find("h1").text.strip()
        left = [value.text.strip().replace(":", "")
                for value in soup.find_all("div", class_="dotted-line_left")[1:]]
        right = [value.text.strip() for value in soup.find_all(
            "div", class_="dotted-line_right")[1:]]
        records = dict(zip(left, right))
        try:
            description = soup.find(
                "div", class_="b-product-description__main b-product-description__main_full").text.strip()
        except:
            description = "Без описания"
        price = soup.find("span", class_="update_price").text.strip()

        yield{
            "Название": name,
            "Категория": "Фреза",
            "Цена": price,
            "Описание": description,
            "Атрибуты": records,
            "Ссылка": response.request.url,
        }
