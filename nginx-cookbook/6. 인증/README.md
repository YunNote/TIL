
## 인증

> 엔진엑스에서는 클라이언트에 대한 인증을 수행할 수 있다. <br>
> 클라이언트 요청을 엔진엑스가 인증함으로써 업스트림 서버에서 인증을 처리하며 발생하는 부하를 줄이고 
> 동시에 인증받지 못한 요청은 서버까지 도달하는것을 막을 수 있다.
> 
> 엔진엑스의 오픈 소스 버전에서는 `HTTP 기본인증`과 `하위 요청`을 통한 인증이 있다.<br>
> 엔진엑스플러스에서는 JWT 검증 모듈을 사용 가능.

----------

### 🌱 HTTP 기본 인증

HTTP 기본인증을 사용하는 방법은 다음과 같다.

```shell
# /etc/nginx/conf.d/passwd
username:password
username:password
```
위와 같은 형식으로 첫번째 필드에는 사용자의 이름, 두번째 필드에서는 비밀번호를 설정한다.

openssl 모듈을 이용하여 비밀번호를 암호화합니다.
```shell
openssl passwd 1q2w3e4r
# $1$Mrfqptx4$YYI92mjtti3/rIWY6NR3z1 - 암호화된 비밀번호
```

해당 파일을 passwd에 등록한다.

```shell
# /etc/nginx/conf.d/passwd
user:$1$Mrfqptx4$YYI92mjtti3/rIWY6NR3z1
```

nginx 설정 파일에 해당 passwd 파일을 추가한다.
```shell
# /etc/nginx/conf.d/default.conf

location / {
  auth_basic    "Private site";
  auth_basic_user_file /etc/nginx/conf.d/passwd;
}
```

```shell
# 성공
# 성공시점 localhost 를 불러오는 network를 확인하면 Authorization에 인증토큰이 넘어가는것을 확인할 수 있다. 
$ curl --user user:1q2w3e4r http://localhost

# Response
<!DOCTYPE html>
<html>
   <head>
      <title>Welcome to nginx!</title>
      <style>
         html { color-scheme: light dark; }
         body { width: 35em; margin: 0 auto;
         font-family: Tahoma, Verdana, Arial, sans-serif; }
      </style>
   </head>
   <body>
      <h1>Welcome to nginx!</h1>
      <p>If you see this page, the nginx web server is successfully installed and
         working. Further configuration is required.
      </p>
      <p>For online documentation and support please refer to
         <a href="http://nginx.org/">nginx.org</a>.<br/>
         Commercial support is available at
         <a href="http://nginx.com/">nginx.com</a>.
      </p>
      <p><em>Thank you for using nginx.</em></p>
   </body>
</html>



# 실패
$ curl --user user:1q2w3e4r!! http://localhost

#Response
<html>
   <head>
      <title>401 Authorization Required</title>
   </head>
   <body>
      <center>
         <h1>401 Authorization Required</h1>
      </center>
      <hr>
      <center>nginx/1.22.1</center>
   </body>
</html>

```

----------

### 🌱 인증을 위한 하위 요청 

요청된 리소스에 대해 응답하기 전에 http_auth_request_module를 사용하여 인증서비스로
요청을 보내고 요청자의 ID를 확인한다, 하위 요청으로 보내기 전에 내부 인증 서버로 보내서 요청을 처리하도록 한다.

----------

### 🌱 JWT 검증하기 (엔진엑스 플러스)

엔진엑스 플러스에서 제공하는 JWT 인증 모듈을 사용하여 토큰의 시그니처를 검증하고 속성 정보와 헤더를
엔진엑스의 변수로 가져 올 수 있다.


```shell
location /api/ {
  auth_jet    "api";
  auth_jwt_key_file     conf/keys.json
}
```

`/api/**`요청에 대해서 jwt 인증이 되어야 함을 지정한다.<br>
`auth_jet_key_file` 지시문은 nginx plus에 JWT의 서명요소를 확인하는 방법을 알려주며, 표준 JWK(Json Web Key)형식으로
만들어진 키 파일의 경로를 의미한다.

----------

엔진엑스 플러스와 관련된 내용은 생략하였습니다.
