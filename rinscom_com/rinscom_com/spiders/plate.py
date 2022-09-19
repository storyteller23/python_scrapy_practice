from gc import callbacks
import scrapy
from bs4 import BeautifulSoup as bs

class PlateSpider(scrapy.Spider):
    name = 'plate'
    start_urls = ['https://www.rinscom.com/katalog/plastiny-tverdosplavnye/']

    def parse(self, response):
        soup = bs(response.text, "lxml")
        blocks = soup.find_all("tr", class_="catalog-section__row catalog-item")
        for block in blocks:
            yield response.follow(block.find("a").get("href"), callback=self.parse_plate_data)
        
        next_page = response.css('.bx-pag-next a::attr("href")')
        if next_page is not None:
            yield response.follow(next_page.get(), callback=self.parse)
    
    def parse_plate_data(self, response):
        soup = bs(response.text, "lxml")
        name = soup.find("h1").text.strip()
        price = soup.find("div", class_="product__price").text.strip()
        records_block = soup.find("div", class_="product__chars")
        left = [name.text.strip() for name in records_block.find_all("span", class_="product__chars-name")]
        right = [name.text.strip() for name in records_block.find_all("span", class_="product__chars-val")]
        records = dict(zip(left, right))
        yield {
            "Название": name,
            "Цена": price,
            "Атрибуты": records,
            "Ссылка": response.request.url,
        }