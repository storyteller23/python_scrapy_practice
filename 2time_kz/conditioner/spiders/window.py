from .conditioner import ConditionerSpider

class WindowConditionerSpider(ConditionerSpider):
    name = 'window'
    start_urls = ['https://2time.kz/g7026213-konditsionery-okonnye']
    cat_2 = 'Оконные'
    page_count = 1