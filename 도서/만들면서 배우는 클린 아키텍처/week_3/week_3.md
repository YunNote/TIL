#### 해당 정리 내용은 `만들면서 배우는 클린아키텍처`도서를 읽고 정리한 내용입니다.

## 7. 아키텍처 요소 테스트하기

테스트 피라미드는 위에서 부터 `시스템 테스트`, `통합 테스트`, `단위 테스트`로 구성되어있다. <br>
테스트 피라미드에 따르면 비용이 많이 드는 테스트는 지양하고 비용이 적게 드는 테스트를 많이 만들어야 한다.

<b>테스트 케이스</b>의 기본 전제는 만드는 비용이 적고, 유지보수하기 쉽고, 빨리 실행되고, 안정적인 작은 크기의 테스트들에 대해 높은 커버리지를 유지해야 한다는 것이다.

주의해야할 점은 여러개의 단위와 단위를 넘는 경계, 아키텍처 경계, 시스템 경계를 결합하는 테스트는 만드는 비용이 더 비싸지고 실행이 더느려지며 깨지기 더 쉬워진다.

테스트 피라미드는 테스트가 비싸질수록 테스트의 커버리지 목표는 낮게 잡아야 한다는 것을 보여준다, 그렇지 않다면 새로운 기능을 만드는 것보다 테스트를 만드는 데 시간을 더 쓰게 되기 때문이다.

---

#### ✔️ 단위 테스트

> 단위테스트는 피라미드의 토대에 해당된다. 일반적으로 하나의 클래스를 인스턴스화하고 해당 클래스의 인터페이스를 통해
> 기능들을 테스트한다. 만약 테스트중인 클래스가 다른 클래스에 의존한다면 의존되는 클래스들은 인스턴스화하지
> 않고 테스트하는 동안 필요한 작업들을 흉내 내는 목(mock)으로 대체한다.

<br>

#### ✔️ 통합테스트

> 통합테스트는 연결된 여러 유닛을 인스턴스화하고 시작점이 되는 클래스의 인터페이스로 데이터를 보낸 후 유닛들의 네트워크가 기대한 대로 잘 동작하는지 검증한다.

<br>

#### ✔️ 시스템 테스트

> 시스템 테스트는 애플리케이션을 구성하는 모든 객체 네트워크를 가동시켜 특정 유스케이스가 전 계층에서 잘 동작하는지 검증한다.

<br><br>

---

### 테스트 하기전 GWT란

`given` - 준비단계로 테스트에 사용하는 변수, 입력 값 등을 정의하거나 Mock객체를 정의하는 구분도 given에 포함된다.

`when` - 실제로 액션을 하는 테스트를 실행하는 과정이다. 아래와 같이 실제 서비스 메서드를 실행하는 과정을 의미
> boolean check = checkService.check(xx);

`then` - 실제 테스트된 결과를 검증하는 과정이다, 예상한값과 실제로 나온값을 검증하는 부분.

---

### 단위 테스트로 도메인 엔티티 테스트하기 ( P.82 )

도메인 엔티티의 행동의 대한 테스트는 다른 클래스에 거의 의존하지 않기 때문에 다른 종류의 테스트는 필요하지 않는다.

---

### 단위 테스트로 유스케이스 테스트하기 ( P.85 )

테스트의 가독성을 높이기 위해 행동-주도 개발에서 일반적으로 사용되는 방식으로 `given`/`when`/`then`섹션으로 나눴다.

실제 업무에서 유스케이스를 테스트 하기위해서는 해당 서비스안에 여러가지 Service or Repositry들이 포함되어있다 해당 객체들은 Mockito라이브러리를 이용하여 목 객체를 생성할 수 있다.

모든 동작을 검증하는 대신 중요한 핵심만 골라 집중해서 테스트하는것이 좋다. 만약 모든 동작을 검증하려고 한다면 클래스가 조금이라도 바뀔 때마다 테스트를 변경해야 한다. 이는 테스트의 가치를 떨어뜨리는 일이다.

---

### 통합 테스트로 웹 어댑터 테스트하기 ( P.86 )

웹어댑터는 다음과 같은 동작을 한다.

- JSON문자열 등의 형태로 HTTP를 통해 입력을 받는다.
- 입력에 대한 유효성 검증을 한다.
- 유스케이스에서 아용할 수 있는 포맷으로 매핑한다
- 유스케이스에 전달한다
- 유스케이스의 결과를 JSON으로 매핑하고 HTTP 응답을 통해 클라이언트에 반환했다.

웹 어댑터에서는 해당 요청을 보내고, 응답의 상태를 검증하고, 모킹한 유스케이스가 잘 호출됐는지 검증한다.

그렇다면 웹 어댑터 테스트를 왜 단위테스트가 아닌 통합테스트라고 부를까

해당 테스트에서는 하나의 웹 컨트롤러 클래스만 테스트한것처럼 보이지만 실제로 뒤에서는 @WebMvcTest 어노테이션을 통해 스프링이 특정 요청 경로, 자바와 JSON간의 매핑, HTTP 입력검증 등에 필요한 전체
객체 네트워크를 인스턴스화하도록 만든다.

그리고 해당 테스트에서는 웹컨트롤러가 이 네트워크의 일부로서 잘 동작하는지 검증한다.

---

### 통합 테스트로 영속성 어댑터 ( P.89 )

웹 어댑터 테스트하기와 비슷한 이유로 영속성 어댑터의 테스트에는 단위 테스트보다는 통합 테스트를 적용하는것이 합리적이다. 단순히 어댑터의 로직만 검증하고 싶은 게 아니라 데이터베이스 매핑도 검증하고 싶기 때문이다.

영속성 어댑터에서의 통합테스트를 하기 위해서는 `@DataJpaTest`어노테이션을 통해 스프링 데이터 리포지토리들을 포함해서 데이터베이스 접근에 필요한 객체 네트워크를 인스턴스화 해야 한다고 스프링에게 알려준다.

추가로 `@Import`를 사용하요 특정 객체가 해당 네트워크에 추가됐다는 것을 명확하게 표현할 수 있다.

다만 주의해야할 점은 해당 테스트는 Mock 데이터를 사용한것이 아닌 실제 데이터베이스와 연동된다. 따라서 SQL구문의 오류나 테이블과 객체간의 매핑에러등으로 문제가 생길 확률이 높다.

이러한 문제의 해결방법으로 스프링에서는 기본적으로 `인메모리` 데이터베이스를 테스트에서 사용한다. 아무것도 설정할 필요 없이 곧바로 테스트할 수 있으므로 아주 실용적이다.

다만 해당 방식도 프로덕션 환경에서는 인메모리 DB를 사용하지 않는 경우가 많기 때문에 인메모리 데이터베이스에서 테스트가 완벽하게 통과했더라고 실제 DB에서도 문제가 생길 가능성은 있다.

하지만 이 방식도 문제가 생길수 있다고 한다. `TestContainers`같은 라이브러리는 필요한 데이터베이스를 도커 컨테이너에 띄울 수 있어 좋다고 한다.

---

### 시스템 테스트로 주요 경로 테스트하기 ( P.91 )

피라미드의 최상단에있는 시스템 테스트는 전체 애플리케이션을 띄우고 API를 통해 요청을 보내고 모든 계층이 조화롭게 잘 동작하는지 검증한다.

`@SpringBootTest` 어노테이션은 스프링이 애플리케이션을 구성하는 모든 객체 네트워크를 띄우게 한다.
(또한 랜덤 포트로 해당 애플리케이션을 띄우도록 설정되어있다.)

해당 테스트에서는 `MockMVC` 상요이 아는 `TestRestTemplate`를 사용하여 작성하였다. 다음과 같이 구성하면 테스트를 프로덕션 환경에 조금 더 가깝게 만들 수 있다.

- 시스템 테스트에서는 단위테스트나 통합테스트가 할 수 있는 것보다 훨씬 더 실제 사용자를 잘 흉내내기 때문에 사용자 관점에서 애플리케이션을 검증할 수 있다.
- 적절한 어휘를 사용하면 훨씬 더 쉬워진다,
- 시스템 테스트는 여러 개의 유스케이스를 결합해서 시나리오를 만들 때 더 빛이 난다. 각 시나리오는 사용자가 애플리케이션을 사용하면서 거쳐갈 특정 경로를 의미한다.
- 시스템 테스트를 통해 중요한 시나리오들이 커버된다면 최신 변경사항들이 애플리케이션을 망가뜨리지 않았음을 가정할 수 있고, 배포될 준비가 됐다는 확신을 가질 수 있다.

---

### 그렇다면 테스트를 얼마나 해야 충분할까

그렇다면 얼마나 테스트를 해야 충분할까??

해당 도서에서는 `라인커러리지`는 테스트 성공을 측정하는 데 있어서는 잘못된지표라고 설명한다. 코드의 중요한 부분이 전혀 커버되지 않을 수 있기 때문에 100%를 제외한 어떤 목표도 완전히 무의미하다.

이 책에서는 얼마나 마음 편하게 소프트웨어를 배포할 수 있느냐를 테스트의 성공 기준으로 삼으면 된다고 생각한다고 나와있다. 테스트를 신뢰하고 더 자주 배포할수록 테스트를 더 신뢰할 수 있다. 일년에 한두번만
배포한다면 해당 테스트를 신뢰할 수 없을 것이다.

처음에는 몇번의 도약이 필요하지만 프로덕션의 버그를 수정하고 이로부터 배우는것을 우선순위로 삼으면 제대로 가고있는 것이다.<br>
버그에 대해서는 해당 케이스를 커버할 수있는 테스트를 추가하고 시간이 지나면 이 작업들이 배포할때 마음을 편하게 해줄것이고, 남겨둔 기록은 시간이 지날수록 상황이 개선되고 있음을 증명해줄 것이다.

#### ✔️ 헥사고날 아케틱처에서 사용하는 전략은 다음과 같다

- 도메인 엔티티를 구현할 때는 단위 테스트로 커버하자
- 유스케이스를 구현할 때는 단위 테스트로 커버하자.
- 어댑터는 통합테스트로 커버하자
- 사용자가 취할 수 있는 중요 애플리케이션 경로는 시스템 테스트로 커버하자.

---

## 8. 경계 간 매핑하기

#### ✔️ 매핑에 찬성하는 개발자

두 계층 간에 매핑을 하지 않으면 양 계층에서 같은 모델을 사용해야 하는데, 이렇게 되면 두 계층이 강하게 결합된다!

#### ✔️ 매핑에 반대하는 개발자

두 계층 간에 매핑을 하게 되면 보일러플레이트 코드를 너무 많이 만들게 된다. 많은 유스케이스들이 오직 CRUD만 수행하고 계층에 걸쳐 같은 모델을 사용하기때문에 계층사이의 매핑은 과하다!

---

### `매핑하지 않기` 전략

P.93페이지의 이미지를 보게 되면 매핑하지 않고 하나의 매핑을 여러개의 계층에서 사용하는 이지미를 볼 수 있다.

해당 이미지에서는 웹 어댑터 계층,애플리케이션계층, 영속성 계층, 즉 모든 계층에서 하나의 모델을 사용하니 계층간 매핑을 전혀 할 필요가 없다.

그렇다면 사용하는 사람입장에서는 하나로 다 처리가 가능하니 당장 개발할떄는 편할것같다. 하지만 웹계층과 영속성 계층에서 특별한 요구사항이 있을경우 해당하는 요구사항을 하나의 매핑클래스에서 다 다뤄야한다. 그렇다면
해당 매핑 클래스는 웹, 애플리케이션, 영속성 계층과 관련된 이유로 인해 변경되야 하기 때문에 단일 책임 원칙을 위반한다.

> 그렇다면 해당 매핑하지않기 전략을 사용하지 말아야 하는가?

그렇지는 않다, 만약 모든 계층이 정확히 같은 구조의, 정확히 같은 정보를 필요로 한다면 `매핑하지 않기`전략은 완벽한 선택지다.

그러나 애플리케이션 계층이나 도메인 계층에서 웹과 영속성 문제를 다루게 되면 곧바로 다른 전략을 취해야 한다.

---

### `양방향 매핑` 전략 ( P. 100 )

각 계층이 전용 모델을 가진 매핑 전략을 양방향 매핑 전략이라고 한다.

각 계층이 전용 모델을 가지고 있기 때문에 각 계층에서 사용하는 모델을 변경하더라도 다른 계층에는 영향이 없다.

따라서 각각 데이터를 최적으로 표현할 수 있는 구조를 가질 수 있으며, 도메인 모델은 유스케이스를 제일 잘 구현할 수 있는 구조를 가질 수 있다.

또한 `매핑하지 않기`전략에서 나오는 `단일 책임 원칙`도 만족할 수 있다.

하지만 양방향 매핑도 단점이 있다.

먼저 너무 많은 보일러플레이트 코드가 생긴다. 코드의 양을 줄이기 위해 매핑 프레임워크를 사용하더라도 두 모델 간 매핑을 구현하는 데는 시간이 든다, 특히 매핑 프레임워크가 내부 동작 방식을 제네릭 코드와
리플렉션뒤로 숨길경우 매핑 로직을 디버깅하는 것은 꽤나 고통스럽다.

---

### `완전 매핑` 전략 ( P. 102 )

와완전 매핑 전략에서는 각 연산마다 별도의 입출력 모델을 사용한다. 계층 경계를 넘어 통신할 때 도메인 모델을 사용ㅇ하는 대신 각 작업에 특화된 모델을 사용한다.

이런 모델을 가르켜 커맨드 or 요청 혹은 이와 비슷한단어로 표현한다.

- 웹계층은 입력을 애플리케이션 계층의 커맨드 객체로 매핑할 책임을 가지고있다.
- 애플리 케이션 계층은 커맨드 객체를 유스케이스에 따라 도메인 모델을 변경하기 위해 필요한 무엇인가로 매핑할 책임을 가진다.
  > 비록 이렇게 매핑하면 여러 유스케이스의 요구사항을 함께다뤄야 하는 매핑에 비해 구현하고 유지보수하기가 훨씬 쉽다.

### `단방향 매핑` 전략 ( P. 103 )

이 전략에서는 모든 계층의 모델들이 같은 인터페이스를 구현한다. 이 인터페이스는 관련있는 특성에 대한 getter 메서드를 제공하여 도메인 모델의 상태를 캡슐화한다.

모든 계층은 다른 계층으로부터 객체를 받을 때 자신이 이용할 수 있도록 매핑하면된다. 그래서 매핑의 대상이 한 인터페이스로 고정되어 있어서 단방향 매핑전략이라고 부른다.

다만 이 전략은 계층간의 모델이 비슷할 때 가장 효과적이다.

### 언제 어떤 매핑 전략을 사용해야 하는가

특정 상황 특정 시점에 최선의 전략을 선택해라 ...


---

## 9. 애플리케이션 조립하기

### 왜 조립까지 신경써야 하나

코드 의존성이 올바른 방향을 가리키게 하기 위해서다, 모든 의존성은 안쪽으로, 애플리케이션의 도메인 코드 방향으로 향해야 도메인 코드가 바깥 계층의 변경으로부터 안전하다는점이다.

유스케이스가 영속성 어댑터를 호출해야하고 스스로 인스턴스화 한다면 코드 의존성이 잘못된 방향으로 만들어진 것이다.

`유스케이스는 인터페이스만 알아야 하고, 런타임시에 인터페이스의 구현을 제공 받아야한다.`

우리의 객체 인스턴스를 생성할 책임은 중립적이고 인스턴스 생성을 위해 모든 클래스에 대한 의존성을 가지는 설정 컴포넌트가 있어야 한다는 것이다.

설정 컴포넌트는 우리가 제공한 조각들로 애플리케이션을 조립하는것을 책임진다.

- 웹 어댑터 인스턴스 생성
- HTTP 요청이 실제로 웹어댑터로 전달되로고 보장
- 유스케이스 인스턴스 생성
- 웹 어댑터에 유스케이스 인스턴스 제공
- 영속성 어댑터 인스턴스 생성
- 유스케이스에 영속성 어댑터 인스턴스 제공
- 영속성 어댑터가 실제로 데이터베이스에 접근할 수 있도록 보장

더불어 설정 컴포넌트는 설정 파일이나 커맨드라인 파라미터 등과 같은 설정 파라미터의 소스에도 접근할 수 있어야 한다.

이렇게 설정파일은 책임이 많다, 비록 단일책임원칙을 위반하지만 나머지 부분을 깔끔하게 유지하고 싶다면 어쩔 수 없다..

### 평범한 코드로 조립하기.

P.110 이미지 참고.

해당 이미지를 보면, Repository생성, Adapter생성시 Repository 전달 후 Adapter 생성, Usecase생성시 apapter 전달, Controller 생성시 Usecase 전달

생성한 후 함꼐 연결하여 작성할 수 있다.

하지만 이 방법에도 몇가지 단점이 있다.

1. 해당 의존성이 한두개라면 단순하게 작성 할 수 있다. 하지만 완전한 엔터프라이즈 애플리케이션을 실행하기 위해서는 이러한 코드를 얼마나 많이 만들어야하는지도 상상하라
2. 각 클래스가 속한 패키지 외부에서 인스턴스를 생성하기 때문에 이 클래스들은 전부 Public이어야 한다. 이렇게 된다면 아무것도 모르는 다른 개발자가 public하기 때문에 외부에서 직접 접근하는 것을 막지
   못한다. package-private 접근 제한자를 이용하면 이러한 원치 않은 의존성을 피할 수 있다. 다행히도 이러한 작업을 대신해주는것이 바로 스프링 프레임워크이다.

---

### 스프링의 클래스 패스 스캐닝으로 조립하기.

스프링 프레임워크를 이용하여 애플리케이션을 조립한 결과물을 애플리케이션 컨텍스트라고 한다.<br>
애플리케이션 컨텍스트는 애플리케이션을 구성하는 모든 객체를 포함한다. (흔히 Bean이라고 부름)

스프링에는 컨텍스트를 조립하기 위한 몇가지 방법이 있는데 첫번쨰 방법은 `클래스 패스 스캐닝` 이다.

#### ✔️ 스프링 클래스 패스 스캐닝

`스프링 클래스 패스 스캐닝` 이란 클래스패스에서 접근 가능한 모든 클래스를 확인하여 `@Component` 어노테이션이 붙은 모든 클래스를 찾는다. 그리고 이 어노테이션이 붙은 각 클래스의 객체를 생성한다.

P.112 코드 참고

스프링은 `@Component`가 붙은 클래스를 찾고 해당 클래스들의 인스턴스를 만들어 애플리케이션 컨텍스트에 추가한다. 필요한 객체들이 모두 생성되면 해당 클래스의 생성자를 호출하고 생성된 객체도 마찬가지로
애플리케이션 컨텍스트에 추가한다.

`클래스 패스 스캐닝` 방식을 사용하면 아주 편하게 애플리케이션을 조립할 수 있다.

하지만 `클래스 패스 스캐닝`방식이 장점만 있는것은 아니다. 단점은 다음과 같다

- 클래스에 프레임워크에 특화된 어노테이션을 붙여야 한다는 점이다. 클린아키텍처파는 이런 방식이 코드를 특정한 프레임워크와 결합시키기 때문에 사용하지 말아야 한다고 주장할 것이다.
- 개발자가 해당 애플리케이션에 존재하는 모든 클래스를 하나하나 자세히 알지 못하기 때문에 악의적으로 조작해서 추적하기 어려운 에러를 일으킬 수 있다.

---

### 스프링의 자바 컨피그로 조립하기.

`@Component`가 아닌 `@Configuration`을 사용하는 방식이다. 해당 박식에서는 애플리케이션 컨텍스트에 추가할 빈을 생성하는 설정 클래스를 만든다.

```java

@Configuration
class xxxConfiguration {

    @Bean
    public xxxAdapter xxxAdapter(xxx xxx, ccc ccc) {
    }
}
```

`@Configuration`을 사용한다면 해당 어노테이션을 통해 해당 클래스가 스프링의 클래스패스 스캐닝에서 발견해야 할 설정 클래스임을 표시해둔다. 따라서 여전히 클래스패스 스캐닝을 사용하고 있지만 보든 빈을
가져오는 대신 설정 클래스만 선택하기 때문에 해로운 마법(악의적 조작)이 일어날 확률이 줄어든다.

해당 박식은 `클래스패스 스캐닝`방식과 달리 @Component 어노테이션을 코드에 덕지덕지 붙이도록 강제하지도 않으며, 의존성 없이 깔끔하게 유지할 수 있다.

하지만 이 방식에도 문제점은 있다.

설정 클래스가 생성하는 빈이 설정클래스와 같은 패키지에 존재하지 않는다면 해당 빈들을 public으로 만들어야 한다. 가시성을 제한하기 위해 패키지를 모듈 경계로 사용하고 각 패키지안에 전용 설정 클래스를
만들수는있다 . 하지만 이렇게 작성하게 된다면 하위 패키지를 사용할 수 없다.

---

### 유지보수 가능한 소프트웨어를 만드는 데 어떻게 도움이 될까 ?

클래스 패스 스캐닝은 아주 편리한 기능이다. 스피링에게 해당 패키지만 알려주면 알아서 찾아서 조립해준다. 하지만 코드의 규모가 커지면 금방 투명성이 낮아진다.

어떤 빈이 애플리케이션 컨텍스트에 올라오는지 정확히 알 수 없을 뿐더러 애플리케이션 컨텍스트의 일부만 독립적으로 띄우기가 어려워진다.

반면 설정 컴포넌트를 만들면 애플리케이션이 이러한 책음으로부터 자유로워진다.

---

## 10. 아키텍처 경계 강제하기

### 경계와 의존성

---

#### ✔️ 접근 제한자

경계를 강제하기 위해 자바에서 제공하는 가장 기본적인 도구는 `접근제한자`이다.

접근제한자는 public, protected, package-private(default), private 제한자가 잇다.

package-private 제한자는 자바 패키지를 통해 클래스들을 응집적인 `모듈`로 만들어 주기 때문에 중요하다.

이러한 모듈 내에 있는 클래스들은 서로 접근가능하지만, 패키지 바깥에서는 접근할 수 없다. 그러면 모듈의 진입점으로 활용될 클래스들만 골라서 public 으로 만들면된다. 이렇게 작성하게 되면 의존성이 잘못된 방향을
가리켜서 의존성 규칙을 위반할 위험이 줄어든다.

package-private 제한자는 몇개 정도의 클래스로만 이뤄진 작은 모듈에서 가장 효과적이다. 그러나 패키지내의 클래스가 특정 개수를 넘어가기 시작하면 하나의 패키지에 너무 많은 클래스를 포함하는것이
혼란스러워진다. 따라서 하위 패키지를 만드는방법을 선호한다.

하지만 자바에서는 하위 패키지를 다른 패키지로 취급하기 때문에 하위패키지의 package-private에 접근할 수 없게 된다, 따라서 하위 패키지의 멤버는 public하게 만들어서 바깥세계에 노출시켜야 하기 때문에
아키텍처에서 의존성 규칙이 깨질 수 있는 환경이 만들어진다.

---

#### ✔️ 컴파일 후 체크

클래스에 public 제한자를 사용하면 의존성 방향이 잘못되더라도 컴파일러는 다른 클래스들이 이클래스를 사용하도록 허용한다 이러한 경우에는 컴파일러가 전혀 도움이 되지 않는다. 따라서 다른 수단을 찾아야 한다.

그 한 가지 방법은 `컴파일 후 체크`를 도입하는 것이다.

`컴파일 후 체크`는 즉 코드가 컴파일된 후에 런타임에 체크한다는 뜻이다. 이러한 런타임 체크는 지속적인 통합 빌드 환경에서 자동화된 테스트 과정에서 가장 잘 동작한다.

이러한 체크를 도와주는 자바 도구는 `ArchUnit`이 있다. 해당 도구는 의존성 방향이 기대한 대로 잘 설정돼 있는지 체크할 수 있는 API를 제공한다.

의존성 규칙 위반을 발견하면 예외를 던지다. 이 도구는 JUnit 과 같은 단위 테스트 프레임워크 기반에서 잘 동작하며 의존성 규칙이 위배되면 테스트를 실패 시킨다.

P.124 참고

참고 URL [Naver D2에서 ArchUnit 정리](https://d2.naver.com/helloworld/9222129)

---

#### ✔️ 빌드 아티팩트

빌드 아티팩트는 멀티 모듈을 활용 한다고 보면 편할듯하다.

각 모듈의 빌드 스크립트에 아키텍처에서 허용하는 의존성만 접근하도록 작성한다.

---

## 11. 의식적으로 지름길 사용하기

### 깨끗한 상태로 시작할 책임

가능한 지름길을 쓰지 않고 기술 부채를 지지 않은채로프로젝트를 깨끗하게 시작하는것이 중요하다. 지름길이 몰래 스며드는 순간 더 많은 지름길을 끌어들여 코드의 품질이 떨어질 수 있다.

하지만 때로는 지름길을 취하는 것이 더 실용적일 때도 있다. 유용한 만큼 의도적인 지름길에 대해서 잘 기록해둬야 한다. 미래의 우리 또는 인계받는 사람들에게 합리적인 이유에서 의도적으로 지름길이 추가됐다는 사실을
알려야 인계받은 사람들이 더 나쁜 지름길로 빠지는것을 방지할 수 있다.

### 유스케이스 간 모델 공유

P.135의 그림 11.1은 두개의 유스케이스가 같은 입력모델을 공유하는 예제를 보여준다. 이렇게 유스케이스 간에 입출력 모델을 공유하게 되면 유스케이스들 사이에 결함이 생긴다.

공유로 인한 영향은 두개의 UseCase가 결합된다는 것이다. 공유하고 있는 모델이 변경되게 된다면 두 UseCase 모두 영향을 받는다.
단일 책임 원칙에서 이야기 하는 `변경할 이류`를 공유하는 것이다. 출력 모델을 공유하는 경우도 마찬가지다.

만약 두 유스케이스가 서로간에 미치는 영향 없이 독립적으로 진화해야 한다면 입출력모델을 따로 분리하여 시작하라.

---

