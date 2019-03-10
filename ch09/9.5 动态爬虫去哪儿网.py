# coding: utf-8
import datetime
import codecs
import time
from bs4 import BeautifulSoup
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class QunaSpider(object):

    # 第一步：找到酒店信息搜索页面，分析搜索输入部分的页面源代码
    # 获取目的地、入住日期、离店日期和搜索按钮的元素位置
    # 输入内容，并点击搜索按钮
    def get_hotel(self, driver, to_city, fromdate, todate):
        ele_toCity = driver.find_element_by_name('toCity')
        ele_fromDate = driver.find_element_by_id('fromDate')
        ele_toDate = driver.find_element_by_id('toDate')
        ele_search = driver.find_element_by_class_name('search-btn')
        ele_toCity.clear()
        ele_toCity.send_keys(to_city)
        ele_toCity.click()
        ele_fromDate.clear()
        ele_fromDate.send_keys(fromdate)
        ele_toDate.clear()
        ele_toDate.send_keys(todate)
        ele_search.click()
        page_num = 0

        # 第二步：分两次获取一页完整的数据，第二次让driver执行js脚本，把网页拉到底部
        # 去哪儿点击搜索后，只会显示15条信息，向下滚到后才会加载剩余的15条，
        # 一个完整的页面有30条信息
        while True:
            try:
                WebDriverWait(driver, 10).until(
                    EC.title_contains((to_city))
                )
            except Exception as e:
                print(e)
                break
            time.sleep(5)

            js='window.scrollTo(0, document.body.scrollHeight);'
            driver.execute_script(js)
            time.sleep(5)
            htm_const = driver.page_source

            # 第三步：使用BS解析酒店信息，并将数据进行清洗和存储
            soup = BeautifulSoup(htm_const, 'html.parser', from_encoding='utf-8')
            infos = soup.find_all(class_='item_hotel_info')
            f = codecs.open(to_city + fromdate + u'.html', 'a', 'utf-8')
            for info in infos:
                f.write(str(page_num) + '--' * 50)
                content = info.get_text().replace(" ", "").replace("\t", "").strip()
                for line in [ln for ln in content.splitlines() if ln.strip()]:
                    f.write(line)
                    f.write('\r\n')
            f.close()

            # 第四步：点击下一页，继续重复这个步骤
            try:
                next_page = WebDriverWait(driver, 10).until(
                    EC.visibility_of(driver.find_element_by_css_selector(".item.next"))
                )
                next_page.click()
                page_num += 1
                time.sleep(10)
            except Exception as e:
                print(e)
                break

    def crawl(self, root_url, to_city):
        today = datetime.date.today().strftime('%Y-%m-%d')
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        tomorrow = tomorrow.strftime('%Y-%m-%d')
        driver = webdriver.Firefox()
        driver.set_page_load_timeout(50)
        driver.get(root_url)
        driver.maximize_window()  # 将浏览器最大化显示
        driver.implicitly_wait(10)  # 控制间隔时间，等待浏览器反映
        self.get_hotel(driver, to_city, today, tomorrow)

if __name__ == '__main__':
    spider = QunaSpider()
    spider.crawl('http://hotel.qunar.com/', u"上海")








