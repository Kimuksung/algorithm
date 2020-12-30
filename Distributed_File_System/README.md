
# 확장 가능한 고성능 파일 분산 시스템

## 분산 파일 시스템이란?
>네트워크를 이용해 접근하는 파일 시스템

## 1. HDFS ( Google File System ) 영향을 받아 만들어진 오픈소스 파일 시스템
- 상대적으로 저비용의 하드웨어(commodity server)를 사용 -> 낮은 비용으로 고용량 저장소 구축 가능	
-   크기가 큰 파일이 청크 단위로 나뉘어 여러 데이터노드에 분산 복제 저장
-   청크 크기는 보통 64MB이고, 각각의 청크는 3개의 복제본이 존재하며, 서로 다른 데이터 노드에 청크가 저장
-   청크 정보는 네임노드에 저장
-   대용량의 파일 저장하는 데 유리 / 파일의 개수가 많으면 네임노드의 부담이 커짐
-   네임노드가 SPOF(Single Point Of Failure). 네임노드에 장애가 발생하면 운영 불가 상황이 발생하며 수동 복구 필요
>![enter image description here](https://d2.naver.com/content/images/2015/06/helloworld-258077-3.png)
## 2. NFS ( Network File system)
- 일반적으로 Linux / Unix 환경에서 사용
- 네트워크를 통하여 다른 호스트에 있는 파일을 공유해 사용
- 로컬 파일 시스템과 동일한 기능 제공
- NAS를 사용하는 경우가 많기 때문에 NAS에 대한 높은 구매 비용 필요
- NAS는 OwFS와 HDFS에 비하여 확장성이 크게 떨어짐
- 파일 스토리지 기반
- 중앙 집권적
- 네트워크 대역폭이 제한되어 있기 때문에 장애의 원인이 될 수 있다(대역폭을 늘려야 함)
- 하지만 Client들의 대역이 좋지 못하면 소용이 없다
>![enter image description here](https://d2.naver.com/content/images/2015/06/helloworld-258077-1.png)
## 3. CIFS ( Common Internet file system)
- 일반적으로 Window 환경에서 사용
- IBM에서 개발한 SMB(Server Message Block) 바탕으로 보안 등의 기능 개선
-  NAS를 사용하는 경우가 많기 때문에 NAS에 대한 높은 구매 비용 필요
- NAS는 OwFS와 HDFS에 비하여 확장성이 크게 떨어짐
## 4. OwFS( Owner-based File system)
- 상대적으로 저비용의 하드웨어(commodity server)를 사용 -> 낮은 비용으로 고용량 저장소 구축 가능
-  Owner라는 컨테이너 개념. Owner는 하나의 파일 시스템이며 Owner가 모여 전체 파일 시스템을 이룬다.
-   DS에 Owner 정보(파일 데이터와 메타데이터)를 저장
-   하나의 DS에 여러 Owner를 저장할 수 있고, Owner는 서로 다른 DS에 분산 저장(복제)돼 있음
-   복제본 위치를 포함한 Owner에 대한 위치 정보는 MDS(Metadata Data Server)에 저장
-   수십 메가바이트 이내의 많은 수의 파일을 처리하기에 적합함
-   모든 구성 요소가 이중화, 삼중화돼 있어 장애가 발생해도 안정적으로 동작함
>![enter image description here](https://d2.naver.com/content/images/2015/06/helloworld-258077-2.png)
장점
-여러 Host에서 저장한 정보 공유 가능하다.

## 5. Ceph
### storage cluster
- Monitor / Manager / OSD(Object storage daemon)
### metadata server cluster
-
### Architecture
><img src="https://ibb.co/nPCk0Y6"/>

# 용어 정리
하나의 File을 5개의 Chunk로 나누었다고 생각하고
DataNode가 5개 있다 생각하면
Chunk1 = 1,2,3
Chunk2 = 1,2,5
Chunk3 = 2,3,5
Chunk4 = 1,2,4
Chunk5 = 3,4,5

이와 같이 'Chunk1 =1,2,3' 을 metadata로 나타낸 뒤 namenode에 기억하구 있어서 
나중에  namenode에 있는 것을 mapping 하여 해당되는 Data를 꺼내쓴다 라구 생각하면 될듯


- metadata = 파일에 관련된 정보( 위치 / 크기 /...)
- namenode = 기존의 FileSystem에서 관리하는 것을 하나의 폴더 안에 Data를 넣어두고 이를 metadata형태로 관리 ( 
- datanode = 실제 Data가 저장되는 공간(즉, 실제 Server의 DB 공간)
- chunk = 하둡에서는 하나의 File을 여러개로 분할하여 나타내는데 이 때의 단위
- RAID = Disk에서는 분산 처리 시 Data를 어떻게 저장할 건지를 나타내는 단위인데 (RAID0 은 각각 Disk에 data를 하나씩만 저장하여 복구 불가X)
- 확장성 = 사용자가 늘어나도 무리가 오는지 정도
- 워크로드 = 주어진 기간 동안 시스템에 의해 실행되어야 할 작업의 할당량

참고  = https://d2.naver.com/helloworld/258077
https://www.redhat.com/ko/topics/data-storage/network-attached-storage
https://www.redhat.com/ko/topics/data-storage/file-block-object-storage
https://www.kdata.or.kr/info/info_04_view.html?field=&keyword=&type=techreport&page=116&dbnum=146422&mode=detail&type=techreport
