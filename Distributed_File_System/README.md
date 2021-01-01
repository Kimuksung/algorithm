
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
>![enter image description here](https://docs.openstack.org/ocata/config-reference/_images/ceph-architecture.png)

## UNIX File System
### Architecture
> File System은 파일을 기록하기 위한 것이다.
> 파일은 속성인 MetaData와 실제 데이터를 기록하는 Data 영역으로 나뉜다.
> ![enter image description here](https://www.livefirelabs.com/unix_tip_trick_shell_script/unix_operating_system_fundamentals/208_global/images/filesystem1.gif)
![enter image description here](https://mblogthumb-phinf.pstatic.net/20140121_147/bitnang_1390307029963jlhn2_PNG/012114_1223_14.png?type=w2)


### Inode
- 파일에 대한 정보 = 아이노드
- offset(독립적으로 저장되어야 할 정보)는 File 디스크립터
- File system에서는 아이노드를 저장하는 영역과 Data 영역을 지정하는 영역이 따로 존재한다.
- 아이노드가 부족하다면 트리의 형태로 추가적으로 만들어준다.
> ![enter image description here](https://mblogthumb-phinf.pstatic.net/20160509_290/eldkrpdla121_14627776275408x5mt_PNG/1.png?type=w2)
![enter image description here](https://mblogthumb-phinf.pstatic.net/20160509_111/eldkrpdla121_1462777261630clhrU_PNG/4.png?type=w2)
![enter image description here](https://mblogthumb-phinf.pstatic.net/20160509_135/eldkrpdla121_1462777627926RJdlU_PNG/2.png?type=w2)
![enter image description here](https://mblogthumb-phinf.pstatic.net/20160509_276/eldkrpdla121_14627780676572FRjh_PNG/1.png?type=w2)
![enter image description here](https://mblogthumb-phinf.pstatic.net/20160510_177/eldkrpdla121_1462863794705bGYVw_PNG/1.png?type=w2)
>![enter image description here](https://mblogthumb-phinf.pstatic.net/20160510_103/eldkrpdla121_1462863875312UcmOw_PNG/1.png?type=w2)

### Metadata
- File의 실제 Data가 저장되어 있는 Index / Owner / Group / 소유자 / 언제 수정 / 언제 접근 등의 파일 속성 데이터가 저장
- File System에서 Data에 접근 시에는 Metadata의 정보를 Memory에 올린 후에 OS가 읽기 요청을 하게 되면 Memory의 Metadata의 정보를 보고 실제 Data를 찾아들어간다.
- metadata 정보 ( inode / 해당 파일의 주인, 그룹, permission, 파일 타입, 하드링크 갯수, 파일 사이즈, 수정날짜, 파일의 첫번째 블락 하드디스크 포인터  / 파일 디스크립터)
> ![enter image description here](https://t1.daumcdn.net/cfile/tistory/25301D4154D85FAE2D)![enter image description here](https://mblogthumb-phinf.pstatic.net/20160509_83/eldkrpdla121_1462777257676cc2Oc_PNG/1.png?type=w2)
![enter image description here](https://mblogthumb-phinf.pstatic.net/20160509_16/eldkrpdla121_1462777258006IjXXd_PNG/2.png?type=w2)
![enter image description here](https://mblogthumb-phinf.pstatic.net/20160509_65/eldkrpdla121_1462777261327q49fI_PNG/3.png?type=w2)
![enter image description here](https://mblogthumb-phinf.pstatic.net/20160509_111/eldkrpdla121_1462777261630clhrU_PNG/4.png?type=w2)
![enter image description here](https://mblogthumb-phinf.pstatic.net/20160509_135/eldkrpdla121_1462777627926RJdlU_PNG/2.png?type=w2)
### 클러스터
> OS가 File system을 생성 하고 저장 장치의 크기를 고려하여 클러스터의 크기 조절![enter image description here](https://mblogthumb-phinf.pstatic.net/20140121_1/bitnang_1390307029668qQYlj_PNG/012114_1223_13.png?type=w2)
- 만약 10KB 파일을  읽을  경우  
- 클러스터가 1KB라면 10번 I/O
- 클러스터  크기가 4KB라면 3번의 I/O
-  FAT16과  같이  파일시스템  주소  지정  방식에 16Bit
- 클러스터의  크기가 1KB라면  저장장치의  크기는 65,536(216) X 1,024(1KB) = 64MB
- 클러스터의  크기가 4KB라면  저장장치의  크기는 65,536(216) X 4,096(4KB) = 256MB

### 디렉토리

- 디렉토리는 해당 inode와 파일명과 맵핑되어 있는 정보를 갖는 파일  
- 파일들을 계층화 그룹화 => Link로 발전하는 file system도 있다
- Architecture를 보게 되면 파일과 유사

### Link

- metadata 정보 ( inode / 해당 파일의 주인, 그룹, permission, 파일 타입, 하드링크 갯수, 파일 사이즈, 수정날짜, 파일의 첫번째 블락 하드디스크 포인터  / 파일 디스크립터)
![enter image description here](https://t1.daumcdn.net/cfile/tistory/25301D4154D85FAE2D)
1. Hard Link
- inode를 서로 다른 파일명으로 지칭할 수 있나? -> 가능하다.  
- 실제 내용을 가지고 있는 영역은 한 개이다.
- 원파일이 사라지면 하드링크도 사라짐.
- 하드링크의 단점 : 파티션 경계를 넘어갈 수 없다.
![enter image description here](https://t1.daumcdn.net/cfile/tistory/246CEE3754D866871A)
2. Soft Link
- 타겟 파일 자체에 대한 위치의 포인터 값을 담고 있는 것(해당파일의 물리적 경로)  
- 파티션 경계를 넘을 수 있다.
- 원본파일이 없어져도 소프트링크는 인식을 못한다.(리눅스가 인식하여 표시해준다.)  

![enter image description here](https://t1.daumcdn.net/cfile/tistory/23320C3754D877151A)
![enter image description here](https://t1.daumcdn.net/cfile/tistory/221D294A54D87A4812)
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
https://kshmc.tistory.com/entry/12-%ED%8C%8C%EC%9D%BC-%EC%8B%9C%EC%8A%A4%ED%85%9C-inode-value-%EB%B0%8F-%ED%95%98%EB%93%9C%EB%A7%81%ED%81%AC