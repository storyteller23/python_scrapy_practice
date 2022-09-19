from .conditioner import ConditionerSpider

class WallConditionerSpider(ConditionerSpider):
    name = 'wall'
    start_urls = ['https://2time.kz/g7026203-nastennye-konditsionery-split/page_']
    cat_2 = 'Настенный(сплит системы)'
    page_count = 13
