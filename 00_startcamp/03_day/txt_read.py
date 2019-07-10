# read() : 개행문자를 포함한 하나의 문자열을 만들어냄.
with open('with_ssafy.txt', 'r') as f:
    all_text = f.read()
    print(all_text)

# readlines() : 파일의 모든 라인을 읽어서 각각의 줄을 요소로 갖는 list 로 만들어냄.
with open('with_ssafy.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())
        #'문자열'.strip() : 양쪽의 개행문자를 삭제.
        # print(dir(line)) : 라인에 쓸 수 있는 함수가 뭐있는지 찾아볼때 dir 사용.
        