from krwordrank.hangle import normalize
from krwordrank.word import KRWordRank
from konlpy.tag import Okt
import openai
from collections import Counter
import pandas as pd


#각 리뷰들을 분석해 자주 보이는 키워드 뽑아내는 코드

openai.api_key = "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"

def gpt(question):
    messages = []
    # user_content = input("user : ")
    messages.append({"role": "user", "content": f"{question}"})
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    assistant_content = completion.choices[0].message["content"].strip()
    messages.append({"role": "assistant", "content": f"{assistant_content}"})
    print(f"GPT : {assistant_content}")

menu = ['돈까스', '피자', '치킨', '파스타', '흑돼지', '버거', '수제', '삼겹살', '국물', '초밥', '국밥']
ingred = ['면', '국물']
taste = ['시원','시원한', '신선한','따뜻','건강','풍미','진한','부드러운','이국','고소','배부']
atmosphere = ['편한', '고급']
service = ['친절', '정성']
price = ['가성비','혜자']
alls = []
menu_all = []
taste_all = []
atmosphere_all = []
service_all = []
price_all =[]


def blog_keyword(restaurant_name):
    texts_blog = open(f"shal/{restaurant_name} 블로그 리뷰.txt", encoding="utf8")
    # texts = open("all.txt", encoding="utf8")
    texts_blog = [normalize(text, english=True, number=True) for text in texts_blog]

    okt = Okt()
        # pos_tags = okt.pos(texts, norm=True, stem=True)
        # adjectives = [word for word, pos in pos_tags if pos == 'Adjective']
        
    
    wordrank_extractor = KRWordRank(
            min_count = 5, # 단어의 최소 출현 빈도수 (그래프 생성 시)
            max_length = 10, # 단어의 최대 길이
            verbose = True
    )
    beta = 0.85    # PageRank의 decaying factor beta
    max_iter = 10
    keywords, rank, graph = wordrank_extractor.extract(texts_blog, beta, max_iter)
    words = []
    for word, r in sorted(keywords.items(), key=lambda x:x[1], reverse=True):
        words.append(word)
    
    # gpt(f"다음은 한 식당에 관한 리뷰에서 따온 키워드들이야.[{words[0:30]}] 이 중 식당의 대표메뉴 이름으로 추정되는 것 한개만 뽑아줘. ex) '대표메뉴1' 이렇게 이름만 표시해. 다른 설명 없이.")
    
    menu2 = []
    taste2 = []
    atmosphere2 = []
    service2 = []
    price2 = []
    
    for i in words:
        if i in menu:
            menu2.append(i)

        if i in taste:
            taste2.append(i)
            
        if i in atmosphere:
            atmosphere2.append(i)
            
        if i in service:
            service2.append(i)
    
        if i in price:
            price2.append(i)
        
        
    # print(words)   

    # print("메뉴 : ", menu2)
    # print("맛 : ", taste2)
    # print("매장 분위기 : ", atmosphere2)
    # print("서비스 : ", service2)
    # print("가격 : ", price2)
            
    for i in menu2:
        alls.append(i)
    for i in taste2:
        alls.append(i)
    for i in atmosphere2:
        alls.append(i)
    for i in service2:
        alls.append(i)
    for i in price2:
        alls.append(i)
        
    
    
    
def comment_keyword(restaurant_name):
    df = pd.read_csv(f"shal/{restaurant_name} 댓글 리뷰.csv")
    texts = df["Review"].tolist()


    okt = Okt()
        # pos_tags = okt.pos(texts, norm=True, stem=True)
        # adjectives = [word for word, pos in pos_tags if pos == 'Adjective']
    wordrank_extractor = KRWordRank(
            min_count = 10, # 단어의 최소 출현 빈도수 (그래프 생성 시)
            max_length = 10, # 단어의 최대 길이
            verbose = True
    )
    beta = 0.85    # PageRank의 decaying factor beta
    max_iter = 10
    keywords, rank, graph = wordrank_extractor.extract(texts, beta, max_iter)
    words = []
    for word, r in sorted(keywords.items(), key=lambda x:x[1], reverse=True):
        words.append(word)
        

        
    menu2 = []
    taste2 = []
    atmosphere2 = []
    service2 = []
    price2 = []
    for i in words:
        if i in menu:
            menu2.append(i)

        if i in taste:
            taste2.append(i)
            
        if i in atmosphere:
            atmosphere2.append(i)
            
        if i in service:
            service2.append(i)
            
        if i in price:
            price2.append(i)
        
        
    # print(words)   

    # print("메뉴 : ", menu2)
    # print("맛 : ", taste2)
    # print("매장 부누이기 : ", atmosphere2)
    # print("서비스 : ", service2)
    # print("가격 : ", price2)
            
    for i in menu2:
        if i in alls:
            continue
        else:    
            alls.append(i)
    for i in taste2:
        if i in alls:
            continue
        else:    
            alls.append(i)
    for i in atmosphere2:
        if i in alls:
            continue
        else:    
            alls.append(i)
    for i in service2:
        if i in alls:
            continue
        else:    
            alls.append(i)
    for i in price2:
        if i in alls:
            continue
        else:    
            alls.append(i)
        

name = "만게츠"
blog_keyword(name)
comment_keyword(name)

for i in alls:
    if i == "부드":
        index = alls.index(i)
        alls[index] = "부드러운"
    if i == "이국":
        index = alls.index(i)
        alls[index] = "이국적인"
    if i == "건강":
        index = alls.index(i)
        alls[index] = "건강한"
    if i == "고소":
        index = alls.index(i)
        alls[index] = "고소한"
    if i == "따뜻":
        index = alls.index(i)
        alls[index] = "따뜻한"
        
if "시원" in alls and "따뜻" in alls:
    alls.remove("따뜻")
        

print("alls : ", alls)
question = f"다음은 식당 {name} 리뷰를 분석해 나온 키워드 모음이야. '{alls}. 한 줄로 이 식당에 대한 묘사를 해줘. '"
# print(gpt(question))
    
# adj_words = []
# for word in words:
#     pos = okt.pos(word)
#     pos_tags = [tag for _, tag in pos]
#     if 'Adjective' in pos_tags or 'Adverb' in pos_tags:
#         adj_words.append(word)  
# print(adj_words)
    
# for i in words_remove:
#     if i in words:
#         words.remove(i)

# print("top 20 words\n")
# print(top_20_words)