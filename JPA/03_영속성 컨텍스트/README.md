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
