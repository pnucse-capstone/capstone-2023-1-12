import csv
from os.path import dirname, realpath

# Open Brand
org_path = dirname(realpath(__file__).replace("\\", "/"))
def get_category_data(csv_file_path):
    csv_full_path = '/'.join([org_path, csv_file_path])
    with open(csv_full_path, "r", newline="", encoding='utf-8-sig') as csvfile:
        csvreader = csv.reader(csvfile)
        data = list(csvreader)
    return data

category_data = get_category_data('brand_category.csv')
print(category_data)

csv_recent_count = len(get_category_data('write.csv'))
f = open('/'.join([org_path, 'write.csv']), "a", newline="", encoding='utf-8-sig')
wr = csv.writer(f)

import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

import time
import re

options = webdriver.ChromeOptions()
# options.add_argument("headless")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
options.add_argument("--blink-settings=imagesEnabled=false")
w, h = 1920, 1080
driver = webdriver.Chrome(options=options)
driver.set_window_size(w, h)
driver.set_script_timeout(5)

wait = WebDriverWait(driver, 10)

total_count = 0
for mainname, subname in category_data[1:]:
    url = f'https://myfranchise.kr/category/contents/{mainname}/{subname}'
    driver.get(url)
    time.sleep(3)
    
    xpath = '//*[@id="category-container"]/div/p'
    element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

    text = driver.find_element(By.XPATH, xpath).text 
    count = re.findall(r'\d+', text)
    count = int(''.join(count)) if count else 0

    print(count)
    if (csv_recent_count >= total_count+count):
        total_count += count
        continue

    for i in range((count-1)//24+1):
        if (csv_recent_count >= total_count+24):
            total_count += 24
            continue
        time.sleep(2)

        url2 = f'{url}?page={i+1}'
        driver.get(url2)

        time.sleep(2)

        # wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'css-0')))
        try:
            element2 = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'css-0')))
        except:
            element2 = driver.find_element(By.CLASS_NAME, 'css-0')
    
        time.sleep(1)
        # element2 = driver.find_element(By.CLASS_NAME, 'css-0')
        buttons  = element2.find_elements(By.CLASS_NAME, 'css-1d3w5wq')

        limit = len(buttons)

        for button in buttons:
            if (csv_recent_count >= total_count+1):
                total_count += 1
                continue
            brand_name  = button.find_element(By.CLASS_NAME, 'brandName').text
            brand_count_texts = button.find_elements(By.CLASS_NAME, 'css-xqf0v7')
            brand_count_text = brand_count_texts[1].text if len(brand_count_texts) >= 2 else ''
            brand_count = re.findall(r'\d+', brand_count_text)
            brand_count = int(''.join(brand_count)) if brand_count else 0
            info_list = [mainname, subname, brand_name, brand_count]
            print(info_list)
            wr.writerow(info_list)

f.close()

    # for i in range((count-1)//24+1):
    #     time.sleep(1)
    #     url2 = f'{url}?page={i+1}'
    #     driver.get(url2)

    #     xpath2 = '//*[@id="category-container"]/div/div[5]'
    #     element2 = driver.find_element(By.XPATH, xpath2)
    #     buttons  = element2.find_elements(By.CLASS_NAME, 'css-1d3w5wq')

    #     limit = len(buttons)

    #     for i in range(limit):
    #         driver.find_element(By.XPATH, xpath2)\
    #               .find_elements(By.CLASS_NAME, 'css-1d3w5wq')[i].click()

    #         time.sleep(5)

    #         driver.get(url2)
    #         wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    #         time.sleep(1)

