#Joseon Dynasty Silok Scraper


print("JDS Scraper")

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
driver.quit()

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
# dataId=ITKC_JT_A0 이런식으로 이어지는것 발견, 확인해서 쓰면 좋을듯.
# 실록 월 일 등 어디까지 가져올 것인지?


# 태조실록 총서 첫번째 링크는 다음과 같음
# https://db.itkc.or.kr/dir/item?itemId=JT#dir/node?grpId=&itemId=JT&gubun=book&depth=3&cate1=&cate2=&dataGubun=%EC%B5%9C%EC%A2%85%EC%A0%95%EB%B3%B4&dataId=ITKC_JT_A0_000_000_000_00010
# 순서대로 00010부터 출발
# 총서나 부록은 따로 긁고, 나머지 누구 몇년 몇월에 따라 최종정보만 긁어오는 식으로 하면 될듯
# 나머지도 최종정보로 긁는 편이 좋을듯
