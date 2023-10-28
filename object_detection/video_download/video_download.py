from pytube import YouTube
import os
import argparse
import cv2
import time

url = "https://www.youtube.com/watch?v=0Wwez-ytt08"
yt = YouTube(url)
data = yt.streams.filter(res="720p").first()
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
os.remove(input_video_path)