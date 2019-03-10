# coding: utf-8

from selenium import webdriver
import time

def main():

    # 第一步：初始化驱动，打开本地网页
    driver = webdriver.Firefox()
    filepath = 'file:///D:\Hello World\python_work\Spider_development_study_note\ch09\login.html'
    driver.get(filepath)
    time.sleep(3)

    # 第二步：获取用户名和密码的输入框，和登录按钮
    # 使用不同的方法查找
    username = driver.find_element_by_name("username").get_attribute()
    password = driver.find_element_by_xpath(".//*[@id='loginForm']/input[2]")
    login_button = driver.find_element_by_xpath("//input[@type='submit']")

    # 第三步：使用send_keys方法输入用户名和密码，使用click方法模拟点击登录
    username.send_keys("yiye")
    password.send_keys("qiye_pass")
    login_button.click()

    # 第四步：清空输入框
    username.clear()
    password.clear()


if __name__ == '__main__':
    main()

