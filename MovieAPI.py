#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import json
import pandas as pd

url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=430156241533f1d058c603178cc3ca0e&targetDt=20200205&itemPerPage=5"
res = requests.get(url)
text = res.text

d = json.loads(text)
# print(d)
movie = []
for b in d["boxOfficeResult"]["dailyBoxOfficeList"]:
    movie.append([b["rank"], b["rankOldAndNew"], b["movieCd"], b["movieNm"], b["salesAmt"], b["audiCnt"]])

    
    
data = pd.DataFrame(movie)
data
# print(d)


# boxofficeType 박스오피스 종류
# showRange 박스 오피스 조회 일자를 출력
# rnum 순번을 출력
# rank 해당일지의 박스오피스 순위를 출력
# rank 전일 대비 순위의 증감분을 출력
# rankOldAndNew 랭킹에 신규진입 여부를 출력 "OLD": ㄱㅣ존, "NEW": 신규
# MovieCd 영화의 대표코드를 출력
# MoiveNm 영화명 국문을 출력합니다.
# openDt 영화의 개봉일을 출력합니다.
# salesAmt 해당일의 매출액을 출력합니다.
# salesShare 해당일자 상영작의 매출 총액 대비 해당 영화의 매출 비율을 출력
# salesChange 전일 대비 매출액 증감 비율을 출력
# salesAcc 누적 매출액
# audiCnt 해당일의 관객수
# audiChange 전일 대비 관객수 증감 비율을 출력
# audiAcc 누적관객수를 출력
# scrnCnt ㅎㅐ당일자에 상영한 스크린수를 출력
# showCnt 해당일자에 상영된 횟수를 출력


# In[16]:





# In[ ]:




