# DB

## DataBase

- 체계화된 데이터의 모임
- 여러사람이 공유하고 사용할 목적으로 통합 관리되는 정보의 집합
- 논리적으로 연관된 자료의 모음
  - 구조화 효율화
- 자료 파일을 조직적으로 통합
  - 중복을 없애고 구조화하여 기억

---

### 데이터베이스 장점

- 중복 최소화
- 무결성(정확한 정보 보장)
- 데이터 일관성
- 데이터 독립성(물리적 / 논리적)
- 데이터 표준화
- 데이터 보안 유지

---

### RDB 관계형 데이터베이스

- Relational DataBase
- 키(Key)와 값(Value)들의 간단한 관계(Relation)를 표(Table) 형태로 정리한 데이터베이스
- 관계형 모델에 기반

---

### 스키마

- Schema

- 데이터베이스에서 자료의 구조, 표현방법, 관계등 전반적인 명세를 기술한 것

- | column  | datatype |
  | :-----: | :------: |
  |   id    |   INT    |
  |  name   |   TEXT   |
  | address |   TEXT   |
  |   age   |   INT    |

---

### 테이블(Table)

- 열(컬럼/필드)과 행(레코드/값)의 모델을 사용해 조직된 데이터 요소들의 집합
- 열(column) : 각 열에는 고유한 데이터 형식이 지정됨 ex) name  텍스트 필드
- 행(row) : 실제 데이터가 저장되는 형태 / 레코드
- 기본키(primary Key) : 강 행(레코드)의 고유 값
  - 반드시 설정해야함
  - 데이터베이스 관리 및 관계 설정 시 주요하게 활용 됨
  - id



---

### RDBMS

- Relational Database Management System
- 관계형 모델을 기반으로 하는 데이터베이스 관리 시스템을 의미
- MySQL, SQLite, PostgreSQL, ORACLE, MS SQL



---

### SQLite

- 파일 형식으로 응용 프로그램에 넣어서 사용
- 비교적 가벼운 데이터베이스
- 임베디드 소프트웨어에도 많이 활용됨
- Sqlite Data Type
  - NULL
  - INTEGER
    - 0, 1, 2, 3, 4, 6, 8바이트에 저장된 부호 있는 정수
  - REAL
  - TEXT
  - BLOB
    - 입력된 그대로 정확히 저장된 데이터
    - 별다른 타입 없이 그대로 저장
  - NUMERIC

- Sqlite Type Affinity
  - 특정 컬럼에 저장하도록 권장하는 데이터 타입

---

### SQL (Structured Query Language)

- 관계형 데이터베이스 관리시스템(RDBMS)의 데이터 관리를 위해 설계된 특수 목적으로 프로그래밍 언어

- 데이터베이스 스키마 생성 및 수정

- 자료의 검색 및 관리

- 데이터베이스 객체 접근 조정 관리

- 주석

  - ```sqlite
    -- SQLite
    ```

- 대소문자 구별안함/ 단, 문자 값 데이터에 대해서는 구별함

---

### SQL 분류

- DDL Data Definition Language 데이터 정의 언어
  - 관계형 데이터베이스 구조(테이블, 스키마)를 정의하기 위한 명령어
  - CREATE DROP ALTER
- DML Data Manipulation Language 데이터 조작 언어
  - 데이터를 저장, 조회, 수정, 삭제 등을 하기 위한 명령어
  - INSERT
    - 새로운 데이터 삽입(추가)
  - SELECT
    - 저장되어있는 데이터 조회
  - UPDATE
    - 저장되어있는 데이터 갱신
  - DELETE
    - 저장되어있는 데이터 삭제
- DCL Data Control Language 데이터 제어 언어
  - 데이터베이스 사용자의 권한 제어를 위해 사용하는 명령어
  - GRANT
  - REVOKE
  - COMMIT
  - ROLLBACK

---

### 테이블 생성 및 삭제

- ```bash
  $ sqlite3 tutorial.sqlite3
  sqlite> .database
  sqlite> .mode csv
  sqlite> .import hellodb.csv examples
  sqlite> .tables
  examples
  sqlite> SELECT * FROM examples;
  
  sqlite> .headers on
  sqlite> SELECT * FROM examples;
  
  sqlite> .mode column
  sqlite> SELECT * FROM examples;
  ```

- sqlite 파일 우클릭 > Open Database > New Query

- ```sqlite
  CREATE TABLE classmates (
    id INTEGER PRIMARY KEY,
    name TEXT
  );
  INSERT INTO classmates (id, name) VALUES (1, 'JYP');
  ```

- 코드 우클릭 >  Run Query or Run Selected Query

- CREATE TABLE

  - 데이터베이스 테이블 생성

- DROP TABLE

  - 데이터베이스 테이블 제거

- ```bash
  $ sqlite3 tutorial.sqlite3
  sqlite> .database
  sqlite> .mode csv
  sqlite> .import hellodb.csv examples
  sqlite> .tables
  examples
  sqlite> CREATE TABLE classmates (
     ...> id INTEGER PRIMARY KEY,
     ...> name TEXT
     ...> );
  sqlite> .tables
  classmates examples
  sqlite> .schema classmates
  CREATE TABLE classmates (
  id INTEGER PRIMARY KEY,
  name TEXT
  );
  sqlite> DROP TABLE classmates;
  sqlite> .tables
  examples
  ```

- ```sqlite
  CREATE TABLE classmates (
  name TEXT,
  age INT
  address TEXT
  );
  ```

- ```bash
  $ sqlite3 tutorial.sqlite3
  sqlite> .schema classmates
  CREATE TABLE classmates (
  name TEXT,
  age INT,
  address TEXT
  );
  ```



---

### CRUD

- CREATE

  - INSERT

    - 테이블에 단일 행 삽입

    - ```sqlite
      INSERT INTO classmates (name, age) VALUES ('JYP', 28);
      ```

    - ```bash
      $ sqlite3 tutorial.sqlite3
      sqlite> SELECT * FROM classmates;
      name	age		address
      ------	------	--------
      JYP		28		
      ```

    - ```sqlite
      INSERT INTO classmates VALUES ('JYP', 28, '부울경');
      ```

    - ```bash
      $ sqlite3 tutorial.sqlite3
      sqlite> SELECT * FROM classmates;
      name	age		address
      ------	------	--------
      JYP		28
      JYP		28		부울경
      sqlite> SELECT rowid, * FROM classmates;
      rowid	name	age		address
      ------	-----	------	---------
      1		JYP		28
      2		JYP		28		부울경
      ```

    - PRIMARY KEY 속성의 컬럼을 작성하지 않으면

    - 값이 자동으로 증가하는 PK 옵션을 가진 rowid 컬럼을 정의

    - ```bash
      sqlite> DROP TABLE classmates;
      sqlite> CREATE TABLE classmates (
         ...> id INTEGER PIRMARY KEY,
         ...> name TEXT NOT NULL,
         ...> age INT NOT NULL,
         ...> address TEXT NOT NULL
         ...> );
      sqlite> INSERT INTO classmates VALUES ('JYP', 28, '부울경');
      Error: table classmates has 4 columns but 3 values were supplied
      sqlite> INSERT INTO classmates VALUES (1, 'JYP', 28, '부울경');
      sqlite> INSERT INTO classmates (name, age, address) VALUES ('JYP', 28, '부울경');
      sqlite> DROP TABLE classmates;
      sqlite> CREATE TABLE classmates (
         ...> name TEXT NOT NULL,
         ...> age INT NOT NULL,
         ...> address TEXT NOT NULL
         ...> );
      ```

    - ```sqlite
      INSERT INTO claamates VALUES
      ('JYP', 28, '부울경'),
      ('MJ', 29, '부울경');
      ```

- READ

  - SELECT

  - 테이블에서 데이터를 조회

  - 다양한 절(clause)와 함께 사용

  - ORDER BY, DISTINCT, WHERE, LIMIT, GROUP BY 등

  - LIMIT

    - 쿼리에서 반환되는 행 수를 제한

    - 특정 행부터 시작해서 조회하기 위해 OFFSET 키워드와 함께 사용하기도 함

    - ```bash
      sqlite> SELECT * FROM classmates LIMIT 1;
      sqlite> SELECT * FROM classmates LIMIT 1 OFFSET 2;
      세번째 하나만 조회
      sqlite> SELECT * FROM classmates LIMIT 10 OFFSET 5;
      6 ~ 10 조회
      ```

    - OFFSET 0부터 시작함????

  - WHERE

    - 쿼리에서 반환된 행에 대한 특정 검색 조건을 지정

    - ```bash
      sqlite> SELECT rowid, name FROM classmates WHERE address='부울경';
      sqlite> SELECT rowid, name FROM classmates WHERE address='부울경' AND name='JYP';
      ```

  - DISTINCT

    - 조회 결과에서 중복 행을 제거

    - SELECT DISTINCT  / SELECT 키워드 바로 뒤에 작성

    - ```bash
      sqlite> SELECT DISTINCT age FROM classmates;
      ```

  - SELECT 컬럼1, 컬럼2 FROM 테이블이름;

    - 특정 컬럼만 조회

    - ```bash
      sqlite> SELECT rowid, name FROM classmates;
      ```

- DELETE

  - 테이블에서 행을 제거

  - ```bash
    sqlite> DELETE FROM classmates WHERE rowid=5;
    sqlite> INSERT INTO classmates VALUES ('MJ', 29, '부울경');
    SQLite는 기본적으로 id를 재사용
    재사용 방지하려면
    sqlite> CREATE TABLE classmates (
       ...> id INTEGER PRIMARY KEY AUTOINCREMENT,
       ...> ...
       ...> );
    AUTOINCREMENT를 통해 재사용 방지 설정 가능
    ```

- UPDATE

  - 기존 행의 데이터를 수정

  - SET clause에서 테이블의 각 열에 대해 새로운 값을 설정

  - ```bash
    sqlite> UPDATE classmates SET name='JYP2', address='양산' WHERE rowid=1;
    ```

- 정리

  - C, INSERT
    - INSERT INTO 테이블이름 (컬럼1, 컬럼2, ...) VALUES (값1, 값2);
  - R, SELECT
    - SELECT * FROM 테이블이름 WHERE 조건;
  - U, UPDATE
    - UPDATE 테이블이름 SET 컬럼1=값1, 컬럼2=값2 WHERE 조건;
  - D, DELETE
    - DELETE FROM 테이블이름 WHERE 조건;

---

### 집계함수

- Aggregate function

- 값 집합에 대한 계산을 수행하고 단일 값을 반환

- COUNT, AVG, MAX, MIN, SUM

- COUNT

  - ```sqlite
    SELECT COUNT(*) FROM users;
    ```

- AVG, MAX, MIN, SUM

  - 컬럼이 INTEGER 일 때만 가능

  - ```sqlite
    SELECT AVG(age) FROM users WHERE age >= 30;
    SELECT first_name, Max(balance) FROM users;
    SELECT AVG(balance) FROM users WHERE age >= 30;
    ```

---

### LIKE

- 패턴 일치를 기반으로 데이터를 조회하는 방법
- % (percent sign)
  - 0개 이상의 문자
- _ (underscore)
  - 임의의 단일 문자

- wildcard character

  - 구체적인 이름 대신 여러 파일을 동시에 지정할 목적으로 사용하는 특수 기호
  - '*', '?' 등
  - 문자열, 파일을 찾거나, 긴 이름을 생량할 때 쓰임

- ```sqlite
  SELECT * FROM 테이블 WHERE 컬럼 LIKE '와일드카드패턴';
  ```

- ```
  2%
  2로 시작하는 값
  %2
  2로 끝나는 값
  %2%
  2가 들어가는 값
  _2%
  아무 값이 하나 있고 두 번째가 2로 시작하는 값
  1___
  1로 시작하고 4자리인 값
  2_%_% / 2__%
  2로 시작하고 적어도 3자리인 값
  ```

- ```sqlite
  SELECT * FROM users WHERE age LIKE '2_';
  SELECT * FROM users WHERE phone LIKE '02-%';
  SELECT * FROM users WHERE first_name LIKE '%준';
  SELECT * FROM users WHERE phone LIKE '%-5114-%';
  ```

---

### ORDER BY clause

