from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

# 드라이버 가져오기
driver = webdriver.Chrome('C://Users//gkfka//Downloads//chromedriver_win32//chromedriver.exe')
# 사이트 열기
url=driver.get('https://www.koreabaseball.com/Schedule/Schedule.aspx')

# 정규 시즌 콤보 박스 클릭
driver.find_element_by_xpath("//select[@id='ddlSeries']/option[text()='KBO 정규시즌 일정']").click()

# 팀 선택
driver.find_element_by_xpath("//ul[@class='tab-schedule']/li[@attr-value = 'HH']").click()

'''
# 년 선텍
driver.find_element_by_xpath("//select[@id='ddlYear']/option[@value='2018']").click()
'''
'''
# 달 선텍
driver.find_element_by_xpath("//select[@id='ddlMonth']/option[@value='05']").click()
'''

# 연도 리스트
list_year=['2018','2019','2020']

# 달 리스트
list_month = ['06', '07', '08', '09']

# 검색결과 담을 리스트
searchList = []

# 연도 반복
for year in list_year:
    # 연도 바꾸기
    driver.find_element_by_xpath("//select[@id='ddlYear']/option[text()='" + str(year) + "']").click()

    # 달 반복
    for month in list_month:
        # 달 선택
        driver.find_element_by_xpath("//select[@id='ddlMonth']/option[text()='"+str(month)+"']").click()

        # 결과
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        tblSchedule = soup.find('table', {'class': 'tbl'})
        trs = tblSchedule.find_all('tr')
        for idx, tr in enumerate(trs):
            if idx > 0:
                tds = tr.find_all('td')
                if len(tds)==8:
                    tds.insert(0,searchList[-1][0])
                    temp = [tds[0], tds[1].text.strip(), tds[2].text.strip(), tds[3].text.strip(), tds[7].text.strip(), tds[8].text.strip()]
                else:
                    temp = [tds[0].text.strip(), tds[1].text.strip(), tds[2].text.strip(), tds[3].text.strip(), tds[7].text.strip(),tds[8].text.strip()]
                if tds[8].text.strip()=='-':
                    searchList.append(temp)

# csv 만들기
data = pd.DataFrame(searchList)
data.columns = ['day', 'time', 'play', 'relay', 'park','bigo']
data.head()
data.to_csv('모든정보.csv', encoding='cp949')


