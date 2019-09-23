## 참고 사이트 : https://devdoggo.netlify.com/categories/sql/

```sql
SELECT * FROM CUSTOMERS;
```



마지막에 ;를 붙여준다.



SELECT: 데이터 선택

UPDATE: 데이터를 업데이트

DELETE: 데이터 삭제

INSERT INTO: 새 데이터 삽입

CREATE DATABASE: 새 데디터베이스 생성

ALTER DATABASE: 데이터베이스 업데이트

CREATE TABLE: 테이블 생성

ALTER TABLE: 테이블 업데이트

DROP TABLE: 테이블 삭제

CREATE INDEX: 인덱스 생성

DROP INDEX: 인덱스 삭제



## SELECT

데이터 베이스에서 데이터를 선택할 때 사용

선택된 데이터는 result-set 이라는 result table에 저장된다.



#### 특정 열(Column)을 지정하여 데이터를 선택하고 싶을 때,

```sql
SELECT 열1, 열2,.. FROM 테이블 이름;
```



#### 모든 데이터를 다 갖고오고 싶다면

```sql
SELECT * FROM 테이블이름;
```

별(asterisk) 는 "모든 [데이터, 객체 등]"을 뜻한다.



#### SELECT DISTINCT Statment

일반적으로 테이블의 한 열에는 겹치는 많은 값들이 있을 수 있다. 중복을 제외하여 데이터들의 종류를 확인하고 싶을 때 사용할 수 있다.

```sql
SELECT DISTINCT 열1, 열2,...
FROM 테이블 이름;
```

#### 

#### COUNT 를 추가한다면?

> Customers 라는 테이블 안에 Country 행의 중복되지 않은 데이터를 구함.
>
> Country 안에 U.S. , U.K., Germany, U.S. 데이터들이 담겨있을 때,

```sql
SELECT COUNT(DISTINCT Country) FROM Customers;
>> 3
```

함수처럼 괄호 안에 원하는 행을 넣어 사용한다. 





## WHERE

WHERE 절은 레코드를 필터할 때 사용된다.

프로그래밍 언어의 if 와 같은 기능을 한다고 생각하면 된다. 어떤 특정 조건을 만족시키는 레코드(행)에 대해서만 선택을 하려고 할 때 사용 가능하다.



> 전체 테이블에서 Country 가 'U.S.' 인 레코드만 불러온다.

```sql
SELECT * FROM Customers
WHERE Country='U.S.';
```



```sql
SELECT * FROM Customers
WHERE Customer ID=1;
```



#### WHERE 에 사용될 수 있는 연산자들

| =                  | 같다                                           |
| ------------------ | ---------------------------------------------- |
| <>                 | 같지 않다.                                     |
| >, <               | 보다 큰, 보다 작은                             |
| >=, <=             | 크거나 같은, 작거나 같은                       |
| BETWEEN<br />range | 어떤 range 사이에 있는                         |
| LIKE 어떤 패턴     | 어떤 패턴에 대해 찾기                          |
| IN                 | 열에 대해 다양한 값들의 가능성을 지정하기 위해 |



## AND, OR, NOT

WHERE절은 AND, OR, NOT 연산자와 함께 사용이 가능하다.



#### AND Syntax

```sql
SELECT 열1, 열2, ...
FROM 테이블이름
WHERE 조건1 OR 조건2 OR 조건3 ...;
```



#### OR Syntax

```sql
SELECT 열1, 열2, ...
FROM 테이블이름
WHERE 조건1 OR 조건2 OR 조건3, ...;
```



#### NOT Syntax

```sql
SELECT 열1, 열2, ...
FROM 테이블이름
WHERE NOT 조건;
```



## ORDER BY 'Keyword'

결과 셋(result-set)을 정렬시킬 때 사용한다.

일단 기본적으로 오름차순 정렬을 한다. 내림차순 정렬을 원한다면 DESC 키워드를 사용한다.



#### Syntax

```sql
SELECT 열1, 열2, ...
FROM 테이블이름
ORDER BY 열1, 열2, ... ASC 또는 DESC;
```



ORDER BY Keyword 의 Keyword 에는 하나 이상의 Keyword 가 들어갈 수 있다. 이 경우, 첫 값을 먼저 정렬 후, 그안에서 두번째 값에 대해 정렬을 하고, 그후 세번째 값에 대해 정렬한다.



예를 들어, ORDER BY Number, Company인 경우

Number로 정리 후 같은 Number에서 Company를 알파벳 순으로 정렬한다.



## INSERT INTO

테이블에 새로운 레코드를 추가할 때 사용한다.



#### Syntax

두 가지 방법으로 적을 수 있다. 첫 번째 방법은 열과 값을 명확하게 적는 방법이고,

```sql
INSERT INTO 테이블이름 (열1, 열2, 열3, ...)
VALUES (값1, 값2, 값3, ...);
```



두 번째 방법은 값만 적는 방법이 있다.

```sql
INSERT INTO 테이블이름
VALUES (값1, 값2, 값3, ...);
```



예시,

```sql
INSERT INTO Companies (Number, Company, Figuares)
VALUES (300, 'Snapchat', 'Evan Spiegel');
=> 마지막 행에 추가 된다.
```



#### INSERT INTO 특정한 열에만 데이터 넣기

특정한 열에만 데이터를 넣을 수 있다. 어떤 열에  넣을지를 지정만 해주면 된다. 넣지 않은 열은 null 값이 들어간다.

```sql
INSERT INTO Companies(Company, Figuares)
VALUES ('Uber', 'Travis Kalanick');
```



## SQL NULL 값

NULL 값은 value 가 없는 필드를 뜻한다.

테이블의 필드 값이 필수가 아니면, 앞서 보았듯이 새 레코드를 추가하거나 기존의 레코드를 업데이트 할 때 값을 지정해주지 않으면 NULL 값이 자동으로 들어가게 된다.

※ 주의 : Null 값은 Zero value 나 " "와 같이 띄어쓰기가 있는 값과 다르다. Null value 란, 생성 시 아무것도 들어가지 않았다는 것을 뜻한다. C와 Java와 같은 개념이지만, 파이썬을 사용했던 사람들이라면 각별히 주의해야 한다.



#### Null 값인지 확인하는 방법

NULL 은 일반적인 비교연산자인 =, <, <> 로 비교가 불가능하다. 그 대신, IS NULL 이나 IS NOT NULL 을 사용한다.

```sql
SELECT 열 이름
FROM 테이블 이름
WHERE 열 이름 IS NULL;
```

```sql
SELECT 열 이름
FROM 테이블 이름
WHERE 열 이름 IS NOT NULL;
```















