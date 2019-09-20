## either project 

> [either.io](http://either.io/)
>
> [Filtering on annotations](https://docs.djangoproject.com/ko/2.0/topics/db/aggregation/#filtering-on-annotations)
>
> [order_by randomly use](https://docs.djangoproject.com/ko/2.1/ref/models/querysets/#order-by)

### **프로젝트 이름**

- crud

### **앱 이름** 

- eithers

### **모델 구조**

1. Question model

| 필드명  | 자료형 |     용도     |
| :-----: | :----: | :----------: |
|  title  | String |  주제 제목   |
| issue_a | String |   선택지 1   |
| issue_b | String |   선택지 2   |
| image_a | Image  | 선택1 이미지 |
| image_b | Image  | 선택2 이미지 |

2. Answer model

|  필드명  | 자료형  |      용도      |
| :------: | :-----: | :------------: |
| question | Integer | 모델 관계 설정 |
|   pick   | Integer |  선택지 선택   |
| comment  | String  |      의견      |

---

### **구현 기능**

1. Bootstrap (input / form / form radio / jumbotron / card / progress 등) 사용
2. Question - C / R
3. Answer - C / R / D
4. [선택] Random 으로 detail 페이지 보여주기

### **사용 뷰 함수**

- index / new / detail / answers_create / answers_delete / random

### **최종 파일 구조 예시**

```
.
├── crud
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── eithers
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   ├── models.py
│   ├── templates
│   │   └── eithers
│   │       ├── base.html
│   │       ├── detail.html
│   │       ├── index.html
│   │       └── new.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
└── media
    └── eithers
        └── images
```

> **위 조건은 외에 추가 함수 및 기능 구현은 자유롭게 작성 가능합니다.**