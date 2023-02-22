
## Nginx 고성능 부하분산

오늘날에는 높은 성능과 가용성이 필요하다, 이를 위해 같은 시스템을 여러개로 운영하고 부하를 각 시스템으로 분산한다.
 
`nginx`와 같은 프록시 또는 `로드 밸런서`서버는 업스트림 서버의 문제를 감지할 수 있어야 하며, 문제 발견 시 트래픽 전송을 중지할 수 있어야한다. 그렇지 않다면 사용자가 서버의 응답을 기다리다가 결국 타임아웃오류를 보게된다.

해당 문제를 찾기위해서 프록시 서버와 로드밸런서 서버가 업스트림 서버의 상태를 확인하도록 하는 방법이 있다.

`nginx` 에서는 `패시브 방식`을 제공하며 `nginx 플러스`에서는 추가로 `액티브 방식`을 제공한다.

> #### 액티브 방식
> - 로드 밸런서 장비가 스스로 업스트림 서버와 주기적으로 연결을 시도하거나 요청을 보내 서버 응답에 문제가 없는지 확인하는 방식.
>   업스트림 서버의 상태를 사용자 요청을 받기전에 미리 확인해야 할 때 유용하다
> 
> #### 패시브 방식
> 
>  - 사용자의 요청을 로드밸런서가 받은 시점에 업스트림 서버와의 연결이나 응답을 확인하는 방식, 업스트림 서버의 부하를 늘리지 않으면서 상태를 확인하려면
>    패시브 방식을 사용하는 편이 좋다.


## HTTP 부하분산, TCP 부하분산 

### 🌟 HTTP 부하분산
> HTTP부하 분산은 nginx의 upstream 블록과 http 모듈을 이용하여 서버간에 부하를 분산한다.

```shell
# 다음과 같이 설정하면 해당 위에 서버 2대를 통해 연결하며, 위 2대와 연결이 불가능할 경우 backup 서버를 사용한다.
# weight의 기본값은 1이며 해당 값을 생략할 수 있다, weight 1, 2를 다음과 같이주면 
# `test.sample.com`서버가 `10.10.10.10`서버에 비해 2배 많은 요청을 받는다.

upstream backend {
    server 10.10.10.10:80        weight=1;
    server test.sample.com:80    weight=2;
    server backup.sample.com:80  backup;
}

server {
    location / {
        proxy_pass http://backend;
    }
}
```

부하분산을 위한 목적지 정보는 유닉스 소켓, IP주소, DNS 혹은 다음 값들의 조합으로 구성한다.
해당 값들을 매개변수와 함께 지정하면 추가 제어방법을 제공한다. 매개변수들을 통해
분산 알고리즘에 가중치를 적용하거나 서버가 어떤 상태인지 알려주며, 서버 가용 여부를 판단하는 방법을 포함한다.

---

### 🌟 TCP 부하분산
> TCP 부하분산은 nginx의 upstream블록과 stream 모듈을 이용하여 TCP 서버간에 부하를 분산한다.

```shell

stream {
   
    # 3306 포트로 요청을 받아 읽기 전용 test1, test2로 구성된 MySQL서버로 부하를 분산한다.
    # HTTP 부하분산과 동일하게 2개의 MySQL서버가 다운되면 backup 서버로 요청을 전달한다.
    upstream mysql_read {
      server test1.sample.com:3306 weight=5
      server test2.sample.com:3306;
      server 10.10.10.10:3306 backup;      
    }
    
    server {
      listen 3306;
      proxy_pass mysql_read;
    } 
}
```

nginx 설치 후 특별한 설정파일을 수정하지 않았다면 기본 설정 파일 경로인 conf.d 폴더는 http블록에 포함된다. 
따라서 stream 모듈을 이용한 이 설정은 stream.conf.d 라는 별도의 폴더를 생성해 저장하는 편이 좋다.

```shell
# /etc/nginx 디렉터리 하위에 stream.conf.d 폴더 생성 후 mysql_read.conf 파일 생성.

# /etc/nginx/nginx.conf
# 하단 설정 추가. 
stream {
  include /etc/nginx/stream.conf.d/*/conf 
}

```

---

### 🌟 http vs stream

http와 stream의 가장 큰 차이점은 해당 두 모듈은 서로 다른 OSI 계층에서 동작한다.
 - http는 7계층인 애플리케이션 계층에서 동작하며 stream은 4게층은 전송계층에서 동작한다.
 - http모듈이 HTTP프로토콜을 완전히 이해하도록 특별히 설계된 반면 stream 모듈은 패킷의 전달 경로 결정과 부하분산에 더 중점을 두었다.


nginx에서 TCP 부하분산은 stream을 사용하지만 http모듈과 마찬가지로 stream모듈도 업스트림 서버 풀을 만들거나 개별 서버를 지정할 수 있다.

stream 모듈을 이용하는 경우 옵션을 통해 TCP 연결과 관계된 리버스 프록시의 여러 속성을 변경할 수 있다. 대표적인 속성으로는
SSL/TLS 인증서 제한, 타임아웃, 킵얼라이브 시간 설정 등이 있다. 일부 옵션은 nginx 변수를 값으로 사용할 수 있는데, 다운로드 속도 제한이나
SSL/TLS 인증서 유효성 검사에서 사용할 이름이 지정된 변수 혹은 이 변수가 포함된 값을 옵션에 사요할 수 있다.

---

### 🌟 UDP 부하분산

> udp 로 정의된 upstream 블록은 nginx stream모듈에서 사용하여 UDP 서버간에 부하 분산을 한다.

```shell
stream {
  
  upstream ntp {
   server ntp1.sample.com:123 weight=1;
   server ntp2.sample.com:123; 
  }
 
 server {
   listen 123 udp;
   proxy_pass ntp;
 } 
}
```

UDP 부하분산은 위에 보았던 TCP 부하분산과 비슷하며 listen 옵션에 `udp`만 추가하면 된다.

UDP와 TCP차이는 listen 지시자를 통해 UDP 데이터그램을 처리할 소켓을 지정한다. 해당 데이터그램을
다루기 위해서는 TCP에서 사용하지 않는 지시자를 몇가지 사용한다. 
대표적으로는 `proxy_response` 지시자를 사용, 해당 지시자를 설정하지 않으면 `proxy_timeout` 지시자의 제한값이 되기 전까지 무제한으로 응답을 처리한다.

* `proxy_timeout`은 연결을 닫기 전에 목적지 서버로의 읽기, 쓰기 작업완료를 기다리는 시간을 지정하는데 사용한다.

---
