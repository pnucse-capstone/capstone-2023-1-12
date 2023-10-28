import os
import pandas as pd
import csv
from googleapiclient.discovery import build
from ultralytics import YOLO
from pytube import YouTube
from pytube.exceptions import AgeRestrictedError, VideoPrivate, VideoUnavailable
import argparse
import cv2
import requests
import time

def yolo(category):
    print(category, " 학습 데이터를 이용해 Detection을 시작합니다")
    
    yolo_path = "/root/youtube/runs/detect/" + category + "/weights/best.pt" # 학습 데이터 경로
    video_path = "/root/youtube/video_download/new_video.mp4"

    model = YOLO(yolo_path)
    results = model.predict(source = video_path, stream=True)
    
    frame_len = 0
    food_count = 0

    for result in results:
        count = [0] * len(model.names)
        
        for c in result.boxes.cls:
            count[int(c)] += 1
        frame_len += 1

        for i in range(len(count)):
            food_count += count[i]

    print("Dection이 성공적으로 마무리 되었습니다. 결과 값을 반환합니다")

    return frame_len, food_count

def video_download(category, url, cookies):
    print(url, "에서 영상 다운로드를 시작합니다")
    response = requests.get(url, cookies=cookies)
    if response.status_code == 200:
        yt = YouTube(url)
        try: data = yt.streams.filter(res="720p").first()
        except Exception as e: return 0, 0
        if data is None: return 0, 0
    else : return 0,0
    
    download_folder = "/root/youtube/video_download/"
    data.download(output_path=download_folder, filename="original.mp4")

    # 입력 MP4 파일 경로
    input_video_path = "/root/youtube/video_download/original.mp4"
    output_video_path =  "/root/youtube/video_download/new_video.mp4"

    # 샘플링할 프레임 간격 설정 (예: 2프레임마다 샘플링)
    frame_interval = 10

    # OpenCV 비디오 캡처 객체 생성
    cap = cv2.VideoCapture(input_video_path)

    # 비디오의 속성 가져오기 (프레임 크기, FPS 등)
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    fps = int(cap.get(5))

    # 출력 비디오 설정
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 코덱 설정
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

    frame_no = 0  # 프레임 번호

    while True:
        ret, frame = cap.read()
        if not ret:
            break  # 비디오 종료

        frame_no += 1

        if frame_no % frame_interval == 0:  # 프레임 샘플링
            out.write(frame)

    cap.release()  # 비디오 캡처 객체 해제
    out.release()  # 출력 비디오 객체 해제
    cv2.destroyAllWindows()  # 창 닫기
    
    print(url, "영상의 프레임 조정을 완료했습니다")
    
    frame_len, food_count = yolo(category)
    
    os.remove(input_video_path)
    os.remove(output_video_path)
    
    print("영상 삭제가 완료되었습니다. 결과 값을 반환합니다")
    
    return frame_len, food_count
    
def main():
    cookies = {
        "PREF": "f4=4000000&tz=Asia.Seoul&f5=20000",
        "VISITOR_INFO1_LIVE": "CgJLUhICGgA%3D"
    }   
    
    category = ["chicken", "sushi"]

    for i in range(len(category)):    
        csv_file_path = '/root/youtube/result_csv/original_csv/' + category[i] + '.csv' # 리스트로 사용할 csv 파일 선택

        last = 0
        with open(csv_file_path, 'r', newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            data = list(csv_reader)
        
        for row in data:
            new_data = [row[0]]
            contents = row[1:]

            # if (category[i] == "pasta") and (row[0] == "디노이레스토랑"): last = 1
            # if (category[i] == "burger") and (row[0] == "그린그린"): last = 1
            if (category[i] == "chicken") and (row[0] == "호호닭집"): last = 1
            if (category[i] == "sushi") and (row[0] == "대양회직판장"): last = 1
            # if (category[i] == "pizza") and (row[0] == "NONONODATA"): last = 1
            if last == 0: continue

            for j in range(len(contents)):
                data = contents[j].replace('"', '')
                res_data = data.split(',')
                
                print(category[i]," 카테고리 - ",res_data[0]," 식당의", res_data[1], " url에 대한 Detection을 수행합니다")

                url = res_data[1]
                frame_len, food_count = video_download(category[i], url, cookies)
                res_data[5] = str(frame_len)  # 5번째 요소를 문자열로 변환
                res_data[6] = str(food_count)  # 6번째 요소를 문자열로 변환

                # 수정된 res_data를 기존 데이터로 대체
                new_data.append(','.join(res_data))  # 1을 더한 이유는 첫 열(식당 이름)을 제외하기 위함

            yolo_file_path = '/root/youtube/result_csv/yolo_csv/yolo_' + category[i] + '.csv' # 리스트로 사용할 csv 파일 선택
            with open(yolo_file_path, 'a', newline='', encoding='utf-8') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(new_data)
            
if __name__ == '__main__':
    main()
    
    
        