from .conditioner import ConditionerSpider

class FloorCeilConditionerSpider(ConditionerSpider):
    name = 'floorceil'
    start_urls = ['https://2time.kz/g7026789-konditsionery-napolno-potolochnye/page_']
    cat_2 = 'Напольно-потолочные'
    page_count = 2
