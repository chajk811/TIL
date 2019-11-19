https://www.npmjs.com/package/vue-session

### this.$session.start()

- session-id 초기화. 만약 세션이 없이 저장하려고 하면 vue-session 플러그인이 자동으로 새로운 세션을 시작



### this.$session.set(key, value)

- session 에 해당 key 에 맞는 값을 저장



### this.$session.has(key)

- key(JWT) 가 존재하는지 여부를 확인



### this.$session.destroy()

- 세션을 삭제



## 흐름

### 0. Django

- 회원가입(JWT 토큰 발급)

### 1. Vue -> Djnago

- 로그인 정보(credentials) 를 Django 서버로 보냄

### 2. Django

- Vue 에서 받은 유저정보에 핻ㅇ하는 고유한 Web Token 발급

### 3. Django -> Vue

- 해당 유저에 대한 token을 Vue로 보냄

### 4. Vue

- Django 에서 받은 토큰을 vue-session 을 통해 저장(이 시점부터  vue 에서는 로그인이 성공 상태)

### 5. Vue -> Django

- vue-session 에 저장된 토큰을 가지고 Django 에 로그인 요청

### 6. Django

- 최초로 보낸 토큰과 일치하는지 여부를 확인(세션에 저장된 토큰 == 요청자의 토큰)

---

`.start()` 를 통해 `session-id` : `sess` + `Data.now()` 가 만들어짐

`.set()` 을 통해 `jwt: jwt 값` 이 만들어짐

----

## Vue 의 라이프 사이크 생성

### 1. Vue instance 생성(create)

### 2. DOM 에 부착(mounted)

### 3. 업데이트 (Update)

### 4. 사라짐(destroy)

----

### FromData

- 기존 키에 새로운  값을 추가하거나 키가 없는 경우 새로운 키를 추가.(`FormData.append()`)
- `FormData.append(name.value)`
- name : value 에 포함되는 데이터 필드 이름
- value : 필드 값















































