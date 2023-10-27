import pandas as pd
from konlpy.tag import Okt

# KoNLPy 형태소 분석기 초기화
okt = Okt()

# 댓글 데이터 파일 불러오기
df = pd.read_csv("shal/톤쇼우.csv", encoding="utf-8")
comments = df['댓글'].astype(str)

# 긍정적인 의미의 단어를 담은 사전 파일 불러오기
positive_words = set()
negative_words = set()
with open("pos_pol_word.txt", encoding="utf-8") as file:
    for line in file:
        word = line.strip()
        positive_words.add(word)

with open("neg_pol_word.txt", encoding="utf-8") as file:
    for line in file:
        word = line.strip()
        negative_words.add(word)

# 긍정적인 감성 단어 카운터 초기화
words_count = 0
positive_count = 0
negative_count = 0
pos_words=[]
neg_words = []
# total_word_count = len(df['댓글'].str.split().sum())
# print(total_word_count)

# 댓글에서 형태소 추출하고 긍정적인 단어 카운트
for comment in comments:
    words = okt.pos(comment)
    for word, pos in words:
        if word in positive_words:
            pos_words.append(word)
            positive_count += 1
    
        if word in negative_words:
            neg_words.append(word)
            negative_count +=1

# 결과 출력
print("positive_counts:", positive_count)
print(pos_words)
print("negative_counts:", negative_count)
print(neg_words)
rate = positive_count / (positive_count + negative_count) * 100
print("rate : ", round(rate,1),"%")