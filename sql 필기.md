`.` splite3 프로그램의 기능을 실행하는 것

`;` 세미콜론 까지가 하나의 멸령(Query)으로 간주

- sql 문법은 소문자로 작성해도 된다.(단, 대문자를 권장)
- 하나의 DB 에는 여러 개의 table 이 존재한다.



id `INTEGER PRIMART KEY `: rowid 를 대체





ALTER

테이블 이름을 변경 혹은 column 추가

ALTER TABLE 현재 이름 RENAME TO 새로운 이름

ALTER TABLE table ADD COLUMN column DATATYPE;

기존의 데이터가 저장되어 있는 상태에서 새로운 컬럼을 추가하려면

기존의 컬럼의 데이터 타입에 NOT NULL 조건때문에 추가가 불가능하다.

NOT NULL 조건을 없애던가

`DEFAULT value;` 디폴트 값으로 주거나 

