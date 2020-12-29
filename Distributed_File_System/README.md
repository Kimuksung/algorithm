
# 확장 가능한 고성능 파일 분산 시스템

## 분산 파일 시스템이란?
>네트워크를 이용해 접근하는 파일 시스템

Ex) 
1. HDFS ( Google File System ) 영향을 받아 만들어진 오픈소스 파일 시스템
- 상대적으로 저비용의 하드웨어(commodity server)를 사용 -> 낮은 비용으로 고용량 저장소 구축 가능	
-   크기가 큰 파일이 청크 단위로 나뉘어 여러 데이터노드에 분산 복제 저장
-   청크 크기는 보통 64MB이고, 각각의 청크는 3개의 복제본이 존재하며, 서로 다른 데이터 노드에 청크가 저장
-   청크 정보는 네임노드에 저장
-   대용량의 파일 저장하는 데 유리 / 파일의 개수가 많으면 네임노드의 부담이 커짐
-   네임노드가 SPOF(Single Point Of Failure). 네임노드에 장애가 발생하면 운영 불가 상황이 발생하며 수동 복구 필요
>![enter image description here](https://d2.naver.com/content/images/2015/06/helloworld-258077-3.png)
2. NFS ( Network File system)
- 일반적으로 Linux / Unix 환경에서 사용
- 네트워크를 통하여 다른 호스트에 있는 파일을 공유해 사용
- 로컬 파일 시스템과 동일한 기능 제공
- NAS를 사용하는 경우가 많기 때문에 NAS에 대한 높은 구매 비용 필요
- NAS는 OwFS와 HDFS에 비하여 확장성이 크게 떨어짐
- 파일 스토리지 기반
>![enter image description here](https://d2.naver.com/content/images/2015/06/helloworld-258077-1.png)
3. CIFS ( Common Internet file system)
- 일반적으로 Window 환경에서 사용
- IBM에서 개발한 SMB(Server Message Block) 바탕으로 보안 등의 기능 개선
-  NAS를 사용하는 경우가 많기 때문에 NAS에 대한 높은 구매 비용 필요
- NAS는 OwFS와 HDFS에 비하여 확장성이 크게 떨어짐
4. OwFS( Owner-based File system)
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

5. Ceph
-
참고  = https://d2.naver.com/helloworld/258077
https://www.redhat.com/ko/topics/data-storage/network-attached-storage
https://www.redhat.com/ko/topics/data-storage/file-block-object-storage
https://www.kdata.or.kr/info/info_04_view.html?field=&keyword=&type=techreport&page=116&dbnum=146422&mode=detail&type=techreport