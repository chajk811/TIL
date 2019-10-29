## let

- 값을 대할당 할 수 있는 변수를 선언
- 단. 각 변수느 한번만 선언 할 수 있다.(할당은 여러번 가능)
- 블록 유효 범위(block scope)



## const

- 값이 변하지 않는 상수를 선언하는 키워드
- 담긴 값이 불변임을 뜻하는게 아니다.
- 단지 상수의 값은 재할당 할 수 없고 재선언도 안된다.

- 블록 유효 범위(block scope)



## var(변수)

- ES6 이전의 feature로 예기치 않은 문제를 많이 발생시키는 키워드로 절대 사용하지 않는다.
- 함수 유효 범위(function scope)
- var 로 선언된 변수의 범위는 현재 실행 문맥인데, 그 문맥이 함수 혹은 함수 외부의 전역으로도 갈 수 있다.

---

- 어디에 쓸지 결정하는건 프로그래머의 몫
- `PT`, `DAYS_IN_JUNE` 과 같은 경우는 상수가 적절
- `WEATHER_TEMP` 처럼 모호한 경우(각자가 생각하는 좋아하는 기온이 다를 수 있으니까) 이런 경우는 변수가 적절

----

일단 모든 선언에서 가능한한 상수(const)를 사용해야 한다.

먼저 상수를 생각하고 값이 바뀌는 것이 더 자연스러운 상황이라면, 그때 변수로 바꿔서 사용하는 것을 권장.

----

var : 할당 및 선언 자유 / 함수 스코프

let : 할당 자유 / 선언은 한번만 / 블록 스코프

const : 할당 및 선언 모두 한번만 / 블록 스코프



## 식별자(identifier)

- 번수명은 식별자라고 불리면 특정 규칙을 따른다.

1. 반드시 문자, 달러($), 또는 밑줄로 시작해야 한다. 이후는 숫자도 가능.
2. 대소문자를 구분하며 클래스명을 제외하고는 대문자로 시작하지 않는 것이 좋다.
3. 예악어는 사용 불가능(class, super, const, case, function ...)



## 호이스팅

- 이 개념은 JS 변수, 함수나 표현이 최상단으로 올려지는 것을 말한다.
- 끌어 올려진 변수는 `undefined` 값을 반환한다.
- 변수와 함수를 위한 메모리 공간을 확보하는 과정.

----

### var 할당 과정

1. 선언 + 초기화
2. 할당

### let 할당 과정

1. 선언
2. TDZ (Temporal Dead Zone,임시적 사각지대)
3. 초기화
4. 할당

---

let, const 의 정의가 평가되기까지 초기화가 되지 않는다는 의미이지, 호이스팅이 되지 않아 정의가 되지 않는 다는 의미와는 다르다.

---------



## 타입과 연산자

타입

1. Primitive
2. Reference



### Primitive

- 불변하다는 특징을 띄고 있다.

1. Numbers
   - `infinity` : 양의 무한대와 음의 무한대로 나뉨
   - `NaN` : Not a Number, 표현할 수 없는 값, 자기 자신과 일치하지 않는 유일한 값을 표현
     - 0/0, "문자"  * 10, Math.sqrt(-9)
2. Strings
3. Boolean
4. Empty Value

----

### Literak

- 값ㅇ르 프로그램 안에서 직접 저장한드는 의미
- 값을 만드는 방법
- JS 는 우리가 제공한 리터럴 값을 받아 데이터를 만듦

```javascript
// room 변수를 가리키는 식별자 / 'conference'(따옴표 안)은 리터럴
let room = 'conference_room'

let hotelRoom = room

// 에러, conference_room 식별자는 존재하지 않는다.
hotelRoom = conference_room
```

- JS 는 따옴표를 통해 리터럴과 식별자를 구분한다.
- 식별자는 숫자로 시작할 수 없으므로 숫자에는 따옴표가 필요없다.(숫자형 리터럴)

----

`null` // `undefined`

- 동일한 역할으 하는 이 2개의 키워드가 존재하는 이유는 단순한 JS의 설계 실수.
- 큰 차이를 두지 말고 interchangeable 하게 사용할 수 있도록 권장

----

`undefined`

- 값이 없을 경우 JS가 자동으로 할당 해주는 값

```javascript
let first_name // 선언만 하고 할당하지 않음.
console.log(first_name) // undefined
```

`null`

- 값이 없음을 우리가 표현하기 위해서 인위적으로 사용하는 값

```javascript
let last_name = null
console.log(last_name) // null-의도적으로 값이 없음을 표현
```