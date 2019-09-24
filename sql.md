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



## UPDATE

기존에 테이블에 있는 레코드를 변형할 때 쓴다.



#### Syntax

```sql
UPDATE 테이블이름
SET 열1 = 값1, 열2 = 값2, ...
WHERE 조건;
```

'변경하고 싶은 테이블에서 조건에 해당하는 레코드에 대해 원래 있던 값을 SET 에 나오는 값들로 변경시켜라' 라고 풀어서 말할 수 있다.

지금까지 본 SQL 과 다르게 살짝 직관적이지 않은 부분은 조건이 변경 사항 뒤에 온다는 점이다.

조건에 해당하는 레코드에 대해 변경한다는 것은, 조건이 없을 경우 테이블의 모든 값들에 대해 변경을 하게 된다는 뜻이지 때문에, UPDATE 를 사용할 경우 WHERE 을 까먹지 말도록 하자.



#### 예시

```sql
UPDATE Companies
SET Company = 'Solarcity', Figures = 'Elon Musk'
WHERE Number = 105;
```



#### 다양한 레코드에 대해 Update

조건에 해당하는 레코드가 변경된다고 앞서 말했다. 그렇다면 조건에 해당하는 레코드가 하나가 아니라 여러가지라면 전부 다 변경이 가능하지 않을까?

```sql
UPDATE Companies
SET Company='Fell off the Loop'
WHERE Number=400;
```

만약 Number=400 인 레코드가 여러개면 다 바뀌게 된다.



##   DELETE

테이블에 이미 있는 레코드를 삭제할때 사용한다.



#### Syntax

```sql
DELETE FROM 테이블이름
WHERE 조건
```

'테이블에 조건에 해당한ㄴ 것을 삭제한다'라고 할 수 있다.



#### 모든 레코드 삭제

테이블을 지우지 않은 상태에서 모든 레코드만 다 비우고 싶다면 다음과 같이 하면 된다.

```sql
DELETE FROM 테이블이름;
```

```sql
DELETE * FROM 테이블이름;
```



## SELECT TOP

많은 데이터가 있을 떄 특정 개수의 레코드만 뽑고 싶다면 사용!

정한 양의 레코드만을 추출하고 싶을 때 사용한다. 큰 테이블에 몇천개의 레코드가 있을 때 아주 유용하다.

※ 주의 : 모든 데이터베이스 시스템이 SELECT TOP 절을 사용하지 않느다. MYSQL 은 LIMIT 이라는 절을 사용하고, Oracle 은 ROWNUM 을 사용한다.



#### SQL Server / MS Access Syntax

```sql
SELECT TOP 숫자 열 이름
FROM 테이블 이름
WHERE 조건;
```

```sql
SELECT TOP 숫자 PRECENT 열 이름
FROM 테이블 이름
WHERE 조건;
```



#### MYSQL Syntax

```sql
SELECT 열 이름
FROM 테이블 이름
WHERE 조건;
LIMIT 숫자;
```



#### Oracle Syntax

```sql
SELECT 열 이름
FROM 테이블 이름
WHERE ROWNUM <= 숫자;
```



## MIN() & MAX() 함수

최대, 최소값을 반환하는 함수이다.



#### Syntax

MIN()

```sql
SELECT MIN(열 이름)
FROM 테이블 이름
WHERE 조건;
```

MAX()

```sql
SELECT MAX(열 이름)
FROM 테이블 이름
WHERE 조건;
```



result-set 에 이름이 MAX(Price) 혹은 MIN(Price)로 나타난다. AS 를 이용해서 필드 이름을 바꿀 수 있다.

```sql
SELECT MIN(Price) AS SmallestPrice
FROM Product;
```



## COUNT(), AVG() 그리고 SUM() 함수

COUNT(): 특정 조건을 만족하는 열의 숫자를 반환한다.

AVG(): 열의 평균 값을 반환한다.

SUM(): 열의 합을 반환한다.



#### Syntax

COUNT()

```sql
SELECT COUNT(열 이름)
FROM 테이블 이름
WHERE 조건;
```



AVG()

```sql
SELECT AVG(열 이름)
FROM 테이블 이름
WHERE 조건;
```



SUM()

```sql
SELECT SUM(열 이름)
FROM 테이블 이름
WHERE 조건;
```





## SQL Group By

aggerate 함수(COUNT, MAX, MIN, SUM, AVG) 와 주로 함께 쓰이며, 결과 셋을 하나 이상의 열로 그룹지을 때 사용된다.



#### GROUP BY Syntax

```sql
SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s)
ORDER BY column_name(s);
```



#### 예시

```sql
SELECT COUNT(Customer ID), Country
FROM Customers
GROUP BY Country;
```



#### GROUP BY 와 JOIN 을 함께 쓰는 예시 (JOIN 공부하고 다시 보기)

```sql
SELECT Shippers.ShipperName, COUNT(Orders.OrderID) AS NumberOfOrder FROM Orders
LEFT JOIN Shippers ON Orders.ShipperID = Shippers.ShipperID
GROUP BY ShipperName;
```



#### GROUP BY 에 조건을 넣고 싶을 때, HAVING

```sql
SELECT NAME, COUNT(NAME) AS 'COUNT'
FROM ANIMAl_INS
GROUP BY NAME HAVING COUNT>1
ORDER BY NAME;
```



## LIKE

WHERE 절 안에서 쓰이는데, 열에서 어떤 특정한 패턴에 부합하는 부분을 찾으려 할 때 쓴다.

LIKE 연산자는 두가지의 와일드카드 문자를 쓴다.

- % : 0, 1 혹은 하나 이상의 char

- _ : 한개의 char

  ※ 주의 : MS Access는 _ 대신 ? 을 사용한다.



#### Syntax

```sql
SELECT 열1, 열2, ...
FROM 테이블이름
WHERE 열 LIKE 패턴;
```

팁: AND 와 OR 조합하여 조건을 표현할 수 있다.

LIKE 와 %, _ 와일드 카드를 이용한 예시들이다.

NOT LIKE 로 부정할 수도 있다.



| LIKE                           | 설명                                      |
| ------------------------------ | ----------------------------------------- |
| WHERE CustomerName LIKE ‘a%’   | “a”로 시작하는 모든 값                    |
| WHERE CustomerName LIKE ‘%a’   | “a”로 끝나는 모든 값                      |
| WHERE CustomerName LIKE ‘%or%’ | “or”이 있는 모든 값                       |
| WHERE CustomerName LIKE “_r%”  | 두 번째 인덱스에 “r” 이 있는 모든 값      |
| WHERE CustomerName LKE ‘a*%*%’ | “a” 로 시작하며 최소 3글자 이상인 모든 값 |
| WHERE contactName LIKE ‘a%o’   | “a” 로 시작하여 “o” 로 끝나는 모든 값     |



#### [Charlist] 와일드 카드

위 %와 _과는 별개로, [charlist] 와일드카드라는 것이 존재한다. 정규표현식 문자열을 생각하면 된다.

[bsp]% 는 'b' or 's' or 'p' 로 시작하는 모든 데이터를 뜻하며,

[a-e]% 는 'a'부터 'e' 사이에 있는 알파벳 중 하나로 시작하는 모든 데이터를 뜻한다.



예

```sql
SELECT * FROM Customers
WHERE ProductName LIKE '[dc]%';
```



#### [!Charlist]

! 를 붙여 NOT의 역할을 하는 와일드카드 또한 만들 수 있다.



예

```sql
SELECT * FROM Customers
WHERE ProductName LIKE '[!dc]%';
```



## IN 연산자

WHERE절 에서 다양한 값들을 선택할 수 있게 해준다.

다시 말해, IN은 여러 개의 OR 조건은 연속으로 사용하는 것과 같은 효과를 낸다.

NOT IN 도 사용가능



#### Syntax

```sql
SELECT 열 이름
FROM 테이블 이름
WHERE 열 이름 IN (값1, 값2, ...);
```

```sql
SELECT 열 이름
FROM 테이블 이름
WHERE 열 이름 IN (SELECT 문)
```



#### IN (SELECT 문)

```sql
SELECT * FROM Product
WHERE Company IN(SELECT CompanyName FROM Stockprice)
```



## BETWEEN 연산자

주어진 range 에 대해서 값들을 선택할 수 있도록 해준다. 여기서 값은 숫자(number), 텍스트(text), 혹은 날짜(date) 일 수 있다.

중요한 점은 inclusive 하다는 것이다. 양쪽 끝이 포함된다. 1과 10을 넣으면 1에 해당하는 값과 10에 해당하는 값이 포함되어 온다는 것이다.



#### Syntax

```sql
SELECT 열 이름
FROM 테이블 이름
WHERE 열 이름 BETWEEN 값1 혹은 AND 값2
```





### 예시

Table : Products

| ProductID | ProductName | Price | Company |
| --------- | ----------- | ----- | ------- |
| 1         | Doritos     | 750   | Pepsi   |
| 2         | Cheetos     | 1200  | Pepsi   |
| 3         | Sun Chip    | 1500  | Pepsi   |
| 4         | GkokalCone  | 500   | Lotte   |
| 5         | Goraebap    | 850   | Orion   |
| 6         | Corncho     | 1000  | Crown   |

``` sql
SELCT * FROM Products
WHERE Price BETWEEN 500 AND 1000
```

=> 결과

| ProductID | ProductName | Price | Company |
| --------- | ----------- | ----- | ------- |
| 1         | Doritos     | 750   | Pepsi   |
| 4         | GkokalCone  | 500   | Lotte   |
| 5         | Goraebap    | 850   | Orion   |
| 6         | Corncho     | 1000  | Crown   |



#### NOT BETWEEN

```sql
SELECT * FROM Products
WHERE Price NOT BETWEEN 500 AND 1000
```

=> 결과

| ProductID | ProductName | Price | Company |
| --------- | ----------- | ----- | ------- |
| 2         | Cheetos     | 1200  | Pepsi   |
| 3         | Sun Chip    | 1500  | Pepsi   |



#### 텍스트 값

숫자와 마찬가지로 텍스트 값을 넣게 되면 알파벳 수서상의 range 에 들어가는 부분이 나오게 된다. BETWEEN 'C' AND 'E' 를 하면 c, d, e 에 해당하는 부분이 될 것이다.

```sql
SELECT * FROM Products
WHERE ProductName BETWEEN 'G' and 'S'
```

=> 결과

| ProductID | ProductName | Price | Company |
| --------- | ----------- | ----- | ------- |
| 4         | GkokalCone  | 500   | Lotte   |
| 5         | Goraebap    | 850   | Orion   |



알파벳이 아니라 아예 해당 상품명을 입력할 수도 있다.

```sql
SELECT * FROM Products
WHERE ProductName BETWEEN 'GkokalCone' AND 'Sun Chip'
```











