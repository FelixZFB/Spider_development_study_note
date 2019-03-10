# selenium操作Firefox打开百度搜索网络爬虫

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def main():

    # 创建一个浏览器
    driver =webdriver.Firefox()
    # 打开百度首页
    driver.get('http://www.baidu.com')
    # 判断标题中是否有百度的字样
    assert u'百度' in driver.title
    # 通过元素wd获取输入框
    elem = driver.find_element_by_name('wd')
    # 清空输入框，向输入框中输入网络爬虫
    elem.clear()
    elem.send_keys(u'网络爬虫')
    # 然后模拟按回车键
    elem.send_keys(Keys.RETURN)
    # 延时3秒
    time.sleep(3)
    # assert是一个判断代码，如果结果为True就正常运行，如果不对，就会抛出一个异常
    # 判断搜索页面是否有网络爬虫.的字样，注意有点，所以判断时not in
    assert u'网络爬虫.' not in driver.page_source
    # 或者判断是否在里面为True,结果为True，代码才不会报错
    assert u'网络爬虫' in driver.page_source
    driver.close()

if __name__ == '__main__':
    main()





