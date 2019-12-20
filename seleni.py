from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from selenium.webdriver.firefox.options import Options
import lxml
from selenium.webdriver import ActionChains
import time
import re
import os
import urllib.request
option=Options()
option.add_argument('--headless')
browser = webdriver.Firefox(options=option)
num=0
for n in range(1,2):
    url='https://hyrz.qq.com/act/a20170510ninja/ninja.shtml?nid={}&xid=0'
    browser.get(url.format(n))
    content=browser.page_source

# print(content)
# content='''background-image: url("//game.gtimg.cn/images/hyrz/zlkdatasys/images/image/20170920/23_8981701.jpg");//game.gtimg.cn/images/hyrz/zlkdatasys/images/image/20181207/dc5a224f6edab4516f3d81b1d0721c2d.png'''
#扫描整个字符串并返回第一个成功的匹配。search
    results=re.findall('(//game.gtimg.cn/images/hyrz/zlkdatasys/images/image/\d+/[0-9a-zA-z_.]+)',content)
    #print(type(results))
for x in results:
    print(x)
    num+=1
    print(num)
    u="https:"+x
      # results.group()
    path = "D:\WorkSpace\pythonwk\hy\pic\\{}.jpg".format(num)
    urllib.request.urlretrieve(u, path)

# browser = webdriver.Firefox()
# browser.get('https://hyrz.qq.com/act/a20170510ninja/ninja.shtml?nid=77')
# img=browser.find_elements_by_class_name('banner')
"""前进后退"""
# browser.get('https://www.baidu.com/')
# browser.get('https://www.taobao.com/')
# browser.get('https://www.python.org/')
# browser.back()
# time.sleep(1)
# browser.forward()
# browser.close()

"""cookie"""
# browser.get('https://www.zhihu.com/explore')
# print(browser.get_cookies())
# browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'germey'})
# print(browser.get_cookies())
# browser.delete_all_cookies()
# print(browser.get_cookies())

"""选项卡管理"""
# browser.get('https://www.baidu.com')
# browser.execute_script('window.open()')
# print(browser.window_handles)
# browser.switch_to_window(browser.window_handles[1])
# browser.get('https://www.taobao.com')
# time.sleep(1)
# browser.switch_to_window(browser.window_handles[0])
# browser.get('https://python.org')

"""异常处理"""
# try:
#     browser.get('https://www.baidu.com')
# except TimeoutException:
#     print('Time Out')
# try:
#     browser.find_element_by_id('hello')
# except NoSuchElementException:
#     print('No Element')
# finally:
#     browser.close()

# browser.get('https://www.taobao.com/')
# wait = WebDriverWait(browser, 10)
# input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
# print(input, button)
# browser.implicitly_wait(10)
# browser.get('https://www.zhihu.com/explore')
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input)
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# # 跳到对于的iframe 的 id 中
# source = browser.find_element_by_css_selector('#draggable')
# print(source)
# try:
#     logo = browser.find_element_by_class_name('logo')
# except NoSuchElementException:
#     print('NO LOGO')
# browser.switch_to.parent_frame()
# logo = browser.find_element_by_class_name('navbar-header')
# #突然想通了 一个标签指定多个class 用 空格分开
# print(logo)
# print(logo.text)
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# logo = browser.find_elements_by_tag_name('body span')
# for x in logo:
#     print(x.text)
# browser.get('https://www.zhihu.com/explore')
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# browser.execute_script('alert("To Bottom")')
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# source = browser.find_element_by_css_selector('#draggable')
# target = browser.find_element_by_css_selector('#droppable')
# actions = ActionChains(browser)
# actions.drag_and_drop(source, target)
# actions.perform()
# browser.get('https://www.taobao.com')
#input = browser.find_element_by_id('kw')
#input.send_keys('Python')#搜索
#input.send_keys(Keys.ENTER)#键盘点击enter
# input = browser.find_element_by_id('q')
# input.send_keys('iPhone')
# time.sleep(1)
# input.clear()
# input.send_keys('iPad')
# button = browser.find_element_by_class_name('btn-search')
# button.click()
# input_first = browser.find_element_by_id('q')
#input_first.send_keys("火影",Keys.ENTER)
# input_second = browser.find_element_by_css_selector('#q')
# input_third = browser.find_element_by_xpath('//*[@id="q"]')
# print(input_first, input_second, input_third)
# #wait = WebDriverWait(browser, 10)
# #wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
# print(browser.current_url)
# print(browser.get_window_size())
# #print(browser.get_cookies())
# #print(browser.page_source)
# lis = browser.find_elements_by_css_selector('.service-bd li a')
# print(lis)
# print()
# time.sleep(10)
# browser.close()