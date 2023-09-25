
## 대규모 확장 가능한 콘텐츠 캐싱

### 🌱 캐싱

> 캐싱이란 반복된 요청에 대해서 응답을 저장해뒀다가 빠르게 콘텐츠를 제공하는 방법이다.<br>
> 업스트림서버가 동일한 요청에 대해서 계산이나 질의를 다시 수행하지 않도록 전체 응답을 저장함으로 업스트림 서버의 부하를 낮춘다.
>   
> nginx를 사용하면 nginx서버가 배치된 모든 곳에 콘텐츠를 캐시할 수 있어서 자신만의 CDN을 만들 수 있다.<br>
> nginx캐싱은 수동적으로 콘텐츠를 캐싱할 뿐만 아니라 업스트림 서버에 문제가 생기면 캐싱된 응답으로 사용자에게 콘텐츠를 제공 할 수 있다.
> 
> 다만 캐싱 기능은 http컨텍스트 내에서만 사용가능하다.

----------

### 🌱 캐싱 영역

```shell
proxy_cache_path /var/nginx/cache
    keys_zone=CACHE:60m
    levels=1:2
    inactive=3h
    max_size=20g;
proxy_cache CACHE;
```

`proxy_cache_path` : 공유 메모리 캐시영역 정의 키워드 <br> 
`/var/nginx/cache` : 캐시 응답을 저장하기 위해 /var/nginx/cache 디렉터리 생성 후 메모리에 CACHE라는 공유 메모리 영역을 60메가바이트 크기로 생성.<br>
`levels=1:2` : 디렉터리 구조의 레벨을 지정한다. (1:2로 지정하면 /var/nginx/cache/ 영역 기준으로 1글자/2글자 형태로 저장된다 [ex] : /var/nginx/cache/c/29/xxxxxxx)<br>
`inactive:3h` : 3시간동안 응답에 대해서 동일한 요청이 오지 않는다면 해당 캐시를 비활성화 한다.<br>
`max_size`: 캐시영역의 크기가 20기가 바이트를 넘지않도록 지정한다.

`proxy_cache_path`는 http 컨텍스트에서만 유효하며 `proxy_cache` 지시자는 http, server, location 컨텍스트에서 사용 가능하다.

----------

### 🌱 캐시 락

`proxy_cache_lock` 지시자는 동일한 리소스에 대한 요청이 여러개가 들어와도 한번에 하나의 요청을 통해서만 캐시가 만들어지도록 한다.<br>
첫번째 요청을통한 캐시가 생성되는동안에는 기존의 요청에 대해서는 처리되지 않고 기다린다.<br>

```shell
proxy_cache_lock on;
proxy_cache_lock_age 10s;
proxy_cache_lock_timeout 3s;
```

`proxy_cache_lock` : 생성 중인 캐시에 대해 동일한 요청이 들어와도 nginx 가 요청을 처리하지 않고 캐시 생성이 완료될 때까지 기다린다.<br>
`proxy_cache_lock_age` : 지정된 시간 (10s)내에 캐시가 생성되야하며, 해당 시간이 초과되면 대기중인 다른 요청을 업스트림 서버로 보내 응답 결과 캐시를 다시 시도한다(default: 5s)<br>
`proxy_cache_lock_timeout` : 지정된 시간내에 캐시생성이 완료되지 못하면 다른 요청을 업스트름 서버로 보내 필요한 콘텐츠를 가져오게 하되, 캐시를 생성하지는 않는다.

얼핏보면 `proxy_cache_lock_age` 와 `proxy_cache_lock_timeout`이 비슷해 보이지만 다음과 같이 보면 다르다 .

`proxy_cache_lock_age`는 캐시 생성이 너무 오래걸리니 내가 대신 만들어줄께에 대한 요청이라면 `proxy_cache_lock_timeout`은 
너무 오래걸리니 필요한 콘텐츠 업스트림 서버에서 가져올테니까 너는 계속 캐시를 생성해라는 의미로 이해하면 쉽다.

----------

### 🌱 해시 키 값 캐시 

```shell
proxy_cache_key "$host$request_uri $cookie_user";
```

`proxy_cache_key` 지시자 뒤에 다음과 같이 작성하면 요청된 페이지를 캐시로 저장할 때, 
호스트명, URI, 쿠키값을 통해서 사용자마다 서로 다른 해시를 생성하여 캐시 키로 사용하도록 한다. 
이를 통해  동적인 페이지를 캐시하지만 다른 사용자의 콘텐츠가 잘못 전달되지 않도록 할 수 있다.

`proxy_cache_key`의 기본 값은 "$scheme$proxy_host$request_uri"이며 일반적으로 무난하게 사용 가능하다.
$scheme는 http or https 가 될것이며 $proxy_host는 업스트림의 호스트를 , $request_uri는 요청의 세부 경로를 나타낸더.

이 외에도 애플리케이션에 대한 요청을 구분하기 위한 쿼리스트링, 헤더, 세션 식별자등 여러 요소가 있으며 해당 값들을 활용한다면
다양한 해시키를 직접 구성 가능.

`proxy_cache_key`는 http, server, location 블록 컨텍스트에서 사용할 수 있으며 사용자 요청을 어떻게 캐시할지 유연하게 제어하도록 해준다. 


----------

### 🌱 캐시 우회

`proxy_cache_bypass` 지시자를 비어있지 않은 값이나 0이 아닌 값으로 지정하면 캐시를 우회한다.
대표적인 방법으로 캐시하고 싶지 않은 location 블록 내에서 지시자의 매개변수로 사용된 특정 변숫값을 빈문자열이나 0이 아닌 어떤값으로 설정한다.

```shell
# cahe-bypass라는 http 요청 헤더값이 0이 아닐 때 nginx가 캐시를 우회하도록 한다.
# cache를 우회할지 판단하기 위해 특정 헤더값을 변수로 사용하며 
# 사용자는 캐시 우회가 필요하면 이 헤더를 요청에 포함하면된다.
proxy_cache_bypass $http_cache_bypass;
```

캐시를 우회하려고하는 이유는 다양하며 트러블슈팅과 디버깅이 대표적이다, 캐시된 페이지가 계속 응답되거나 사용자를 특정하도록
설정된 캐시 키를 사용하면 문제 상황을 재현하기가 어렵다, 따라서 캐시를 그대로 두고 업스트림 서버로 우회할
방법을 확보하는것이 좋다, location블록과 같이 주어진 컨텍스트 내에서 proxy_cache 지시자를 off 로 설정하면
캐시기능을 완전히 끌 수 있기 때문에 해당 방법도 좋은 선택이 된다.

----------

### 🌱 캐시 성능

```shell
location ~* \.(css|js)$ {
  expire 1y;
  add_header Cache-Control "public";
}
```

위와 같이 캐시를 설정하게 되면 , css 와 js 파일을 캐시하도록 명시하게 된다.<br>
캐시 기간은 1년으로 지정하였으며,. Cache-Control 헤더를 추가하며 public으로 지정함으로써 콘텐츠가 전달되는 중간에
위치한 어떤 캐시 서버라도 리소스를 캐시할 수 있도록 한다, private 으로 설정하면 실제 사용자 환경에만 리소스를 캐시한다.


----------

### 🌱 캐시 퍼지 (엔진엑스 플러스)

엔진엑스플러스에서 제공하는 퍼지 기는을 사용하고 `proxy_cache_purge` 지시자에 비어있지 않은 값이나 0이 아닌 값을 할당한다. 

```shell
map $request_method $purge_method {
  PURGE 1;
  default 0;
}

server {
  ...
  location / {
    ...
    proxy_cache_purge $purge_method;
  }  
}
```
해당 예시는 HTTP 요청 메서드가 `PURGE`라면 요청된 리소스에 대한 캐시를 퍼지한다. 

----------

### 🌱 캐시 분할 

nginx의 slice 지시자와 내장 변수를 사용하면 캐시 결과를 작은 조각으로 나눌 수 있다.

```shell
proxy_cache_path /tmp/mycache keys_zone=mycache:10m;

server {
  #...
  proxy_cache mycache;
  slice 1m;
  proxy_cache_key $host$uri$is_args$slice_range;
  proxy_set_header Range $slice_range;
  proxy_http_version 1.1;
  proxy_cache_valid 200 206 1h;
  
  location / {
    proxy_pass http://origin:80;
  }
}
```

`slice` :지정자를 사용하여 사이즈를 정해주면 해당 사이즈만큼 파일 조각으로 나눈다(위의 예제는 1m 1메가바이트)<br>
`proxy_cache_key`: 지시자에 지정된 규칙에 따라 저장된다.<br>
`proxy_set_header`지시자를 사용하여 원본 서버로요청을 보낼때 Range 헤더를 추가하고 헤더값으로 $slice_range 변수값을 사용한다.

다만 HTTP 1.1 버전부터 지원되는 기능이므로 proxy_http_version 지시자를 사용해 프로토콜 버전을 업그레이드 해야한다.
캐시가 200, 206응답에 한해 1시간동안 유효하도록 proxy_cache_valid 지시자를 사용하여 이후에 location 블록과 원번 서버를 정의한다.