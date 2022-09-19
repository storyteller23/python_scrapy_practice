from .conditioner import ConditionerSpider

class ColumnarConditionerSpider(ConditionerSpider):
    name = 'columnar'
    start_urls = ['https://2time.kz/g7026205-konditsionery-kolonnye-napolnye/page_']
    cat_2 = 'Колонные'
    page_count = 2
