## 보안 제어 

---

### 🌱 IP 주소 기반 접근 제어

```shell
location /test/ {
  deny 10.0.0.1;
  allow 10.0.0.0/20
  allow 2001:0db8::/32;
  deny all
}
```

`allow`와 `deny` 지시자는 http, server, location 과 TCP/UDP 에 대한 stream server 컨텍스트에서 사용 가능.

`allow` 의 경우 해당 IP에 대한 접근을 허용을 의미하며 `deny`의 경우에는 거부하는것으로 한다. 
접근이 차단되면 403응답을 받는다.

---

### 🌱 크로스 오리진 리소스 공유(CORS)

```shell
map $request_method $cors_method {
  OPTION 11;
  GET     1;
  POST    1;
  default 0;
}

server {
 #... 
 location / {
   if($cors_method ~ '1') {
    add_header 'Access-Control-Allow-Methods' 'GET,POST,OPTIONS';
    add_header 'Access-Control-Allow-Origin' '*.example.com';     
    add_header 'Access-Control-Allow-Headers'
               'DNT
                Keep-Alive,
                User-Agent,
                X-Requested-With,
                If-Modified-Since,
                Cache-Control,
                Content-Type';
   }
   
   if($cors_method = '11') {
      add_header 'Access-Control-Max-Age' 1728000;
      add_header 'Content-Type' 'text/plain; charset=UTF-8';
      add_header 'Content-Length' 0;
      return 204  
   }
}
```

map 지시자를 사용하여 GET, POST 메서드를 그룹화하여 처리한다, OPTIONS 메서드는 프리플라이트 요청으로
사용자에게 서버가 가진 CORS 정책을 응답한다.

해당 내용은 요청시 `Access-Control-Allow-Origin` 헤더를 통해 http://example.com 하위 도메인에서 서버 리소스에 접근 가능함을 려준다.

또한 프리플라이트 요청을 매번 보내지 않고도 CORS 정책을 참고할 수 있도록 `Access-Control-Max-Age`시간을 섲엏나다.

---

### 🌱 클라이언트 측 암호화

`ngx_http_ssl_module`, `ngx_stream_ssl_moldule`과 같은 SSL모듈을 사용해 트래픽을 암호화 할 수 있다.

```shell
http {
  server {
    listen 8443 ssl;
    ssl_certificate /etc/nginx/ssl/example.crt;
    ssl_certificate_key /etc/nginx/ssl/example.key;
  }
}
```

8443 포트로 들어오는 요청에 대해서 SSL/TLS 를 사용하여 암호화하도록 한다. 
`ssl_certificate` 지시자는 인증서와 중간 체인 인증서가 저장된 파일 경로를 정의한다. 
`ssl_certificate_key` 지시자는 엔진엑스가 클라이언트 요청을 복호화하고 응답을 암호화 하는데 사용할 비밀키 파일을 정의한다.

---

### 🌱 고급 클라이언트 측 암호화

클라이언트 측 암호화보다 높은 수준으로 성정하기 위해서는 `고급 클아이언트 측 암호화`가 존재한다.

http와 stream의 엔진엑스 SSL모듈은 수신된 요청과 SSL/TLS 연결협상을 제어한다.

인증서와 키 파일은 설정을 통해 해당 파일 경로 값을 지정하면 된다. 

엔진엑스는 설정된 내용에 따라 사용가능한 프로토콜, 암호화 스위트, 키 형식을 클라이언트에게 제공한다.

클라이언트와 엔진엑스 서버는 연결 맺는 과정에 사용 간으한 가장 높은 수준의 보안 표준을 사용한다. 일정시간 동안 캐시해 빠른 응답을 제공하는데
사용할 수 있다.

```shell
http {
  server {
    listen 8443 ssl;
    
    # 허용할 TLS 버전과 암호화 알고리즘을 설정헌다.
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    
    # RSA 인증서 파일 경로 지정 
    ssl_certificate /etc/nginx/ssl/example.crt;
    
    # RSA 암호화 키 파일 경로를 지정
    ssl_certificate_key /etc/nginx/ssl/example.key;
    
    # EV 인증서를 변수에서 불러온다.
    ssl_certificate $ecdsa_cert;
    
    #EV 키를 파일경로가 담긴 변수를 참조해 읽어온다.
    ssl_certificate_key data:$ecdsa_key_path;
    
    # 클라이언트-서버 간의 SSL/TLS 연결 협상 결과를 캐시한다.
    ssl_session_cache shared:SSL:10m;
    ssl_session_timeout 10m;
  }
}
```

TLS 1.2, TLS 1.3 버전을 사용하도록 하였으며 , `ssl_ciphers`지시자는 TLS 표준이 제시하는 높은 수준의 암호화 알고리즘을 사용하도록 
HIGH로 지정하고 aNULL과 MD5는 사용하지 않도록 명시적으로 느낌표를 붙여 지정하였다.

> `aNULL` : 인증 기능이 없는 cipher suite. 따라서, Man-In-The-Middle (MITM) 공격에 취약함.
> `MITM`은 두 사용자간의 통신을 가로채어 정보를 도청, 조작 또는 도난하는 유형의 공격을 의미. 데이터 흐름일 감시하고 제어한다.

---

### 🌱 업스트림 암호화
