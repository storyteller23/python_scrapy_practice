import scrapy
from bs4 import BeautifulSoup as bs
from scrapy.utils.project import get_project_settings
from scrapy import Request

class HddSpider(scrapy.Spider):
    name = 'hdd'
    start_urls = ["https://shop.kz/zhestkie-diski-NB/"]
    settings = get_project_settings()
    cookies = settings.get('COOKIES')
    
    def start_requests(self):
        for url in self.start_urls:
            req = Request(url, cookies=self.cookies, callback=self.parse)
            yield req

    def parse(self, response):
        soup = bs(response.text, 'lxml')
        finds = soup.find_all("div", class_="bx_catalog_item_title")
        for el in finds:
            yield response.follow(el.find("a").get("href"), callback=self.parse_hdd_data)
    
    def parse_hdd_data(self, response):
        soup = bs(response.text, "lxml")
        name = soup.find("h1").text
        description = soup.find("div", class_="bx_item_description").text.replace("Описание", "").strip()
        dt = soup.find_all("dt")
        dt_text = []
        try:
            price = soup.find("div", class_="item_current_price").text
        except:
            price = "Цена не указана"
        for d in dt:
            dt_text.append(d.text.strip())
        dd = soup.find_all("dd")
        dd_text = []
        for d in dd:
            dd_text.append(d.text.strip())
        records = dict(zip(dt_text, dd_text))
        
        yield {
            "Название": name,
            "Цена": price,
            "Описание": description,
            "Атрибуты": records,
            "Ссылка": response.request.url,
        }