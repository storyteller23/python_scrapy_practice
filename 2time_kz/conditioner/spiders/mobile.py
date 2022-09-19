from .conditioner import ConditionerSpider

class MobileConditionerSpider(ConditionerSpider):
    name = 'mobile'
    start_urls = ['https://2time.kz/g7026797-konditsionery-mobilnye-napolnye/page_']
    cat_2 = 'Мобильные'
    page_count = 1
