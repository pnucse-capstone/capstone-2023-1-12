import openai

api_key = "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"  # 본인의 API 키로 대체해야 합니다.
openai.api_key = api_key

def ask_gpt35_turbo(question):
    response = openai.Completion.create(
        engine="text-davinci-002",  # text-davinci-001 : 3.0, 002 : 3.5turbo, 003 - 4.0
        prompt=question,
        max_tokens=5,  # 출력할 최대 토큰 수를 조정.(i love pizza -> 3토큰)
        n=1,  # 생성할 답변 수를 지정합니다.
        stop=None,  # 특정 문자열로 생성을 중지하려면 여기에 추가합니다.
        temperature=0.7,  # 낮은 값은 보수적인 답변을, 높은 값은 다양한 답변을 생성합니다.
        frequency_penalty=0.2,  # 낮은 값은 더 다양한 답변을 생성합니다.
        presence_penalty=0.0,  # 높은 값은 반복을 줄입니다.
    )
    # 답변을 추출하고 반환합니다.
    answer = response.choices[0].text.strip()
    return answer

def  emotion():
    origin_text = open("shal/부산대 톤쇼우 리뷰.txt", encoding="utf8")
    positive     = open("shal/pos_pol_word.txt", encoding="utf8")
    negative    = open("shal/neg_pol_word.txt", encoding="utf8" )
    origin = origin_text.read()    # origin_text 를 문자형 변수 origin 에 담는다
    words = origin.split()
    pos =  positive.read().split('\n')  # 긍정단어를 엔터로 구분해서 리스트로 구성
    neg =  negative.read().split('\n')
    pos = list( filter( lambda  x : x, pos ) )
    neg = list( filter( lambda x : x, neg ) )
    pos1 = list( filter( lambda  x : True  if len(x) > 1  else  False, pos ) )
    neg1 = list( filter( lambda  x : True  if len(x) > 1  else  False, neg ) )
    # f2 = open("origin_pos.csv", "w", encoding="utf8")
    # f3 = open("origin_neg.csv", "w", encoding="utf8")
    pos1.remove('^^')
    pos_cnt = 0
    neg_cnt = 0
    pos_words=[]
    neg_words=[]
    
    for i in pos1:
        if i in origin:
            # print(i)
            # f2.write( i + ',' + str( origin.count(i) ) + '\n' )
            pos_words.append(i)
            pos_cnt += 1
                       
    for j in neg1:
        if j in origin:
            # print(j)
            # f3.write( i + ',' + str( origin.count(i) ) + '\n' )
            neg_words.append(j)
            neg_cnt += 1        
    
    # f2.close()
    # f3.close()   
    print("positive")
    print(pos_words)
    print("negaitive")
    print(neg_words)
    # rate = pos_cnt/(pos_cnt + neg_cnt)*100
    rate = pos_cnt / len(words) * 100
    print(f"pos_cnt : {pos_cnt}")
    print(f"neg_cnt : {neg_cnt}")
    print(f"rate : {rate}")





emotion()








    
    


