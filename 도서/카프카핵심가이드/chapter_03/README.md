# 3. 카프카 프로듀서: 카프카에 메시지 쓰기

---
## 프로듀서 개요 

서로 다른 요구 조건을 필요로 하는 경우 카르카가 메시지를 쓰기 위해 프로듀서 API를 사용하는 방식에 영향을 미치게 된다.

프로듀서 API는 매우 단순하지만, 데이터를 전송할때 내부적으로는 조금 더 많은 작업들이 이루어 진다.

프로듀서 API는 단순하지만 우리가 데이터를 전송할 때 내부적으로는 조금 더 많은 작업들이 이루어진다.


![img.png](img.png)

### 1. ProducerRecord 객체를 생성한다.

> 레코드가 저장될 토픽과 벨류를 필수로 지정하며, 파티션과 키는 선택사항이다. ProducerRecord를 전송하는 API를 호출하였을때
> 프로듀서는 키와 값 네트워크를 통해 전송될 수 있도록 직렬화하여 바이트 배열로 변환하는 과정이다.


### 2. 파티셔너에게 데이터를 전송.
> 파티션을 명시적으로 지정하지 않았다면 해당 데이터를 파티셔너에게로 보낸다음 파티셔너를 통해 파티션을 결정한다. 보통 
> 파티셔너에서는 ProducerRecord 객체의 키값으로 결정한다.
> 
> 파티션이 결정되어 메시지가 전송될 토픽과 파티션이 확정되면 프로듀서는 레코드를 같은 토픽 파티셔너로 전송될 케도드들을 모은 
> 레코드 배치에 추가한다.
> 
> 그러면 별도의 스레드가 해당 레코드 배치를 적절한 브로커에게 전송한다.


### 3. 브로커에서 메시지 처리
> 브로커가 메시지를 받으면 응답을 돌려줘야 한다.
> 
> 성공적으로 저장되었을 경우 토픽, 파티션, 파티션 안에서의 레코드의 오프셋을 담은 RecordMetadata를 리턴한다.
>
> 
> 만약 실패하였을 경우에는 에러가 반환되며, 프로듀서가 에러를 수신하였을 경우 몇번더 재시도 한다.

---

## 카프카 프로듀서 생성하기

카프카 메시지를 쓰려면 원하는 속성을 지정하여 프로듀서 객체를 생성해야 한다. 카프카는 해당 아래 3가지의 값을 필수로 갖는다.

### 🔥 bootstrap.servers

카프카 클러스와 첫 연결을 생성하기 위해 사용할 브로커의 host:port 목록을 의미한다.
다만 해당 값에 모든 브로커들이 명시될 필요는 없다. 왜냐하면 첫번째 연결을 생성한뒤 추가 정보를 받아오게
되어있기 때문이다. 다만 브로커중 갑자기 장애가 발생할 수 있기 때문에 프로듀서가 클러스터에 연결할 수 있도록
최소 2개 이상을 지정할것을 권장하긴한다.


### 🔥 key.serializer

카프카에 쓰기 위한 레코드를 직렬하기 위해서 사용하게될 시리얼라이저 클래스의 이름을 지정하기 위해 사용한다.

브로커는 메시지의 키값, 밸류값의 바이트 배열을 전달받는다. 하지만 애플리케이션마다 전송 방법이 다르기 때문에
임의의 애플리케이션에서 객체를 전송할 수 있도록 매개변수화된 타입을 제공하도록 지원한다.

해당 옵션을 사용하면 가독성 높은 코드를 작성할 수 있지만, 프로듀서입장에서는 해당 객체를
어떻게 바이트배열로 변경해야하는지 알아야한다.

`key.serializer` 옵션에는 org.apache.kafka.common.serialization.Serializer인터페이스를
구현하는 클래스의 이름이 지정되어야 한다.  

카프카 Client 는 `ByteArraySerializer`, `StringSerializer`, `IntegerSerializer`등등이 포함되어 있어
자주 사용하는 타입을 사용하고 싶은경우 직접구현할 필요없이 있는것읅 가져다 쓰면된다.

### 🔥 value.serializer

카프카에 쓸 레코드의 밸류값을 직렬하기 위한 시리얼라이저 클래스의 이름을 지정한다.

---


## 직접 Producer 구현 및 테스트 

#### <i>해당 예제는 Java 기준입니다.</i>

```groovy
// Kafka Gradle 추가
// https://mvnrepository.com/artifact/org.springframework.kafka/spring-kafka
implementation 'org.springframework.kafka:spring-kafka:3.0.11'
```

```java
public static void main(String[] args) {
   
  // 1. Properties 객체 생성 
  // 2. Properties 에 필수 설정 값 세팅  
  Properties configs = new Properties();
  configs.put("bootstrap.servers", "localhost:9092"); // kafka host 및 server 설정
  configs.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");   // serialize 설정
  configs.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");

  /**
   * bootstrap.servers => AdminClientConfig.BOOTSTRAP_SERVERS_CONFIG
   * key.serializer => ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG
   * value.serializer => ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG
   * 오타에 취약하기 때문에 2.x부터는 카프카 클래스에 정의된 상수 사용 가능.
   */
  
  
  // 3. KafkaProducer 객체 생성시 config 를 전달하여 프로듀서 생성 .
  KafkaProducer<String, String> producer = new KafkaProducer<String, String>(configs);
  producer.send(new ProducerRecord<>("test", "WORLD"));

  producer.flush();
  producer.close();
}
```

만약 필수값을 넣지 않는다면 아래와 같은 에러가 발생 

![img_1.png](img_1.png)



---

## 메시지를 전송하는 방법 

### 1. 파이어 앤 포켓

메시지를 전송만하고 성공,실패에 대해서는 신경쓰지 않는다. 대부분의 메시지는 정상적으로 전송되겠지만
재시도를 할 수 없는 에러가 발생하거나 타임아웃이 발생할 경우 메시지가 유실되며, 애플리케이션은 아무런 정보나
예외를 전달 받을 수 없다.


### 2. 동기적 전송

카프카 프로듀서는 언제나 비동기적으로 동작한다. send()를 통해 보내면 Future 객체를 반환한다.

동기적으로 처리하기위해서는 .get()메소드를 호출하여 작업이 완료될때까지 기다려 성공여부를 확인해야한다.

![img_2.png](img_2.png)

실제 전송 후 .get()을 반환한 데이터를 보면 아래와 같은 결과를 받을 수 있다.

![img_3.png](img_3.png)

### 3. 비동기적 전송

콜백 함수와 함께 send() 메서드를 호출하면 브로커로부터 응답을 받는 시점에서 자동으로 콜백함수가 실행된다.

---


## 카프카로 메시지 전달하기 

1. 메시지를 전송하기 위해서는 먼저 `ProducerRecord`를 만드는 것부터 시작한다.
2. `ProducerRecord`가 생성되었따면 전송하기 위해서 send() 메서드를 사용한다.
3. send()를 사용하면 메시지는 버퍼에 저장되었다가 별도의 스레드에 의해서 브로커로 보내진다. RecordMetadata를 포함한 자바 Future 객체를 반환하지만 리턴값을 무시하기 때문에 성공 여부를 알 방법은 없다.
    일러한 방법은 누락되어도 상관없는경우에만 사용하라..
4. 메시지를 보내기전에 에러가 발생하는 상황이 있는데. 
   1. `SerializationException` - 메시지의 직렬화 실패
   2. `TimeoutException` - 버퍼가 가득 찰 경우 
   3. `InterruptException` - 전송 작업을 실행하는 중 스레드에 인터럽트가 걸리는 경우

---

### 동기적으로 메시지 전송하기

동기적으로 메세지를 보내는 법은 단순하며, 브로커가 쓰기 요청에 에러 응답을 하거나, 재전송 횟수가 소진 되었을때 발생하는
예외를 처리할 수 있다.

동기적으로 하였을때 에러가 밸생하는 경우는 대게 성능과 관련이 있다. 카프카 클러스터에 작업이 많이 몰리게 된다면
최소 2ms 에서 최대 몇초까지도 지연이 될 수 있다. 

따라서 동기적으로 전송하게 된다면 해당 시간동안 아무것도 하지 않고 기다리게 된다. 성능이 낮아질뿐만 아니라 그시간동안에
아무런 메시지를 전송할 수도 없어 실제 애플리케이션에서는 잘 사용되지는 않는다. 

```java
...
try {
   // 정상 호출 되었을 경우 RecordMetadata 객체를 반환한다.   
   producer.send(producerRecord).get();
}catch (Exception e) {
   // 여기서 처리 ~
   e.printStackTrace();   
}   

```

KafkaProducer에서는 두 종류에 에러가있다. 

1. 재시도가 가능한 에러 
   > 브로커에 문제가 발생하여 다른 파티션에 새 리더가 선출되어 메타데이터가 업데이트 되면 재시도를 통해 해결 가능
2. 재시도가 불가능한 에러 
   > 메시지 크기가 너무 클 경우 재시도 없이 바로 예외를 발생시킨다.

---

### 비동기적으로 메시지 전송하기 

대략 10ms 가 걸리는 하나의 요청에 대해서 메시지를 전송할때 동기적으로 매번 기다리게 된다면 100개의 요청을 처리하는데는
약 1초정도가 걸리게 된다.

메시지를 전부 전송해놓고 응답을 기다리지 않는다면 100개의 메시지를 전송하더라도 시간이 거의 걸리지 않는다.

카프카를 사용하는 대부분의 경우 굳이 응답을 받아서 처리하는 경우는 없을것 이라고 생각하고, 저 또한 그렇게 사용해왔다.

카프카는 레코드를 쓴뒤 레코드의 토픽, 파티션, 오프셋을 반환하지만 대부분의 애플리케이션은 이 값으로 무엇인가를 
하거나 하지는 않았다. 다만 메시지 전송에 완전히 실패하였을 경우에는 내용을 알아야 예외를 발생시키던, 로그를 작성하거나하야
사후 분석을 할 수 있다.

```java
/** 비동기 호출 콜백 */

producer.send(new ProducerRecord<>("test", "WORLD"), (RecordMetadata record, Exception e) -> {
  if(e != null) {
     e.printStackTrace();
  }
});
```

위 코드와 같이 `org.apache.kafka.clients.producer.Callback` 인터페이스를 구현하면 CallBack을 통해 에러를 처리하기 위한 콜백을 지정할 수 있다.

---





