from flask import Flask, render_template, request
import requests
from decouple import config

app = Flask(__name__)

api_url = 'https://api.telegram.org'
token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')
naver_client_id = config('NAVER_CLIENT_ID')
naver_client_secret = config('NAVER_CLIENT_SECRET')

@app.route('/')
def hello():
    return 'hello'


@app.route(f'/{token}', methods=['POST'])
def telegram():
    # 1. 데이터 구조 print 해보기
    from_telegram = request.get_json()

    if from_telegram.get('message') is not None:
        chat_id = from_telegram.get('message').get('from').get('id')
        text = from_telegram.get('message').get('text')
        
        # 한글키워드 받기

        # '/번역 ' 으로 입력이 시작된다면, 파파고로 번역이 동작한다.
        if text[0:4] == '/번역 ':
            headers = {
                'X-Naver-Client-Id': naver_client_id,
                'X-Naver-Client-Secret': naver_client_secret
            }
            data = {'source': 'ko', 'target': 'en', 'text': text[4:]}
            papago_res = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data)
            text = papago_res.json().get('message').get('result').get('translatedText') # 여기에 한영 번역 text 가 있다.
            
        if text[0:4] == '/로또 ':
            num = text[4:]
            # 동행복권에 요청을 보내 응답을 받는다.
            res = requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}')
            # json 형태로 바꿔준다. (우리가 크롬에서 보고있는 결과와 동일한 모습)
            lotto = res.json()

            # 당첨번호 6개만 가져오기
            winner = []
            for i in range(1, 7):
                winner.append(lotto[f'drwtNo{i}'])
            text = winner
        requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
    return '', 200 