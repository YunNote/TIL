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

엔진엑스와 업스티림 서비스간 트래픽 암호화를 하고, 컴플라이언스 법규 준수 및 보안 네트워크 밖에 있는
업스트림 서비스와의 연결을 하기 위해서는 HTTP프록시 모듈의 SSL 지시자를 사용해야한다.


> 컴플라이언스(Compliance)는 조직이나 기업이 법적, 규제적, 윤리적 요구사항을 준수하는 것을 의미합니다. 다양한 법규와 규제들이 있지만, 여기서는 대표적인 법규들을 알아보겠습니

```shell
location / {
  proxy_pass https://upstrea.example.com;
  proxy_ssl_verify on;
  proxy_ssl_verify_depth 2;
  proxy_ssl_protocols TLSv1.2;
}
```

proxy 지시자들은 엔진엑스가 준수해야 하는 SSL 규칙을 정의한다.<br>
`proxy_ssl_verify_depth`의 경우 인증서와 인증서 체인이 2단계 까지 유효한지 확인한다.<br>
`proxy_ssl_protocols TLSv1.2`를 통하여 TLS 1.2 버전만 SSL 연결 설정에 사용하도록 설정.

> 기본적으로 엔진엑스는 업스트림 서버의 인증서와 연결할 때 사용한 TLS 버전을 확인하지 않는다.

---

### 🌱 location 블록 보호하기

secure link 모듈과 secure_link_secret 지시자를 사용하여 secure link를 가진 사용자만 리소스에 접근하도록 허용한다.

```shell

location /resources {
  secure_link_secret mySecret;
  if($secure_link = "") { return 403; }
  
  rewrite ^ /secured/$secure_link;
}

location /secured/ {
  internal;
  root /var/www;
}
```

해당 설정은 공개된 location 블록과 내부에서만 접근 가능한 location 영역을 만든다. /re4sources 경로에 대해 설정된 공개
location 블록은 요청 URI가 secure_link_secret지시자에 설정된 비밀값으로 검증 가능한 md5해시값ㅇ르 가지고
있지 않으면 403을 반환한다, $secure_link 변수는 URI 포함된 해시값이 검증되기 전까지는 아무런 값을 갖지 않는다.

> 개인 실습 테스트

```shell
# default.conf 에 하단 내용 추가 
location /resources {
    secure_link_secret mySecret;
    if ($secure_link = "") { return 403; }

    rewrite ^ /secured/$secure_link;
}

location /secured/ {
    internal;
    root /var/www;
}

```

직접 실습을 통해 테스트 해보았습니다.
`internal;` 을 설정의 차이는 해당 internal; 설정을 한 경우에는 직접적으로 secured경로를 통해 접근 불가능함. 해당 설정을 추가하면
오로지 secure_link를 통해서만 접근가능.

`mySecret을 통해 파일의 md5 만드는법`<br>
```shell
# /var/www/secured 하위에 있는 파일명 + secure_link_secret 값을 문자열 연결 후 md5 암호화
echo -n 'test.htmlmySecret' | openssl md5 -hex
## f33c627034f3192a0e74f806fa3a54f6 : md5 암호화된 값
```

위 설정대로 /secured path는 resources/{md5}/접근경로 를 통해서만 접근가능 하도록 한다는 설정이 추가되었으며.
/secured path의 root는 /var/www로 설정하였다.


예를 들어 /var/www/secured/test.html 이 있다고 가정한다면 
`echo -n 'test.htmlmySecret' | openssl md5 -hex` md5 암호화를 거친 후<br>

```http request
http://localhost/resources/f33c627034f3192a0e74f806fa3a54f6/test.html
```

위와 같이 접근을 하면 된다.

다음과 같이 작성하면 실제 test.html 파일의 경로를 감출 수 있다. <br> 
또한 md5의 값과 요청하고자 하는 파일의 명이 다르다면 403으로 접근 실패한다.

---

### 🌱 비밀값으로 보안링크 생성하기.

nginx의 secure link 모듈은 URI경로와 비밀값을 연결한 문자열로 생성한 md5 해시의 16진수 다이제스트를 인식한다.
위의 location블록 보호하기의 내용과 연관.

---

### 🌱 기간 제한 링크로 location 블록 보호하기 (실습 실패..)

```shell
location /resources {
  root /var/www;
  secure_link $arg_md5,$arg_expires;
  secure_link_md5 "$secure_link_expires$uri$remote_addrmySecret";
  if ($secure_link = "") { return 403; }
  if ($secure_link = "0") { return 410; }
}
```

`secure_link`지시자는 쉼포로 구분된 매개변수 두개를 사용하여 queryString으로 전달 받을 수 있다.

해시가 검증지 않으면 $secure_link에 값이 저장되지 않으며, 검증되더라도 만료시간이 초과된다면 $secure_link변수값은 0이된다.

---

### 🌱 기간 제한 링크 생성하기.

```shell
# 유닉스 시스템
date -d "2030-12-31 00:00" +%s --utc
# 1924905600
```

`"$secure_link_expires$uri$remote_addrmySecret";` 다음과 같이 secure_link_md5를 설정하였기 떄문에
해당 내용과 같이 문자열을 암호화 한다.

따라서 문자열은 `1924905600/resources/index.html127.0.0.1mySecret`이 된다. 

#### 암호화 방법 
```shell
# 
echo -n '1924905600/resources/index.html127.0.0.1mySecret' \ 
 | openssl md5 -binary \ 
 | openssl base64 \ 
 | tr +/ -_ \
 | tr -d =
```
`+`기호는 `-`으로, `/`기호는 `_`기호로 변경, `=`기호는 삭제됩니다.

해당 실행을 통해 해시값을 얻고 링크 만료시점 정보와 함께 URL에 요청하면 된다.
파이썬으로 테스트 필요.



---

### 🌱 HTTPS 리다이렉션

```shell
server {
  listen 80 default_server;
  listen [::]:80 default_server;
  server_name _;
  return 301 https://$host$request_uri
}
```

위와 같이 지정후 nginx reload한후 접근하게 된다면 IPv4, IPv6 주소를 가리지 않고 80포트로 요청을 받는다.
return 구문은 301 Permanent Redirect 응ㄷ갑을 보내 동일한 호스트명과 uri 에 대해서 다시 HTTPS로 요청하도록 한다. 

![img.png](img.png)

---

### 🌱 HTTPS 리다이렉션 - SSL 오프로딩 계층이 있는경우

> 엔진엑스가 실제 사용자의 요청을 수신하는 경우가 아니라면 X-Forwarded-Proto 헤더를 통해 사용자의 프로토콜을 확인할 수 있으며
> 이값을 활용하여 리다이렉트를 한다.

```shell
server {
  listen 80 default_server;
  listen [::]:80 default_server;
  server_name _;
  
  if ($http_x_forwarded_proto = 'http') {
    return 301 https://$host$request_uri
  }  
}
```

위에 나온 일반 리다이렉션과 비슷해보이지만 x-forwarded-proto 헤더값이 http인 경우에만 301 리다이렉트 응답을 한다.


---

### 🌱 HSTS 
Strict-Transport-Security 헤더를 설정하면 HSTS확장을 사용할 수 있다.
```shell
# 헤더를 유효기간 1년으로 지정하여 헤더를 전달한다, 해당 도메인에 대해 HTTP요청이 발생하면 내부 리다이렉트를 통해 모든 요청이 항상 HTTPS를 이용하도록 한다.
add_header Strict-Transport-Seecurity max-age=31536000;
```

> 해당 설정이 중요한 이유는 일반적으로 POST요청의 폼 데이터에 민감한 정보들이 담기지만 HTTP로 전송이 된다면 엔진엑스의 HTTPS 리다이렉트 응답은 도움이 되지 않는다.
> 왜냐하면 HTTPS로 리다이렉트 되기전에 이미 평문으로 데이터가 탈취되어 상황이 끝났을수도 있다. 따라서 근본적으로는 HTTP로 요청을
> 보내지 못하게 함으로써 요청이 암호화되지 않은 상태로 전송되는상황을 방지한다.
 
---

### 🌱 다중 계층 보안

`satisfy` 지시자를 사용하면 설정 옵션에 따라서 모든 보안 검증을 통과해야만 요청을 허용할 것인지, 일부 보안 검증만
통과해도 유효한 요청으로 볼지 설정한다.

`satisfy` 지시자는 `any`와 `all` 값을 가지게 되며 `all`일 경우 모든 요청에 대해서 통과해야지만 유효한 요청으로 판단.
`any`일 경우에는 하나 이상을 만족하면 유효한 요청으로 판단한다.

`satify`는 다양한 지시자들과 함께 사용할 수 있다, 높은 수준의 보안 정책을 요구하는 location, server블록에 `satisfy`지시자를 적용할 수 있다.


---

엔진엑스 플러스에 대한 내용은 도서 참고 . 

---

### 🌱 다중 계층 보안(엔진엑스플러스)
엔진엑스 플러스를 사용하면 클러스터 레벨으 rate limit 과 자동화된 차단리스트를 적용할 수 있다.

### 🌱 앱 프로텍트 WAF 모듈 설치와 설정 (엔진엑스 플러스)
엔진엑스 플러스를 사용하면 클러스터 레벨으 rate limit 과 자동화된 차단리스트를 적용할 수 있다.