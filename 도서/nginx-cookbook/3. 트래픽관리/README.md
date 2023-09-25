
## 트래픽 관리

엔진엑스와 엔진엑스 플러스는 웹 트래픽 컨트롤러로도 분류 된다.

해당 트래픽관리 장에서는  사용자 요청을 비율로 분기, 사용자의 위치를 활용하여 흐름 조절, 요청빈도 , 연결수, 대역폭 등을 제한해 트래픽을 제어하는 방법을 알아본다.

### 🌱 A/B 테스트 

> A/B 테스트는 두 가지 다른 버전의 웹사이트, 앱, 또는 마케팅 캠페인 등을 동시에 실행하여 어떤 버전이 더 효과적인지를 비교하는 실험적인 방법입니다. 이를 통해 사용자들의 반응을 분석하고 최적의 결과를 얻을 수 있습니다.

기본적인 A/B 테스트에 대한 설명입니다.

nginx에서는 `split_clients` 모듈을 사용하면 해당 작업이 가능하다.

```shell
split_client "${remote_addr}AAA" $variant {
  20.0% "backendv2";
  *     "backendv1";
}
```

split_client 지시자는 첫 번째 매개변수에 지정된 문자열(${remote_addr}AAA)을 활용해 해시를 생성한다.

지정된 비율에 따라 두번째 매개변수에 지정된 변수에 값을 할당한다.

두번째 매개변수는 세번째 매개변수인 $variant 매개변수에 지정된 분기 비율에 따라 특정 값을 저장한다.
즉 $variant 변수는 요청의 20%에 대해서는 backendv2가 할당되고 나머지 80%에 대해서는 backendv1이 할당된다.

```shell
location / {
  proxy_pass http://$variant
}
```

nginx 로 수신된 트래픽은 $variant 변수를 사용해 두개의 애플리케이션 서버풀로 분기된다.

A/B 테스트 배포시에는 주로 카나리 배포가 널리 사용되나 일반적으로는 블루-그린 배포방식이 사용된다.

 - 카나리 배포 : 변경사항을 모든 서비스에 한번에 적용하지 않고 일부 서버에만 적용해서 실서비스 환경의 트래픽을 이용해 문제가 있는지 확인하는 방식
 - 블루-그린 배포 방식 : 한번에 새로운 애플리케이션을 사용하도록 분기하되 새 버전에 문제가 없다고 확인될 때까지 기존 버전을 유지한다.

----------

### 🌱 GeoIP 모듈과 데이터베이스 활용하기 (Geolocation과 IP 합성어)
 GeoIP 국기 및 도시 데이터베이스를 통해 IP를 통한 위치 정보를 사용가능한듯 ..

----------

### 🌱 국가 단위 접근 차단하기

```shell
load_module "ngx_http_geoip_module.so 파일 경로"

http {
  map $geoip_country_code $country_access {
    "US"    0;
    default 1;
  }
}
```
위 설정의 map 지시자는 $country_access 변수에 1 or 0을 할당한다, 사용자 접속 주소 IP가 US일 경우 0을 할당
기외의 국가라면 1을 할당.

추가로 다음과 같이 server 블록에 if 문을 작성하여 차단가능

```shell
server {
  if($country_access = '1') {
    return 403
  }
}
```

이와 같이 if 문과 코드를 사용하면 리소스에 대한 접근을 차단할 ㅅ ㅜ있다.


----------

### 🌱 실제 사용자 IP 찾기

geoip_proxy 지시자로 프록시 서버 IP대역을 정의하고 geoip_proxy_recursive 지시자로 사용자의 원래 IP 주소 확인 가능.

```shell
load_module "ngx_http_geoip_module.so 파일 경로"

http {
 geoip_country GeoIp.dat 경로;
 geoip_city GeoLiteCity.dat 경로;
 geoip_proxy 프록시서버 IP 대역;
 geoip_proxy_recursive on; 
}
```

geoip_proxy 지시자에 CIDR표기법으로 프록시 서버의 IP대역을 지정하고 x-forwarded-for 헤더 값을 활용하여
실제 사용자 IP를 찾도록 한다. `geoip_proxy_recursive`지시자를 사용하면 엔진엑스는 x-forwarded-for 헤더값을
순차적으로 탐색해 최종 사용자의 IP를 확인한다.

`x-forwarded-for 헤더는 표준에 정의된 헤더는 아니지만 여러 프록시 서버등에서 광범위하게 사용됨 `


---------

### 🌱 연결 제한하기

limit_conn 지시자를 사용해 연결수를 제한한다.

```shell
http{
  
  limit_conn_zone $binary_remote_addr zone=limitbyaddr: 10m
  limit_conn_status 429;
  
  server {
    limit_conn limitbyaddr 40;
  }
}
```

해당 설정을 하면 limitbyaddr 이라는 공유 메모리 영역을 생성하게 된다,

공유 메모리 크기는 10메가 바이트로 설정한다 (zone=limitbyaddr: 10m)
`limit_conn_status`는 지정된 연결수를 초과하면 사용자에게 전달할 HTTP 코드를 지정하며, 429는 너무 많은 요청을 의미한다.

`limit_conn` 과 `limit_conn_status`지시자는 http, server, location 컨텍스트에서 사용 가능.


---------

### 🌱 요청 빈도 제한하기

빈도 제한 모듈을 사용하여 요청 빈도를 제한 한다.

```shell
http {
  limit_req_zone $binary_remote_addr zone=limitbyaddr: 10m rate=3r/s;
  limit_req_status 429;
  
  server {
    limit_req zone=limitbyaddr
  }
}
```

위에 나온 연결제한하기와 마찬가지로 limitbyaddr 공유 메모리 영역을 생성하고 10메가 바이트로 설정한다.

지정 빈도를 초과하는 요청에 대해서는 limit_req_status 429 응답코드를 내려준다. 만약 해당 limit_req_status를
지정하지 않는다면 기본값은 503 이 반환된다.

```shell
server {
  location / {
    limit_req zone=limitbyaddr burst=12 delay=9;
  }
}
```

burst 매개변수를 사용하면 빈도가 지정된 값보다 낮으면 차단하지 않고 허용하도록 설정한다. delay 값보다 큰 요청에 대해서는
지정된 rate에 맞춰 지연처리를 한다.

위의 내용에 대해서는 사용자가 요청을 초당 9개까지만 지연없이 전송할 수 있으며 초과된 3개에 대해서는
쓰로틀링돼 지연처리가 된다.

---------

### 🌱 전송 대역폭 제한하기

전송 대역폭은 `limit_rate`와 `limit_rate_after`지시자를 사용하여 응답 대역폭 제한 가능.

```shell
location /download/ {
  limit_rate_after 10m;
  limit_rate 1m;
}
```

위 location 블록에 설정을 함으로써 /download/ 로 시작하는 URI에 대해서 누적 전송량이 10메가바이트를 초과하면 초당 1메가바이트를 
넘지 않도록 제한한다. 대역폭 제한은 개별연결에 적용되는 설정이므로 연결 수와 함께 전송 대역폭을 제한할 필요가 있다.
