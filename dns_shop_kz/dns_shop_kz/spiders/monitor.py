import scrapy
from bs4 import BeautifulSoup as bs

class MonitorSpider(scrapy.Spider):
    name = 'monitor'
    start_urls = ['https://www.dns-shop.kz/catalog/17a8943716404e77/monitory/']

    def parse(self, response):
        for monitor_link in response.css('.catalog-product__name::attr("href")').extract():
            yield response.follow(monitor_link, callback=self.parse_monitor_info)
        try:
            next_page = response.css('.pagination-widget__page-link_next::attr("href")')
        except:
            return
        if next_page is not None:
            response.follow(next_page.get(), callback=self.parse)
    
    def parse_monitor_info(self, response):
        soup = bs(response.text, "lxml")
        left = [el.text.strip() for el in soup.find_all(
            "div", class_="product-characteristics__spec-title")]
        right = [el.text.strip() for el in soup.find_all(
            "div", class_="product-characteristics__spec-value")]
        records = dict(zip(left, right))
        name = records["Модель"]
        if "Технология изготовления матрицы" in records:
            if records["Технология изготовления матрицы"].upper() in ("IPS", "TN", "VA"):
                records["Технология изготовления матрицы"] = "ЖК"
        yield{
            "Название": name,
            "Категория": "Монитор",
            "Атрибуты": records,
            "Ссылка": response.url
        }