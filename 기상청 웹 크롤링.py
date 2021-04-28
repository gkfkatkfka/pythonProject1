from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time


# 드라이버 가져오기
driver = webdriver.Chrome('C://Users//gkfka//Downloads//chromedriver_win32//chromedriver.exe')

# 사이트 열기
url=driver.get('https://data.kma.go.kr/data/lwi/lwiRltmList.do?pgmNo=635')

# 불쾌지수 클릭
driver.find_element_by_xpath("//select[@id='idxCode']/option[text()='불쾌지수']").click()

# 날짜 지우고 입력
driver.find_element_by_xpath("//input[@id='startDt']").send_keys("\b\b\b\b\b\b\b\b20180614")

# 시간
driver.find_element_by_xpath("//select[@id='startHh']/option[@value='00']").click()


# 스크롤 대상 지정
box = driver.find_element_by_id('stnArea')

# 지역 선택
driver.find_element_by_id("ztree_983_switch").click()
box.send_keys(Keys.PAGE_DOWN)
time.sleep(2)
driver.find_element_by_id("ztree_1034_switch").click()
box.send_keys(Keys.PAGE_DOWN)
time.sleep(2)
driver.find_element_by_id("ztree_1039_check").click()

# 조회 버튼 클릭
driver.find_element_by_xpath("//button[@title='조 회']").click()

# 표 가져오기
searchList = []

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
tblSchedule = soup.find('table', {'class': 'tbl'})
tbody = tblSchedule.find('tbody')
trs = tbody.find_all('tr')

for idx, tr in enumerate(trs):
    tds = tr.find_all('td')
    temp = [tds[0].text.strip(), tds[5].text.strip(), tds[6].text.strip(), tds[7].text.strip()]
    searchList.append(temp)

# csv 만들기
data = pd.DataFrame(searchList)
data.columns = ['place', '12', '15', '18']
data.head()
data.to_csv('테스트시간.csv', encoding='cp949')





'''
# 문학
driver.find_element_by_id("ztree_822_switch").click()
driver.find_element_by_id("ztree_847_switch").click()
box.send_keys(Keys.PAGE_DOWN)
time.sleep(2)
driver.find_element_by_id("ztree_868_check").click()

# 잠실
driver.find_element_by_id("ztree_2_switch").click()
box.send_keys(Keys.PAGE_DOWN)
time.sleep(2)
driver.find_element_by_id("ztree_405_switch").click()
box.send_keys(Keys.PAGE_DOWN)
time.sleep(2)
driver.find_element_by_id("ztree_428_check").click()

# 고척
driver.find_element_by_id("ztree_2_switch").click()
box.send_keys(Keys.PAGE_DOWN)
time.sleep(2)
driver.find_element_by_id("ztree_279_switch").click()
box.send_keys(Keys.PAGE_DOWN)
time.sleep(2)
driver.find_element_by_id("ztree_287_check").click()

# 수원
box.send_keys(Keys.PAGE_DOWN)
time.sleep(2)
driver.find_element_by_id("ztree_1249_switch").click()
driver.find_element_by_id("ztree_1250_switch").click()
box.send_keys(Keys.PAGE_DOWN)
time.sleep(2)
driver.find_element_by_id("ztree_1258_check").click()

# 사직
driver.find_element_by_id("ztree_452_switch").click()
box.send_keys(Keys.PAGE_DOWN)
time.sleep(2)
driver.find_element_by_id("ztree_523_switch").click()
box.send_keys(Keys.PAGE_DOWN)
time.sleep(2)
driver.find_element_by_id("ztree_531_check").click()

# 대전
driver.find_element_by_id("ztree_1084_switch").click()
box.send_keys(Keys.PAGE_DOWN)
time.sleep(2)
driver.find_element_by_id("ztree_1102_switch").click()
box.send_keys(Keys.PAGE_DOWN)
time.sleep(2)
driver.find_element_by_id("ztree_1110_check").click()

# 청주
box.send_keys(Keys.PAGE_DOWN)
time.sleep(2)
driver.find_element_by_id("ztree_2064_switch").click()
driver.find_element_by_id("ztree_2079_switch").click()
box.send_keys(Keys.PAGE_DOWN)
time.sleep(2)
driver.find_element_by_id("ztree_2082_check").click()

# 마산
box.send_keys(Keys.PAGE_DOWN)
time.sleep(2)
driver.find_element_by_id("ztree_3391_switch").click()
driver.find_element_by_id("ztree_3426_switch").click()
box.send_keys(Keys.PAGE_DOWN)
time.sleep(2)
driver.find_element_by_id("ztree_3433_check").click()

# 광주
driver.find_element_by_id("ztree_983_switch").click()
box.send_keys(Keys.PAGE_DOWN)
time.sleep(2)
driver.find_element_by_id("ztree_1034_switch").click()
box.send_keys(Keys.PAGE_DOWN)
time.sleep(2)
driver.find_element_by_id("ztree_1039_check").click()


# 대구
# 관할은 고산2동이라서 고산 2동으로 선정
driver.find_element_by_id("ztree_674_switch").click()
box.send_keys(Keys.PAGE_DOWN)
time.sleep(2)
driver.find_element_by_id("ztree_765_switch").click()
box.send_keys(Keys.PAGE_DOWN)
time.sleep(2)
driver.find_element_by_id("ztree_787_check").click()

"울산"
driver.find_element_by_id("ztree_1169_switch").click()
box.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
driver.find_element_by_id("ztree_1184_switch").click()
box.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
driver.find_element_by_id("ztree_1194_check").click()

'''
