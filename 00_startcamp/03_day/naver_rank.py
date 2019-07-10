import requests
from bs4 import BeautifulSoup

# 요청 보내서 html 파일 받고
url = 'https://www.naver.com'

html = requests.get(url).text

# 뷰숲으로 정제
soup = BeautifulSoup(html, 'html.parser')

# slect 메서드로 사용해서 list 를 얻어낸다.
rank_list = '#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k'
searchs = soup.select(rank_list)

# 뽑은 list 를 with 구문으로 잘 작성하기.
with open('example.txt', 'w', encoding='utf-8') as f:
    for search in searchs:
        f.write(search.text + '\n')