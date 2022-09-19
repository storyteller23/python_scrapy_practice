from .conditioner import ConditionerSpider

class CanalConditionerSpider(ConditionerSpider):
    name = 'canal'
    start_urls = ['https://2time.kz/g7026211-konditsionery-kanalnye/page_']
    cat_2 = 'Канальные'
    page_count = 2
