# -*- coding: utf-8 -*-

# Scrapy settings for shtspider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'shtspider'

SPIDER_MODULES = ['shtspider.spiders']
NEWSPIDER_MODULE = 'shtspider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'shtspider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
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
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'shtspider.middlewares.ShtspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'shtspider.middlewares.ShtspiderDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline':301,
    'shtspider.pipelines.ShtspiderPipeline': 300,
    'shtspider.pipelines.MyImagesPipeline': 1,

}

# 上面添加了ImagesPipeline用于下载图片
# 设置图片的下载地址，图片地址，文件结果信息，制作缩略图
IMAGES_STORE = 'D:\Hello World\python_work\Spider_development_study_note\ch12\sht\shtimages'
IMAGES_URLS_FIELD = 'image_urls'
IMAGES_REULT_FIELD = 'images'
IMAGES_THUMBS = {
    'small': (50, 50),
    'big': (270, 270),
}


# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 使用scrapy_redis的调度器，
# 启动爬虫前需要先CMD启动本地的redis-server，然后处于打开状态，然后再运行爬虫
# 第一遍运行后，已经爬取过的数据都会存储在redis数据库中，然后再次运行，由于都是爬取过的，爬虫会迅速结束，
# 有新的内容才会继续爬取
SCHEDULER = 'scrapy_redis.scheduler.Scheduler'
# （可选参数）在Redis中保持scrapy-redis用到的各个队列，从而允许暂停和暂停后恢复
SCHEDULER_PERSIST = True
# 使用scrapy_redis的去重方式
DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'
# 使用scrapy_redis的存储方式,见上面ITEM_PIPELINES，并将顺序设置成最后一个，用于存储下载所有的数据
# 定义Redis的IP和端口
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379

# 注意，改造成分布式爬虫后，传人URL，已经爬取过的ITEM会存储在本地服务器中
# 可以在redis中输入keys * 查看所有的键
# 使用flushall可以删除所有本地所有的键值数据
# 删除数据后再次传入起始URL，然后启动爬虫，就可以开始爬取
# 注意：分布式爬虫，redis服务器一直处于运行状态，爬虫不会自己结束，
# 可以向服务器一直传入新的URL，然后爬虫会自动继续爬取新的URL，重复的会自动跳过
# 爬取完成后，手动结束爬虫程序即可


