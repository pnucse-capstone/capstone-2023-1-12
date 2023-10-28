"""
category_keyword 에는 키워드와 해당 키워드와 관련 있는 식당의 목록이 저장되어 있음

해당 py 파일은
category_keyword 에 있는 내용을 읽어 Youtube api 를 이용해
식당 이름을 Youtube에 검색했을 때 나오는 영상들의 정보를 추출한다.
"""

import csv
import os
import pandas as pd
from googleapiclient.discovery import build

api_key = "INSERT YOUR API KEY"     # API 키

youtube = build("youtube", "v3", developerKey=api_key)      # YouTube Data API 클라이언트 생성

def youtube_api(keyword, category):
    url_list = []
    
    csv_filename = '/root/youtube/result_csv/original_csv/' + category + '.csv'
    csv_file = open(csv_filename, 'a', newline='', encoding='utf-8')
    csv_writer = csv.writer(csv_file)
    res_data_list = [keyword]
    
    new_keyword = "부산대 " + keyword
    search_response = youtube.search().list(
        q=new_keyword,  # 검색 내용
        order="relevance",  # 검색결과 정렬기준 relevance
        part="snippet",  # video에 대한 정보를 받고 싶으면 snippet / 그렇지 않으면 id
        maxResults=3  # 검색결과
    ).execute()

    for search_result in search_response.get("items", []):
        if 'id' in search_result and 'videoId' in search_result['id']:
            video_id = search_result['id']['videoId']  # 비디오 id
        else:
            continue
        videos_stats = youtube.videos().list(part="snippet, cont    entDetails, statistics", id=video_id).execute()

        for video in videos_stats['items']:
            video_title = video['snippet']['title']
            if keyword not in video_title:
                continue  # 키워드가 제목에 포함되지 않으면 다음 영상으로 넘어감
            url = video['id']     
            url_list.append(url)
            
            # youtube 영상 관련 데이터를 csv 파일에 추가
            youtube_url = "https://www.youtube.com/watch?v=" + str(url)
            viewCount = str(video['statistics']['viewCount']) if 'viewCount' in video['statistics'] else '0'  # 조회수
            likeCount = str(video['statistics']['likeCount']) if 'likeCount' in video['statistics'] else '0'  # 좋아요수
            commentCount = str(video['statistics']['commentCount']) if 'commentCount' in video['statistics'] else '0'  # 댓글수                
            res_data_list.append(f"{keyword},{youtube_url},{viewCount},{likeCount},{commentCount},{0},{0},{0}")
            
    new_search_response = youtube.search().list(
        q=keyword,  # 검색 내용
        order="relevance",  # 검색결과 정렬기준 relevance
        part="snippet",  # video에 대한 정보를 받고 싶으면 snippet / 그렇지 않으면 id
        maxResults=2  # 검색결과
    ).execute()

    for search_result in new_search_response.get("items", []):
        if 'id' in search_result and 'videoId' in search_result['id']:
            video_id = search_result['id']['videoId']  # 비디오 id
        else: continue
        videos_stats = youtube.videos().list(part="snippet, contentDetails, statistics", id=video_id).execute()

        for video in videos_stats['items']:
            video_title = video['snippet']['title']
            if keyword not in video_title:
                continue  # 키워드가 제목에 포함되지 않으면 다음 영상으로 넘어감
            url = video['id']
            video_title = video['snippet']['title']

            # 동일한 url이 이미 있는지 검사
            url_check = False
            for k in range(len(url_list)) :
                if(url_list[k] == url) :
                    url_check = True
                    break
            
            if url_check == True : break
            else : url_list.append(url)
            
            # youtube 영상 관련 데이터를 csv 파일에 추가
            youtube_url = "https://www.youtube.com/watch?v=" + str(url)
            viewCount = str(video['statistics']['viewCount']) if 'viewCount' in video['statistics'] else '0'  # 조회수
            likeCount = str(video['statistics']['likeCount']) if 'likeCount' in video['statistics'] else '0'  # 좋아요수
            commentCount = str(video['statistics']['commentCount']) if 'commentCount' in video['statistics'] else '0'  # 댓글수
            res_data_list.append(f"{keyword},{youtube_url},{viewCount},{likeCount},{commentCount},{0},{0},{0}")
    
    csv_writer.writerow(res_data_list)
    csv_file.close()

def main() :
    res_list = '/root/youtube/restaurant_list/target_list2.csv'
    res_list = pd.read_csv(res_list)
    names = res_list['이름']
    categories = res_list['카테고리']
    
    for i in range(len(names)):
        youtube_api(names[i], categories[i])  

if __name__ == '__main__':
    main()