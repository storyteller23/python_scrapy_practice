from .conditioner import ConditionerSpider

class RooftopConditionerSpider(ConditionerSpider):
    name = 'rooftop'
    start_urls = ['https://2time.kz/g7345684-kryshnye-konditsionery-ruftop/page_']
    cat_2 = 'Крышные'
    page_count = 1
