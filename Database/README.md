
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
> Client 접속 및 쿼리 요청에 대해 처리하는 Connection Handler와 Optimizer로 이루어진다.

- mysql은 Data Table에 대해 각각의 성격에 따라 성능 향상을 이룬다.
-	mysql 엔진 = Query 분석 및 최적화
- 스토리지 엔진 = Data를 읽는 역할

-Thread 구조 = 포그라운드 + 백그라운드

-포그라운드 = 클라이언트 쓰레드
>**최소한 MySQL 서버에 접속된 클라이언트의 수만큼 존재하며, 주로 각 클라이언트 사용자가 요청하는 쿼리 문장을 처리하는 것이 임무**입니다.  

-백그라운드
>**1. 인서트 버퍼(Insert Buffer)를 병합하는 스레드**
>**2. 로그를 디스크로 기록하는 스레드**
> **3. InnoDB 버퍼 풀의 데이터를 디스크에 기록하는 스레드**
>  **4. 데이터를 버퍼로 읽어들이는 스레드** 
> **5. 모니터링하는 스레드**  (잠금이나 데드락)

## data modeling 지식 말해보라
### 삼성 취식량
- 판매 날짜 / 브랜드 / 소비자 아이디 / 갯수
- 소비자 아이디 / 생년월일 / 성별
- 날짜 / 온도 / 기온 / 습도 / 휴일 여부

### 치과 증상 의사 추천
- 증상 / 해당 과 라벨링
- 의사 / 이름 / 주소 / 좌표 / 근무 의사 현황 / 개업일자
- 논문 / 이름 / 라벨링

### 브런치 글 추천
- 글의 메타데이터( 등록 시간 , 아이디, 식별 번호..)
- 글 정보( 글 식별번호 , 작성자 아이디)
- 사용자( 사용자 아이디, 키워드 리스트 , 구독 리스트)
- 매거진( 매거진 태그 리스트 , 매거진 아이디)
  
 ### 공간대여 웹 서비스
  - Nosql(MongoDB)
  - 로그인(ID, PW, 사용자 정보)
  - 게시판(제목, 부제목, 위치, 가격, 이미지 , 유저ID, 카테고리)

## 통계 지식
- 모집단(Population)
-- 조사의 관심이 되는 전체 집단
-- 정의는 명확하고 구체적
- 표본(Sample)
-- 일부 실제 조사한 대상
- 모수(Parameter)
-- 모집단으로 부터 계산된 값
-- 전수조사를 하지 않는한 알수 없는 미지의 수
- 통계량(Statics)
-- 표본으로 부터 계산된 값
-- 일반적으로 이를 가지구 모수 추정
  ![enter image description here](https://i.ibb.co/PDqX5J2/1-1.png)

- 명목척도
-- 응답자를 단지 분류할 목적으로 숫자 부여 -> 범주형
-- Ex) 성별 , 증상 -> 과

- 서열 척도
-- 응답자 간에 순서 서열 의미 -> 범주형
-- Ex) 학력

- 등간 척도
-- 응답자 순서 + 숫자의 간격이 동일하여 양적인 정도
-- 연속형
-- Ex) 온도 , 성적

- 비율 척도
-- 등간척도와 유사 But 0 값은 '실제로 없다' -> 연속형
-- Ex) 소득 , 키 , 몸무게

- Independent 사건
-- 발생된 사건이 확률에 영향을 미치지 않는다. 
- Dependent 사건
-- 한번 시행된 사건으로 인해 다음에 발생할 사건에 영향

-	복원 추출
-- 집단에서 또는 한 표본에서 하나를 선택한 후 다시 넣고 재추출

-	비복원 추출
-- 선택된 것을 다시 표본에 넣지 않고 나머지 중에서 추출

![enter image description here](https://i.ibb.co/z4B0qcV/1.png)
- 조건부 확률
> 한 사건이 일어날 것을 전제로 다른 사건이 일어날 확률
![enter image description here](https://i.ibb.co/NmSJh9z/1-2.png)
- 결합 확률
> 사건 A , B 가 동시에 발생할 확률
![enter image description here](https://i.ibb.co/Z2TTFML/1-1.png)

참고 = https://m.blog.naver.com/aporia25/221152554185

## FDS란?

  

## API 개발 경험
- 안심 귀가 APP 및 공간 대여 서비스 WEB 구축하면서 카카오 MAP , 도로명 주소 사용해보았다.
- 공간 대여 서비스 WEB에서 Kakao 결제 서비스를 가상에서만 구현해봄(실제 서비스 X)