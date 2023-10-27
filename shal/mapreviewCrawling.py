from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
import pandas as pd

# Chrome 드라이버 경로 설정 (자신의 환경에 맞게 수정)
# 웹 드라이버 초기화
driver = webdriver.Chrome()

# 네이버 지도 리뷰 페이지 열기
url = "https://pcmap.place.naver.com/restaurant/33061157/review/visitor"
driver.get(url)

# 리뷰 데이터 크롤링
reviews = []

while True:
    try:
        # 더보기 버튼이 나타날 때까지 기다림 (최대 10초 대기)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'lfH3O')))
        time.sleep(1)  # 3초 대기

        # 더보기 버튼 클릭
        more_button = driver.find_element(By.CLASS_NAME, 'lfH3O')
        more_button.click()
    except Exception:
        break

# 페이지 소스 가져오기
page_source = driver.page_source

# BeautifulSoup를 사용하여 페이지 파싱
soup = BeautifulSoup(page_source, 'html.parser')

# 리뷰 텍스트 추출
review_elements = soup.find_all('span', class_='zPfVt')
for review_element in review_elements:
    reviews.append(review_element.text)

# 데이터프레임 생성
df = pd.DataFrame({'Review': reviews})

# CSV 파일로 저장
df.to_csv('스시심 댓글 리뷰.csv', index=False)

# 브라우저 종료
driver.quit()
