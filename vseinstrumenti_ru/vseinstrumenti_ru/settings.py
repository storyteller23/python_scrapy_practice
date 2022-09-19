# Scrapy settings for vseinstrumenti_ru project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'vseinstrumenti_ru'

SPIDER_MODULES = ['vseinstrumenti_ru.spiders']
NEWSPIDER_MODULE = 'vseinstrumenti_ru.spiders'

COOKIES = {
    'isVueListing': '1',
    'cartToken': 'E2l9SgwkS2bd44gvWK2mpu9a4YtaB2f7',
    'favToken': 'e5hU8lJv5fg4meSdnC2Ruw7Oi6CCHATE',
    'rrpvid': '338967080088746',
    'device_uid': 'ZLTVw0qWXv6QgXYXNnLep30M3J40X0UZ7ni40zgBY5uHi44yy9VAYQ4T2V8sJ05k',
    'ab_exps': '%7B%22237%22%3A4%2C%22243%22%3A11%2C%22245%22%3A1%2C%22248%22%3A0%2C%22249%22%3A1%2C%22260%22%3A9%2C%22262%22%3A0%2C%22280%22%3A2%2C%22362%22%3A1%2C%22368%22%3A1%2C%22380%22%3A1%2C%22402%22%3A10%2C%22415%22%3A2%2C%22426%22%3A0%2C%22432%22%3A3%2C%22438%22%3A1%2C%22462%22%3A0%2C%22468%22%3A3%2C%22408%22%3A3%2C%22474%22%3A1%2C%22374%22%3A2%7D',
    'shouldBeSaleTeaser': '1',
    'goods_per_page': '40',
    'pages_viewed': '%7B%22value%22%3A1%2C%22expiration%22%3A1662628412%7D',
    'is-visited': '1',
    'wucf': '7',
    'DCID': '3dc-site-ox1-app3',
}

FEED_EXPORT_ENCODING = 'utf-8'
SPLASH_URL = 'http://localhost:8050/'
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'vseinstrumenti_ru.middlewares.VseinstrumentiRuSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
#    'vseinstrumenti_ru.middlewares.VseinstrumentiRuDownloaderMiddleware': 543,
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'vseinstrumenti_ru.pipelines.VseinstrumentiRuPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
