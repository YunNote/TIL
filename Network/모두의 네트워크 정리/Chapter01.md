> 네트워크 지식이 완벽하지 않은것 같아 간단하게 공부해볼만한 책을 찾다가 <br> 
> [모두의 네트워크 10일만에 배우는 네트워크](http://www.yes24.com/Product/Goods/61794014) 라는 책을 발견하곤 Yes24를 통해 ebook으로 구매하였습니다.<br>
> 간단하게 정리하기에 앞서 읽어보니 지루하지 않게 예제도 잘나와있고 빠르게 보기 좋은내용 같습니다. <br>
> 해당 README에서는 간단하게 먼저 읽어보고 또 다른 책으로 내용을 보충하겠습니다 .

---

## 😊 컴퓨터 네트워크
> 전송 매체를 매개로 연결되어 서로 데이터를 주고 받는 시스템의 모음
>

<br>

---

<br>

## 😊 패킷 (Packet)
> 브라우저에는 사진과 문자를 보여주기 위한 <strong>규칙</strong> 가 존재한다.<br>
> 이러한 규칙을 `패킷`이라고 부른다. `패킷`은 컴퓨터 간에 데이터를 주고받을 때 네트워크를 통해 전송되는 데이터의 작은 조각을 말한다.
> ```큰 데이터가 있어도 작게 나눠서 보내는것이 규칙이다.```

그렇다면 큰 데이터를 그냥 한번에 보내면 되는것을 왜 굳이 작게 나눠서 데이터를 전송하는것일까요 .<br>
먼저 `대역폭`부터 알아야 합니다.

> 대역폭 (bandwidth) 
> ```text
> 대역폭이란 네트워크에서 이용 가능한 최대 전송 속도로 전보를 전송할 수 있는 단위 시간당 전송량을 말한다.
> ```

만약 대역폭을 생각하지 않고 전송하게 된다면, 해당 내용이 네트워크 대역폭을 너무 많이 점유해서 다른 패킷의 흐름을 막아 속도가 정체될 수 있다.

하나의 예를 들어보겠습니다.<br>
하나의 사진을 네트워크로 전송하기위해 작게 조각내었다. 그렇다면 해당 데이터를 받는쪽에서는 어떻게 작은 조각들을 가지고 하나의 원본 사진을 만들수 있을까 ??<br>
실제로 데이터가 누락되었을수도 있고, 해당 패킷전송때 네트워크가 지연되어 늦게 도착하거나 할 수도 있습니다.

이러한 상황때문에 송신 측에서 수신 측으로 패킷을 보낼 때는 각 패킷에 순서를 부여하여 전송합니다. <br>
이렇게 되면 번호에 맞춰 정렬하면 되니 늦게 도착한 패킷도 원래의 위치로 돌아갈 수 있다.

<img src="imagesacket.jpeg" alt="" width="450" />

---


## 😊 Bit 와 Byte
> `bit` - 컴퓨터에서 사용 하는 가장 작은 단위, 2진수 0 or 1로 표현된다
>
> `byte` -  1Byte 는 8bit로 이루어져있다. 컴퓨터는 기본적으로 바이트 단위로 데이터를 읽고 쓰는 작업을 한다.

<br>

---

## 😊 LAN과 WAN
네트워크는 접속할 수 있는 범위에 따라 두가지 종류로 나뉜다.<br>
바로 위에 나온 LAN 과 WAN 입니다. <br>

> ### LAN
> ```text
> Local Area Network(근거리 통신망)을 의미하며 좁은 범위의 네트워크에서 사용된다.<br>
> 사무실이나 가정과 같이 지리적으로 제한된 공간.
> ``` 

> ### WAN
> ```text 
> Wide Area Network(광역 통신망)을 의미하며 넓은 범위의 네트워크에서 사용한다.<br>
> WAN은 ISP가 제공하는 서비스를 사용하여 구축된 네트워크를 의미한다.<br>
> ```

WAN 은 LAN 과 LAN을 연결하는 것으로도 생각해도 된다. 이러한 작업은 ISP 가 LAN과 LAN사이에서 서비스를 제공한다.
> ### ISP
>  ```text
>  Internet Service Provider의 약자로 우리가 흔히 알고있는 KT, U+, SK 브로드 밴드와 같은 사업자를 의미한다.
> ```

---

## 😊 LAN 과 WAN 의 차이는 ?
LAN 같은 경우는 연결하는 거리가 짧은 만큼 `속도가 빠르며 신호가 약해지거나 오류가 발생할 확률이 적다` 그와 반대로 WAN같은 경우에는
멀리 있는 LAN과 LAN의 연결이기 때문에 `속도가 LAN에비해 느리며 신호가 약해지거나 오류가 발생할 확률이 더 높다.`

---

## 😊 용어 정리 
> #### 네트워크 (network) <br>
> `컴퓨터를 두 대 이상 연결하여 서로 데이터를 전송할 수 있는 통신망을 의미`

> #### 인터넷(Internet) <br>
> `TCP/IP 프로토콜을 사용하는 세계 최대 규모의 네트워크, 전 세계의 컴퓨터를 서로 연결하여 정보를 교환할 수 있도록 만든 하나의 거대한 컴퓨터 통신망이다.`

> #### 패킷 (Packet) <br>
> `네트워크 통신을 할 때 사용되는 작게 분할된 데이터 조각으로 네트워크에서 사용하는 데이터의 기본 단위`

> #### 비트 (bit) <br>
> `정보의 최소 단위로 0 or 1을 의미`

> #### 바이트 (byte) <br>
> `컴퓨터의 정보량 단위로 8bit를 1byte 로 표기 할 수 있다.`

> #### 랜(LAN, Local Area Network) 과 왠(WAN, Wide Area Network)
> - LAN : `가까운 거리에 위치한 장치들을 서로 연결한 네트워크를 의미, 주로 집, 사무실, 건물등 가까운 지역을 연결하는 네트워크를 의미`
> - WAN : `LAN을 하나로 묶는 거대한 네트워크이다. 특정 도시, 국가, 대륙과 같이 넓은 범위를 연결하는 네티워크를 말한다. 넓은 지역에 설치된 컴퓨터들 간의 정보와 자원을 공유하기에 적합하도록 설계한 컴퓨터 통신이다.`

> #### 인터넷 서비스 제공자 (Internet Service Provider, ISP)
> `인터넷에 접속하는 수단을 제공해주는 주체를 의미, 일반 사용자, 기업체, 기관, 단체등 인터넷에 접속하여 인터넷에 접속하여 인터넷을 이용할 수 있도록 돕는 사업자.
> 우리가 흔히 알고있는 SK브로드밴드, LG U+, KT가 ISP인터넷 서비스를 제공한다.`

> #### 서버(Server)
> `컴퓨터 네트워크에서 다른 컴퓨터에 서비스를 제공하기 위한 컴퓨터 또는 프로그램`

> #### DMZ(DeMilitarized Zone)
> `네트워크 구성중에서 일반적으로 인터넷인 외부 네트워크와 내부 네트워크 사이에 위치한 중간 지대를 말한다.
> 네트워크의 보안 영역으로, 외부 공격자가 내부 네트워크에 침투하는것을 막는 역할을 한다.`