"""

target_list 식당 중에서 프랜차이즈 식당을 찾아 franchise_list.csv 파일에
프랜차이즈의 목록을 저장한다.

"""
import csv
import pandas as pd


restaurant_names = []
restaurant_category = []
franchise_restaurants = []

# CSV 파일을 읽어서 데이터 추출
with open('/root/youtube/restaurant_list/target_list.csv', 'r', newline='', encoding='utf-8') as csvfile:
    csvreader = csv.DictReader(csvfile)
    
    # 식당 이름만 추출하여 출력
    for row in csvreader:
        restaurant_names.append(row['이름'])
        
        if ' ' in row['이름']:
            parts = row['이름'].split(' ')
            franchise_restaurants.append(parts[0])
            restaurant_category.append(row['카테고리'])

with open('/root/youtube/restaurant_list/franchise_list.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["프렌차이즈", "카테고리"])  # 열 이름을 추가

    # name과 cate 리스트 데이터를 행으로 저장
    for i in range(len(franchise_restaurants)):
        csvwriter.writerow([franchise_restaurants[i], restaurant_category[i]])
