from selenium import webdriver
import bs4
import time
import re
import pandas as pd

def searching(word):        #특정 검색어에 따른 주소 만들기
    url = 'https://www.instagram.com/explore/tags/' + word
    return url

#def select_first(driver):   #첫 게시물 여는 함수
#    first = driver.find_element_by_css_selector("div._9AhH0")
#    first.click()
#    time.sleep(3)

driver = webdriver.Chrome('c:\chromedriver.exe')
driver.get('https://www.instagram.com')
time.sleep(2)

email = '인스타 아이디'       #인스타그램 로그인  #<직장인을 위한 데이터 분석 실무> 참고
input_id = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[0]
input_id.clear()
input_id.send_keys(email)

password = '인스타 비밀번호'
input_pw = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[1]
input_pw.clear()
input_pw.send_keys(password)
input_pw.submit()

time.sleep(2)       #검색어 입력
word = '검색어'
url = searching(word)
driver.get(url)
time.sleep(2)
