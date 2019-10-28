API 

정해진 형식으로 요청을 보내면 요청한 정보를 받을 수 있는 소통방법

어플리케이션간의 소통 



인터페이스 (접점)

사람 - 기계  UI(user interface)

기계 - 기계  API(어플리케이션 프로그래밍 인터페이스)

REST 라는 형식의 API 



POST 요청만으로도 가능하다. 근데 왜?

각 요청이 어떠한 동작&정보를 위한 것인지 요청형식자체 주소로 파악이 가능한 것



fixture

- 데이터베이스의 직렬화(serialized) 된 내용을 포함하는 파일 모음이다.
- 각 fixture 는 고유한 이름을 가지며, 이를 구성하는 파일은 여러 응용 프로그램에서 여러 디렉토리에 배포될 수 있다.
- django 는 loaddata 시  설치된 모든 app 에서 fixture 라고 이름의 폴더를 찾는다.
- static, templates 와 같이 지정된 이름의 파일을 찾는다.

```
musics/
	fixtures/
    	musics/
        	dummy.json
```

python manage.py dumpdata --indent 2 musics > dummy.json

python manage.py loaddata musics/dummy.json



참고)

Django REST framework



django drf-yasg

api doc 라이브러리 중 하나



POSTMAN

서버에 요청을 보낼때 사용하는 프로그램