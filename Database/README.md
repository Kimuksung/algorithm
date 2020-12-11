
# Database
  

## dbms란?

>DB 관리 시스템으로서, 사용자들이 DB에 접근이 가능하도록 만든 시스템

  

### DDL(data definition Language)
> create , alter , drop , rename = table에 관하여 정의

  

### DML(data manipulation Language)

> select , update , delete , insert

  

### DCL(data control language) = 데이터 보호 관리 목적(무결성, 보안, 권한제어)

  >grant = 사용자에게 권한을 부여
```
GRANT [권한] ON [DB] [TABLE] TO [유저_아이디]@[호스트] IDENTIFIED BY ‘비밀번호’

SHOW GRANTS FOR [유저_아이디]@[호스트]
```
>revoke = 사용자에게 권한 취소
```
REVOKE [권한] ON [DB][TABLE] FROM [유저_아이디]@[호스트]
```
  

참고 = https://m.blog.naver.com/PostView.nhn?blogId=minki0127&logNo=220784504000&proxyReferer=https:%2F%2Fwww.google.com%2F

 ### View
>허용된 데이터를 보여주는 가상 테이블

### 정규화
> 중복을 최대한 줄여 데이터 구조화
> 불필요한 데이터를 논리적으로 저장
> 이상 현상 방지

### 이상현상
>Data Attribute들의 종속성으로 인하여 Data 중복이 발생하는 것을 막는다.  

- Table Column은 Unique 해야함
- Foreign Key는 Null or 참조 Table의 Primary key

### Trigger
> 자동으로 실행 정의된 Procedure
> Event를 관리하기 위해 생성
> Ex) 로그인 , 로그아웃 => 하나의 정보 Table

### Indexing
- B+ TREE

- Hash

- Database를 Indexing을 하여 더 효율적으로 관리하기 위함( 건수가 적으면 Index를 생성X -> Full scan)

- DML이 자주 나온다면 Index에 변경을 가함으로 이와 같은 Table은 indexing 을 하지 않는 것이 좋다.

## rdbms란?
> Relation DB = Table형태  + 개체간의 상관관계
>  Ex) Oracle / Mysql / Sqlite

- DATA  = 2D Table 
- DATA의 독립성 + DML을 이용한 표현 능력
- 상호 관련성을 가진 Table 집합
- 만들거나 이용하기도 쉽고, <span style="color:red">**확장이 용이**</span>
- 확장이 용이 = 자유롭게 구조 변경 가능

### Oracle
> 대규모 Transaction load 처리 가능 + 성능 최적화
> 성능 최적화란? 여러 서버에 DB 분산

-일반적으로 Oracle > Mysql

### Mysql
> 단일 DB + Transaction(Commit + rollback)

### Transaction
> Query를 하나의 묶음 처리해서 실행 여부에 관한 논리적인 단위
>
- Commit = 하나의 Transaction에 대해 작업이 성공적으로 끝나면, 갱신 연산에 대해 완료 처리 후 관리자에게 알려줌
-  Rollback = Transaction 중에 하나라도 처리가 비정상적으로 종료되었다면, DB의 일관성을 해치기 때문에 연산을 취소 시키는 연산

### ACID
-	Atomicity(원자성)
--	All or Nothing으로 일부분만 실행하지 않는다.
-	Consistency(일관성)
--	Data Type이 변경되지 않는다.	
-	Isolation(격리성)
-- Transaction 수행시 다른 Transaction은 끼어들수 없다.
-- 즉, Transaction 끼리는 간섭 불가	
-	Durability(지속성)
-- Transaction이 성공적이라면 영원히 반영

### Transaction이 없다면?
>아래와 같이 Commit을 하지 않은 채로 잠궈버리게 되면 DEADLOCK 발생
![enter image description here](https://github.com/JaeYeopHan/Interview_Question_for_Beginner/blob/master/Database/images/deadlock.png?raw=true)

## RDBMS vs NOSQL
### RDBMS
-	RDBMS = 스키마가 정의
-	Vertical 확장(수직적) 
-	CPU / RAM 부품을 업그레이드하거나 하드웨어 추가하여 서버의 성능 향상
-	Transaction(ACID) 
>데이터 저장을 위해서 스키마 정의가 필수
>
![enter image description here](https://academind.com/static/c6c8b088e9d9dd4722a965cde6b76e0d/d7ad1/sql-schema.jpg)
>Table간의 Join을 통해 데이터 파악 가능

![enter image description here](https://academind.com/static/5df24f0f34a3d98feb531b5fc7776f72/a2510/sql-relations.jpg)
### NOSQL
- MongoDB
- NOSQL = 스키마 X
- 수평적 확장(Horizontal)
-  서버를 추가해서 데이터를 분산하여 저장
-  **샤딩**이라는 기법을 이용하여 분산 저장
-  CAP이론
>Document에 Data 저장
>JSON과 같은 형태로 Key-value

![enter image description here](https://t1.daumcdn.net/cfile/tistory/99FBC9415C937F2A20)
> Collection 별로 중복데이터가 발생
> 
![enter image description here](https://academind.com/static/bbea2ff32393dedce24d2114b26254fb/d7ad1/nosql-no-relations.jpg)

### CAP이론
> 모든 것을 만족 X -> 2가지만 만족
- Consistency(일관성)
-- 모든 요청은 최신 데이터 또는 에러를 응답 
-- 3개의 DB로 분산되어 있을 때, 하나의 DB가 수정되면 나머지 2개의 DB에서도 수정된 데이터 응답을 받아야 한다.

- Availability(가용성)
-- 모든 request 는 정상 response을 받는다.
-- 특정 DB가 장애가 발생해도 서비스 가능

- Partitions Tolerance(분리 내구성)
-- DB간 통신이 실패하는 경우라도 시스템은 정상 동작

## mysql 사용 여부 / 쿼리 얼마나 아는가?

  

## mysql server 란?

  ## mssql이란?

## data modeling 지식 말해보라

  
## 통계 관련 지식 말해보라

  
## FDS란?

  

## API 개발 경험