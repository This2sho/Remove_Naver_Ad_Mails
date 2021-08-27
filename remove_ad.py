#-*- coding: utf-8 -*-
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import pyperclip
import time
URL = 'https://nid.naver.com/nidlogin.login?url=http%3A%2F%2Fmail.naver.com%2F'

options = webdriver.ChromeOptions()
options.add_argument('lang=ko_KR')
driver = webdriver.Chrome(executable_path='chromedriver', options=options)
driver.get(url=URL)

login_id = ''
login_pw = ''

#login form
tag_id = driver.find_element_by_name('id')
tag_pw = driver.find_element_by_name('pw')
tag_id.clear()
time.sleep(0.5)

#input id
tag_id.click()
pyperclip.copy(login_id)
tag_id.send_keys(Keys.CONTROL, 'v')
time.sleep(0.5)

#input pw
tag_pw.click()
pyperclip.copy(login_pw)
tag_pw.send_keys(Keys.CONTROL, 'v')
time.sleep(0.5)

#login button click
login_btn = driver.find_element_by_id('log.login')
login_btn.click()
time.sleep(0.5)
register_btn = driver.find_element_by_id('new.save')
register_btn.click()

#ad search
search_box = driver.find_element_by_id('searchKeyWord')
key = u"광고"
search_box.send_keys(key)
search_btn = driver.find_element_by_id('searchBtn')
search_btn.click()
time.sleep(0.5)

#check all and Delete
while True:
    time.sleep(0.5)
    num = driver.find_element_by_class_name('schMail').get_attribute('textContent')
    if  (num != '(0)'): 
        driver.find_element_by_id('mailCheckAll').click()
        driver.find_element_by_xpath('//*[@id="listBtnMenu"]/div[1]/span[2]/button[2]').click()
    else:
        break

print("Ad Remove Complete!")