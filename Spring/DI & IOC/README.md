## Spring DI & IOC

> Spring을 공부하거나 면접에서 Spring의 핵심이 뭐냐는 질문에 제일 먼저 생각나는것은 바로 DI & IOC입니다.<br>
> DI & IOC 를 다시 머릿속에 정리하기 위하여 이렇게 정리합니다.

---

## 🌟 DI (Dependency Injection)

`DI(Dependency Injection)`이란 Spring이 제공하는 의존 관계 주입 기능을 의미한다. 객체를 직접 생성하지 않고 외부에서 생성한 후 주입 시켜주는 방식을 의미한다.<br>
`DI`를 사용하였을때 얻는 이점으로는 외부에서 생성한 후 주입하기 때문에 모듈 간의 결합도가 낮아지고 유연성은 높아지는 장점이 있다.

그렇다면 객체를 외부에서 생성하여 주입한다고 하는데 과연 어디서 생성되고 어느시점에 주입되는것일까?

우리는 Spring 을 공부하다보면 `객체`를 `객체` OR `Bean`이라고 부릅니다. 이러한 `Bean`은 프로젝트 실행시
`Bean` 객체의 생성과 소멸에 관한 작업을 자동으로 수행해주는데 이렇게 객체를 생성되는 곳을 `Bean 컨테이너`라고 부른다.

### 📚 Spring 에서의 객체 주입 방법
- ### ☝ Field Injection
  ```java
  // 다음과 같이 의존성을 주입하고자 하는 `Field` 위에 @Autowired 어노테이션을 추가하면됩니다. 
  @RestController
  public class ExamController {
  
    @Autowired
    private ExampleService exampleService;
    ...
  }
  ```

- ### ☝ Setter based Injection
  ```java
  @RestController
  public class ExamController {
    
    private ExampleService exampleService;
  
    // setter 메서드에 @Autowired 어노테이션을 붙여주면 됩니다.
    @Autowired
    public void setExampleService(ExampleService exampleService) {
        this.exampleService = exampleService;
    }
    ...
  }
  ```

- ### ☝ Constructor based Injection
  ```java
  @RestController
  public class ExamController {
    
    private final ExampleService exampleService;
    
    // 생성자를 통하여 의존성을 주입하는 방식 
    public void ExamController(ExampleService exampleService) {
        this.exampleService = exampleService;
    }
    ...
  }
  ```

- ### ☝ 예외 Lombok Library 를 사용할 경우
  ```java
  @RestController
  @requiredargsconstructor
  public class ExamController {
    private final ExampleService exampleService;
    ...
  }
  ```
  
---

## 🌟 IOC (Inversion Of Control)

`Spring`의 핵심에서 `DI`와 함께 나오는 개념은 바로 `IOC`입니다.<br>
제어의 역전이라는 의미로 불리우며, 의미 그대로 메소드나 객체의 호출 작업을 개발자가 결정하는 것이 아닌 , 외부에서 결정되는것을 의미한다.

Spring IOC를 통하여 의존성을 역전시켜 객체 간의 결합도를 줄이고, 가동성 및 유지보수를 편하게 할 수 있다.

> 간단하게 생각하면 사용자가 컨트롤하는 것이 아니라 스프링에게 전적으로 작업을 맡긴다고 보면될듯합니다.

흔히 우리가 Java 프로그래밍시 객체를 생성하는 방법은 다음과 같았습니다.<br>

> 객체 생성 -> 의존성 객체 생성(클래스 내부) -> 의존성 객체 메소드 호출  

하지만 Spring IOC가 있다면 다음과 같은 방식으로 객체가 생성되고 실행됩니다.
> 객체 생성 -> 의존성 객체 주입(Spring Container에서 만들어놓은 객체 주입) -> 의존성 객체 메소드 호출




