import scrapy
from bs4 import BeautifulSoup as bs


class JournalSpider(scrapy.Spider):
    name = 'journal'
    start_urls = ['https://www.hr-ok.ru/e-store/journals/']

    def parse(self, response):
        soup = bs(response.text, "lxml")
        a = soup.find_all("a", class_="tile__title")
        for el in a:
            if "Набор" in el.text or "Штамп" in el.text:
                continue
            yield response.follow(el.get("href"), callback=self.parse_journal_data)

    def parse_journal_data(self, response):
        soup = bs(response.text, "lxml")
        name = soup.find("h1").text.strip()
        price = soup.find("div", class_="tile__price-current").text.strip()
        journal_type = ""
        if "учет" in name.lower():
            journal_type = "Для учета"
        else:
            journal_type = "Для записи"
        soup.find("div", class_="catalog-item-card__offer portal").decompose()
        soup.find("div", class_="catalog-item-card__buy").decompose()
        description = soup.find("div", class_="catalog-item-card__description")
        full_desc = description.text.strip()
        description = [
            el for el in description.text.strip().split("\n")if el != "\r"]
        records = {}
        if "Ведение" in description[0]:
            records["Тип журнала"] = journal_type
            records["Ведение"] = description[0].split()[1]
            for l in description:
                if "Количество" in l:
                    records["Количество страниц"] = l
                    continue
                if "Обложка" in l:
                    records["Обложка"] = l.split(":")[1].strip()
        else:
            records["Тип журнала"] = journal_type
            for l in description:
                if "Формат" in l:
                    records["Формат"] = l.split(":")[1].strip()

                if "Количество" in l:
                    records["Количество страниц"] = l
                    continue
                if "Обложка" in l:
                    records["Обложка"] = l.split(":")[1].strip()
        yield{
            "Название": name,
            "Категория": "Журнал",
            "Цена": price,
            "Атрибуты": records,
            "Полное описание": full_desc,
            "Ссылка": response.request.url
        }
