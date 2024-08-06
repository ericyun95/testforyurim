#Joseon Dynasty Silok Scraper
# 3.9.13('base': conda로 실행)

print("JDS Scraper")
import sys
import selenium
selenium.__version__
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# ChromeDriver 경로 설정
chrome_driver_path = '/Users/hyunwoongyun/Downloads/chromedriver-mac-x64/chromedriver'
# 제 3자 보안 설정 해줘야 열림
# ChromeDriver 서비스 설정
service = Service(chrome_driver_path)
service.start()

options = webdriver.ChromeOptions()
#안열리는 옵션은 잠시 끄기로 함
#options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)


# 2024/8/1 크롬드라이버 정상작동 확인
# 여기서부터 한국고전종합DB - https://db.itkc.or.kr/
# 크롬드라이버 사용이유 = API 사용시 전문 확보 불가


url = 'https://db.itkc.or.kr/'
driver.get(url)

# 사이트 로드 대기
time.sleep(3)  # 페이지가 완전히 로드될 때까지 잠시 대기

# 조선왕조실록으로 이동
driver.find_element(By.LINK_TEXT, '조선왕조실록').click()
time.sleep(3)
url2 = 'https://db.itkc.or.kr/dir/item?itemId=JT#dir/list?itemId=JT&gubun=book&pageIndex=1&pageUnit=50'
driver.get(url2)
# dataId=ITKC_JT_A0 이런식으로 이어지는것 발견, 확인해서 쓰면 좋을듯.
# 실록 월 일 등 어디까지 가져올 것인지?
book_list_box = driver.find_elements_by_xpath('/html/body/div[2]/section[2]/section[1]/div/div[2]/ul/li/ul')
# 서명
book_list = book_list_box[0].text.strip().split('\n ')
# 서명당 클릭후 복귀
for name in book_list:
    driver.find_element(By.LINK_TEXT, name).click()
    time.sleep(3)
    driver.back()
    time.sleep(3)

driver.quit()
driver.find_element(By.LINK_TEXT, book_list[0]).click()
lsttest = driver.find_elements_by_css_selector('tr')
lsttest[0].text
lsttest.pop(0)
len(lsttest)
# 총서 부록과 n년 텍스트 가져오는 코드는 달라야 함

# 태조실록 총서 첫번째 링크는 다음과 같음
# https://db.itkc.or.kr/dir/item?itemId=JT#dir/node?grpId=&itemId=JT&gubun=book&depth=3&cate1=&cate2=&dataGubun=%EC%B5%9C%EC%A2%85%EC%A0%95%EB%B3%B4&dataId=ITKC_JT_A0_000_000_000_00010
# 순서대로 00010부터 출발
# 총서나 부록은 따로 긁고, 나머지 누구 몇년 몇월에 따라 최종정보만 긁어오는 식으로 하면 될듯
# 나머지도 최종정보로 긁는 편이 좋을듯
# 수정: https://sillok.history.go.kr/search/inspectionMonthList.do 로 들어가는게 좋을지도?
# 여기는 클릭당 url은 안바뀌는데, 크롬드라이버의 클릭으로 돌리는 함수가 나오면 가능할까, 생각중. 지금은 보류


# 월에 들어가면 일자가 보이고, 일자 수를 받아서 클릭하는 함수
# 아래 full XPath
# /html/body/div[2]/section[2]/section[2]/section/div[2]/ul - 날짜리스트, 여기 안에 <li class> 마다 클릭
# /html/body/div[2]/section[2]/section[2]/section/div[3]/div[1] - para-block
# /html/body/div[2]/section[2]/section[2]/section/div[3]/div[1]/div[1] - 제목
# /html/body/div[2]/section[2]/section[2]/section/div[3]/div[1]/div[2] - 내용
