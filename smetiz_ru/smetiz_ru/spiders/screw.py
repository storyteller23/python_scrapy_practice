import scrapy
from bs4 import BeautifulSoup as bs

class ScrewSpider(scrapy.Spider):
    name = 'screw'
    start_urls = ["https://smetiz.ru/tovary/gajki/"]

    def parse(self, response):
        soup = bs(response.text, "lxml")
        blocks = soup.find_all("a", class_="catalogItemSub")
        for block in blocks:
            yield response.follow(block.get("href"), callback=self.parse_screw_pages)
    
    def parse_screw_pages(self, response):
        soup = bs(response.text, "lxml")
        blocks = soup.find_all("a", class_="d-inline-block text-decoration-none")
        for block in blocks:
            yield response.follow(block.get("href"), callback=self.parse_screw_data)
        
        next_page_exist = response.css('.pagination__item.control span::text') == "»"
        if next_page_exist:
            next_page_url = response.css('.pagination__item.control a::attr("href")')[-1].get()
            yield response.follow(next_page_url, callback=self.parse_screw_data) 
    
    def parse_screw_data(self, response):
        soup = bs(response.text, "lxml")
        name = "Гайка"
        left = []
        right = []
        items = soup.find_all("div", class_="chars-list__item")
        for item in items:
            left.append(item.find("div", class_="chars-list__title").text.replace(":", "").strip())
            right.append(item.find("div", class_="chars-list__desc").text.strip())
        
        records = dict(zip(left, right))
        if "Группа стандартов" in records:
            name += " " + records["Группа стандартов"]
        if "Артикул" in records:
            del records["Артикул"]
        yield {
            "Название": name,
            "Категория": "Гайка",
            "Атрибуты": records,
            "Ссылка": response.request.url,
        }