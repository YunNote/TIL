
## Nginx 실습을 위한 Docker 환경 세팅

```shell
# 버전 ubuntu 22.04

docker container run -it -v /Users/choiyunjin/nginx-volume:/volume --name ubuntu ubuntu:22.04

# shell 접속 후 
apt-get update
apt install -y gnupg2 ca-certificates lsb-release debian-archive-keyring

# nginx 패키지 저장소 서명키 다운로드
curl https://nginx.org/keys/nginx_signing.key | gpg --dearmor | tee /usr/share/keyrings/nginx-archive-keyring.gpg >/dev/null


# apt 소스파일 생성 
# echo $OS => ubuntu 출력
OS=$(lsb_release -is | tr '[:upper:]' '[:lower:]')
RELEASE=$(lsb_release -cs)
echo "deb [signed-by=/usr/share/keyrings/nginx-archive-keyring.gpg] http://nginx.org/packages/${OS} ${RELEASE} nginx"  | tee /etc/apt/sources.list.d/nginx.list 


## 패키지 정보 업데이트 후 nginx 설치 
apt-get update
apt-get install -y nginx
nginx -version


## docker 실행 후 port 바인딩 시켜야할때...

# 컨테이너 종료
docker stop {containerID}

# 기존 Container를 Image로 저장
docker commit {containerID} {imageName}

# 저장된 Docker Image로 Container 실행 
docker run --name {name} -p {local-port}:{docker-port} -it -v {local-path}:{docker-path} {imageName} /bin/bash
## sample ## 
# docker run --name yunjin-ubuntu2204 -p 80:80 -it -v nginx-volume:/volume yunjin-ubuntu2204 /bin/bash

```
다음과 같이 설정하면 `localhost:80`으로 접근시 docker에 올라간 nginx 환경에 접근 가능.