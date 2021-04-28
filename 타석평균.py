from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

# 드라이버 가져오기
driver = webdriver.Chrome('C://Users//gkfka//Downloads//chromedriver_win32//chromedriver.exe')

# 연도 리스트
list_year=['2018', '2019', '2020']

# 페이지 리스트
list_page = ['1', '2', '3']

# 검색결과 담을 리스트
searchList = []

sum = 0
count = 0

for year in list_year:
    for page in list_page:
        # 사이트 열기
        url = driver.get('http://www.kbreport.com/leader/main?order=oWAR&orderType=DESC&teamId=&defense_no=&year_from='+year+'&year_to='+year+'&gameType=R&split01=&split02_1=&split02_2=&r_tpa_count=&tpa_count=0#/'+page)

        # 년 선텍
        driver.find_element_by_xpath("//select[@class='page-row-num']/option[@value='100']").click()

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        tblSchedule = soup.find('table', {'class': 'ltb-table responsive'})
        trs = tblSchedule.find_all('tr')
        for idx,tr in enumerate(trs):
            if idx > 0:
                tds = tr.find_all('td')
                print(tds[0].text.strip(), tds[4].text.strip())
                sum += int(tds[4].text.strip())
                count += 1


average = sum/count
print(average)

'''
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

# 드라이버 가져오기
driver = webdriver.Chrome('C://Users//gkfka//Downloads//chromedriver_win32//chromedriver.exe')

# 연도 리스트
list_year=['2018', '2019', '2020']

# 페이지 리스트
list_page = ['1', '2', '3']

# 검색결과 담을 리스트
searchList = []

for year in list_year:
    for page in list_page:
        # 사이트 열기
        url = driver.get('http://www.kbreport.com/leader/main?order=oWAR&orderType=DESC&teamId=&defense_no=&year_from='+year+'&year_to='+year+'&gameType=R&split01=&split02_1=&split02_2=&r_tpa_count=&tpa_count=0#/'+page)

        # 년 선텍
        driver.find_element_by_xpath("//select[@class='page-row-num']/option[@value='100']").click()

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        tblSchedule = soup.find('table', {'class': 'ltb-table responsive'})
        trs = tblSchedule.find_all('tr')
        for idx,tr in enumerate(trs):
            if idx > 0:
                tds = tr.find_all('td')
                print(tds[0].text.strip(), tds[4].text.strip())

'''