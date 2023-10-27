import time
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

video_url = 'https://www.youtube.com/watch?v=RWaKWlLPvg0&ab_channel=%ED%91%B8%EB%94%94%EB%A1%9C%EB%93%9CFoodieRoad'

driver = webdriver.Chrome('root/shal/webdriver')
driver.get(video_url)

# 스크롤 다운하여 댓글 로딩
SCROLL_PAUSE_TIME = 2
last_height = driver.execute_script("return document.documentElement.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

soup = BeautifulSoup(driver.page_source, 'html.parser')
comments = soup.find_all('yt-formatted-string', {'id': 'content-text'})

# 댓글을 CSV 파일로 저장
csv_filename = 'youtube_comments3.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['댓글'])

    for comment in comments:
        csv_writer.writerow([comment.text])

driver.quit()
