import requests
from bs4 import BeautifulSoup

# 1. 원하는 주소로 요청을 보재 응답을 저장한다.

html = requests.get('https://finance.naver.com/sise/').text
soup = BeautifulSoup(html, 'html.parser')
kospi = soup.select_one('#KOSPI_now').text

print(kospi)