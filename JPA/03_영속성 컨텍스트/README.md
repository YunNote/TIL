## 😊 EntityManagerFactory, EntityManager

---

`EntityManagerFactory`는 `EntityManager`를 만들어주는 공장같은 일을 한다. 
이러한 `EntityManagerFactory`을 만드는 비용은 크기 때문에 한개만 만들어서 애플리케이션에서 
공유하도록 설계가 되어있다고 한다.


`EntityManager`는 Entity를 저장하고, 수정, 삭제등 엔티티와 관련된 일을 처리하게 도와준다.
이러한 `EntityManager`는 `EntityManagerFactory`를 통해 생성이 된다. `EntityManager`를 만드는 비용은
크지 않다. 

주의해야할 점은 `EntityManagerFactory`는 여러 스레드가 동시에 접근해도 안전하기 때문에 다른 스레드에서
공유하여 사용해도 되지만 `EntityManager`는 스레드가 동시에 접근하면 동시성 문제가 발생하기 때문에
스레드 간에 공유를 하지 않는것이 좋다.

> EntityManager는 Database의 연결이 꼭 필요한 시점까지 커넥션을 얻지 않는다.<br> 
> EntityManager는 Transaction을 시작할 때 커넥션을 사용한다.
> 

---

## ⭐ 영속성 컨텍스트 (Persistence Context)

>개인적으로 JPA 에서 제일 중요한 용어 및 개념이라고 생각합니다

영속성 컨텍스트를 해석하면 `Entity를 영구 저장하는 환경`이라는 의미를 가집니다.

Entity Manager를 통하여 Entity를 저장 or 수정을 하면 해당 Entity Manager 는 영속성 컨텍스트에 Entity를 보관하고 관리하게 됩니다.

```java
// 단순히 저장하는것이 아닌, EntityManager를 통해 Member Entity를 영속성 컨텍스트에 저장한다는 의미.
em.persist(member);
```

---

## 😊 Entity의 생명 주기 
