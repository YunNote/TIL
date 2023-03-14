
## 프로그래머빌리티와 자동화

> 프로그래머빌리티란 프로그래밍을 통하여 상호작용하는 능력을 말한다. 

### 🌱 엔진엑스 플러스 API

```shell
upstream backend {
  zone http_backend 64k
}

server {
  
  # location 블럭을 통해 API 활성화
  location /api {
    api [write=on];
  }
  
  # nginx 대시보드 접근가능하도록 설정 
  location = /dashboard.html {
    root  /usr/share/nginx/html;
  }
}
```
위와같이 작성하면 API를 사용할 수 있게되면 API를 통해 업스트림 서버를 추가할 수 있다.

```shell
$ curl -X POST -d '{"server" : 172.17.0.3}' \
    'http://nginx.local/api/3/http/upstreams/backend/servers/'
```

위와 같이 작성하면 curl 을 통해 엔진엑스 플러스의 업스트림 서버 설정에 새로운 서버를 추가하게 된다.

-----------

```shell
# /api/{version}/http/upstreams/{httpUpstreamName}/servers/
$ curl 'http://nginx.local/api/3/http/upstreams/backend/servers/'
```

다음과 같이 curl 전송시 업스트림 서버 풀에 포함된 모든 서버를 반환해준다. (응답값은 책에서 확인)

해당 curl은 이름이 backend인 업스트림 서버풀에 포함된 모든 서버 목록을 가져온다.


-----------

업스트림 서버 풀에 추가하는것과 반대로 서버를 제외하기 위해서는 해당 서버의 연결이 모두 종료되어야 하며, 다음과 같이 점진적으로 종료할 수 있다.
```shell
# PATCH 메서드를 사용하여 특정 서버의 연결을 감소하다도록 지시. 
# 대상서버의 IP는 URI의 맨 마지막에 포함. 
# 하단의 URI 에서는 0을 의미하며, 서버풀을 추가하였을때 생성되는 ID를 의미한다.
$ curl -X PATCH -d '{"drain": true}' \ 
  'http://nginx.local/api/3/http/upstreams/backend/servers/0'
  
```

-----------

위에서 나온 내용으로는 특정 서버의 연결이 모두 종료되어야 해당 서버를 제거할 수있다고 하였다. 
그렇다면 연결 갯수를 확인해야하는데 서버가 맺은 연결 현황을 보기위해서는 다음명령어를 통해 확인 할 수 있으며 `active` 속성값을 확인한다.

```shell
$ curl 'http://nginx.local/api/3/http/upstreams/backend'
# response
{
  "zone": "http_backend",
  "keepalive":0,
  "peers": [
    {
      "backup":false,
      "id":0,
      "unavail":0,
      "name": "172.17.0.3",
      "requests": 0,
      "received": 0,
      "state": "draining",
      "server": "172.17.0.3:80",
      "active" : 0,
      ... 이하 생략
      
    }
  ]
}
```

`active` 갯수를 확인 후 모든 연결이 종료되었다면 아래 명령어를 통해 업스트림 서버 풀에서 해당 서버를 제거한다.

```shell
# DELETE 메서드를 통해 해당 서버ID를 업스트림 풀에서 삭제한다. 
$ curl -X DELETE 'http://nginx.local/api/3/http/upstreams/backend/servers/0'
```

> nginx 플러스는 유료라 직접 테스트 해보지는 못했다.

----------

### 🌱 키-값 저장소 사용하기 (엔진엑스 플러스)

```shell
keyval_zone zone=blocklist:1M;
keyval $remote_addr $blocked zone=blocklist;

server {
  #...
  location / {
    if($blocked) {
      return 403 'Forbidden';
    }
    
    return 200 'OK';
  }
}

server {
  #... 
  location /api {
    api write=on;  
  }  
}
```

`keyval_zone` 지시자를 통해 blocklist라는 1메가바이트의 공유 메모리 생성.<br>
`keyval`지사자는 $remote_addr을 값과 일치하는 키값이 있다면 해당 키값을 $blocked 변수에 저장한다.
저장된 변수는 403 Forbiddend 으로 응답할지 200 OK로 응답할지 결정하는데 사용된다.

```shell
$ curl 'http://127.0.0.1'
OK
```
 127.0.0.1을 호출하면 현재 blocklist에 등록되어 있지 않기때문에 정상적으로 OK를 반환한다.

```shell
$ curl -X POST -d '{"127.0.0.1": "1"}' 'http://127.0.0.1/api/3/http/keyvals/blocklist'
```
다음과 같이 POST메서드로 키-값을 등록한다. 다음과 같이 등록되면 상단에 있는 127.0.0.1조회를 하면
해당 IP가 blocklist에 추가되어있기때문에 Forbidden을 반호나하게 된다.

만약 해당 키-값을 갱신하거나 삭제하려면 PATCH를 사용한 후 json값에 1대신 null을 대입한다.
```shell
$ curl -X POST -d '{"127.0.0.1": null}' 'http://127.0.0.1/api/3/http/keyvals/blocklist'
```

-----------

### 🌱 NJS 모듈로 엔진엑스 자바스크립트 기능 활용하기

데비안/우분투 계열 엔진엑스에서 nginx-module-njs 설치
```shell
$ apt-get install nginx-module-njs

# 자바스크립트 리소스를 위한 디렉터리 생성
$ mkdir -p /etc/nginx/njs
``` 
해당 도서에서는 JWT토큰을 예제로 사용하였으며, njs 모듈을 불러오고, 작성한 자바스크립트 파일을 임포트 한다. 자바스크립트 함수가
반환한 값을 엔진엑스 변수에 저장하고 해당 변수들을 활용하여 로직을 검증한다.

----------

### 🌱 상용 프로그래밍 언어로 엔진엑스 확장하기
nginx 모듈을 다양한 언어로 쓸 수 있다. 대표적으로는 위에서본 NJS가 있으며 그 외에도 루아와 펄모듈또 한 사용 가능하다.
이러한 언어 모듈을 통해 코드가 작성된 파일을 불러오거나 엔진엑스 설정 내부에 직접 코드 블록을 장성한다.

해당 언어로 사용하기 위해서는 관련된 해당ㄷ 모듈을 설치한다음 코드블록 형태로 코드를 작성하면된다.

해당 도서에 루아, 펄을 통한 설정에 대한 내용은 직접 보길 바랍니다 P.85

