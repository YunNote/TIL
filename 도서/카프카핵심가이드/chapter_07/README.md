# 7. 신뢰성 있는 데이터 전달 

---

카프카는 신뢰성 있는 데이터 전달에 있어서 매우 유연하다.
카프카는 매우 세세한 지점까지도 설정이 가능하도록 개발되었으며, 클라이언트 API 역시 유연하기는 마찬가지이다. 
따라서 신뢰성에 관한 한 모든 종류의 절충점이 가능하다.

다만 매우 유연한만큼 사용자가 사용하다가 실수로 문제를 발생시키기도 쉽다.

다음에 나오는 내용을 미리보면 다음과 같다.

- 서로 다른 종류의 신뢰성 
- 카프카의 복제 메커니즘과 해당 메커니즘이 시스템의 신뢰성에 어떤 영향을 미치는지.
- 활용 사례에 대해서 브로커와 토픽들을 어떻게 설정해야하는지. 
- 서로 다른 환경에서 클아이언트들을 어떻게 사용해야하는지.
- 시스템의 신뢰성을 검증하는 방법 

---

## 신뢰성 보장 

신뢰성 보장에 가장 많이 등장하는 용어는 RDB의 ACID이다

`원자성(atomicity)`, `일관성(consistency)`, `격리성(isolation)`, `지속성(durability)`

어떠한 데이터베이스가 ACID를 준수한다고 한다면 트랜잭션 처리 관리해서 어떠한 행동을 보장한다는 의미가 된다.

신뢰성 있는 애플리케이션을 개발하고자 한다면 카프카가 신뢰성을 어떻게 보장하는지 이해해야 한다. 그래야
실패 상황에서 시스템이 어떻게 작동하는지를 알 수 있기 때문이다.

아파치 카프카는 다음과 같은 내용을 보장한다.

 - 카프카는 파티션의 메시지들 간 순서를 보장한다. 동일한 파티션에서 A다음에 B메시지가 쓰였다면 B의 오프셋이 A보다 큰 것을 보장한다.
 - 클라이언트가 쓴 메시지는 모든 인싱크 레플리카의 파티션에 쓰여진 뒤에야 커밋된 것으로 간주된다. 프로듀서는 완전히 커밋된 다음에 응답이 올지, 리더에게 쓰여진 다음 응답을 올지, 네트워크로 전송된 다음 바로 응답이 올지를 선택가능하다.
 - 커밋된 메시지들은 최소 1개의 작동 가능한 레플리카가 남아있는한 유실되지 않는다.
 - 컨슈머는 커밋된 메시지만 읽을수있다.


위의 내용을 바탕으로 신뢰성을 보장하여 시스템을 구축하기 위해 사용할 수 있지만 트레이드 오프가 있는 법이다. 
따라서 이러한 트레이드 오프를 조절할 수 있ㄷ록 개발자나 운영자가 설정 매개변수를 조절함으로써 어느 정도의 신뢰성이
필요한지를 결정할 수 있도록 개발되었다. ( 신뢰성과 일관성이 우선이냐, 가용성, 높은처리량, 낮은 지연과 같은 고려사항 등 )

---

## 복제

