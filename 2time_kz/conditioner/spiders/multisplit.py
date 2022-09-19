from .conditioner import ConditionerSpider

class MultiSplitConditionerSpider(ConditionerSpider):
    name = 'multisplit'
    start_urls = ['https://2time.kz/g7026206-konditsionery-multi-split/page_']
    cat_2 = 'Мульти-сплит система'
    page_count = 2
