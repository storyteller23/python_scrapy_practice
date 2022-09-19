import scrapy
from scrapy import Request
from bs4 import BeautifulSoup as bs

class SwitchSpider(scrapy.Spider):
    name = 'switch'
    start_urls = ['https://ekfgroup.com/catalog/modulnye-avtomaticheskie-vyklyuchateli?page=']

    page_count = 54

    def start_requests(self):
        for page_number in range(1, self.page_count + 1):
            req = Request(self.start_urls[0] + str(page_number), callback=self.parse)
            yield req
    
    def parse(self, response):
        soup = bs(response.text, "lxml")
        titles = soup.find_all("p", class_="product-title")
        for title in titles:
            yield response.follow(title.find("a").get("href"), callback=self.parse_switch_data)
    
    def parse_switch_data(self, response):
        soup = bs(response.text, "lxml")
        name = soup.find("h1").text
        categor = soup.find_all("li", class_="breadcrumb-item")[-1].text.strip()
        left = []
        right = []
        for row in soup.find_all("tr")[1:]:
            temp = row.find_all("td")
            left.append(temp[0].text.strip())
            right.append(temp[1].text.strip())
        records = dict(zip(left, right))
        yield {
            "Название": name,
            "Категория": "Выключатель",
            "Категория 2": categor,
            "Атрибуты": records,
            "Ссылка": response.url,
        }