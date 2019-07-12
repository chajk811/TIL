from flask import Flask, render_template, request
from datetime import datetime
import random

app = Flask(__name__)

@app.route('/')
def hello():
    #return 'Hello World!'
    # render template
    return render_template('index.html')

@app.route('/ssafy')
def ssafy():
    return 'This is SSAFFY!'


@app.route('/d_day')
def dday():
    # 오늘 날짜
    today_time = datetime.now()
    # 수료 날짜
    endgame = datetime(2019, 11, 29)
    # 수료 날짜 - 오늘 날짜
    dday = endgame - today_time
    return f'{dday.days}일 남았습니다.'


@app.route('/html')
def html():
    return '<h1>This is HTML TAG</h1>'


@app.route('/html_line')
def html_line():
    return """
    <h1>여러 줄을 보내 봅시다</h1>
    <ul>
    <li>1번</li>
    <li>2번</li>
    </ul>    
    """


@app.route('/greeting/<name>')
def greeting(name):
     return render_template('greeting.html', html_name=name)
     #return f'반갑습니다! {name}'



@app.route('/cube/<int:number>')
def cube(number):
     # 연산을 모두 끝내고 변수만 cube.html 로 넘긴다.
     #return f'{number}의 세제곱은 {number**3}입니다.'
     result = number**3  
     return render_template('cube.html', number=number, result=result)

@app.route('/lunch/<int:number>')
# 플라스크는 여러 메뉴 중에서 인원 수만큼의 메뉴를 응답합니다.
def lunch(number):
    menu = ['한식', '일식', '양식', '중식']
    lunch_menu = []
    for i in range(number):
         lunch_menu.append(random.choice(menu))
    #lunch_menu = random.choices(menu, [1, 1, 1, 1], k=number)
    return str(lunch_menu)

@app.route('/movie')
def movie():
     movies = ['토이스토리4', '스파이더맨', '알라딘', '기생충', '앤드게임']
     return render_template('movie.html', movies=movies)


@app.route('/ping')
def ping():
     return render_template('ping.html')

@app.route('/pong')
def pong():
     name = request.args.get('data')
     return render_template('pong.html', name=name)


# fake naver, fake google 만들기
#url = 'https://search.naver.com/search.naver?query='
@app.route('/naver')
def naver():
     return render_template('naver.html')


@app.route('/google')
def google():
     return render_template('google.html')


# vonvon 봇 만들기
@app.route('/name')
def name():
     return render_template('name.html')


@app.route('/result')
def result():
     name = request.args.get('data')
     characters = ['순수함', '활발함', '똘기', '꼼꼼함']
     character = []
     for i in range(3):
          character.append(random.choice(characters)+ '' + str(random.randrange(1,11)) + '스푼')
     return render_template('result.html', name=name, character=character)


#로또 회차/내병호 입력 페이지
#결과 페이지
import requests

@app.route('/lotto_check')
def lotto_check():
    return render_template('lotto_check.html')


@app.route('/lotto_result')
def lotto_result():
    # 회차 번호를 받아온다.
    num = request.args.get('num')
    # 동행복권에 요청을 보내 응답을 받는다.
    res = requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}')
    # json 형태로 바꿔준다. (우리가 크롬에서 보고있는 결과와 동일한 모습)
    lotto = res.json()

    # 당첨번호 6개만 가져오기
    winner = []
    for i in range(1, 7):
        winner.append(lotto[f'drwtNo{i}'])

    # 내 번호 리스트 만들기
    numbers = []
    for num in request.args.get('numbers').split():
        numbers.append(int(num))
    
    # 등수 가리기(몇개 맞았는지 교집합이 필요)
    # 내 번호 요소를 뽑아서 당첨번호 리스트에 있는지 확인.
    matched = 0
    for num in numbers:
        if num in winner:
            matched += 1

    if matched == 6:
        result = '1등입니다!'
    elif matched == 5:
        if lotto['bnusNo'] in numbers:
            result = '2등입니다!'
        else:
            result = '3등입니다!'
    elif matched == 4:
        result = '4등입니다!'
    elif matched == 3:
        result = '5등입니다!'
    else:
        result = '꽝입니다!'
    
    return render_template('lotto_result.html', winner=winner, numbers=numbers, result=result)
    