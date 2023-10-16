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

  // 3. KafkaProducer 객체 생성시 config 를 전달하여 프로듀서 생성 .
  KafkaProducer<String, String> producer = new KafkaProducer<String, String>(configs);
  producer.send(new ProducerRecord<>("test", "WORLD"));

  producer.flush();
  producer.close();
}
```

만약 필수값을 넣지 않는다면 아래와 같은 에러가 발생 

![img_1.png](img_1.png)





















