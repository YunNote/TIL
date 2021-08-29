> 개발 및 설계를 하면서 객체지향의 5대 원칙 or SOLID라는 말을 많이 들어봤습니다. <br>
> 하지만 대략적인 내용만 알지 제대로 기억나지 않아 이렇게 정리해봅니다 ...

[참고한 블로그](https://dev-momo.tistory.com/entry/SOLID-%EC%9B%90%EC%B9%99)

<strong>S</strong> : Single Responsibility Principle (단일 책임 원칙)<br>
<strong>O</strong> : Open-Closed Principle<br>
<strong>L</strong> : Liskov Substitution Principle<br>
<strong>I</strong> : Dependency Inversion Principle <br>
<strong>D</strong> : Interface Segregation Principle<br>

### 😊 Single Responsibility Principle (단일 책임 원칙)

---

> 이말은 즉 <strong>소프트웨어의 설계 부품(클래스 or 함수)는 단 하나의 책임만을 가져야한다.</strong><br>
> 만약 한 클래스가 수행할 수 있는 기능, 책임이 많아지게 된다면, 내부의 함수끼리 강한 결합을 발생시킬 가능성이 많아지게 되고.
> 유지보수에 비용이 증가하기 떄문에 책임을 분리하여 관리할 필요가 있다.

<br>

### 😊 Open-Closed Principle (개방 폐쇄 원칙)

---

> <strong>소프트웨어 요소는 확장에는 열려 있으나 변경에는 닫혀 있어야 한다.<strong><br>
> 이 말은 즉 기존의 코드를 변경하지 않고 기능을 수정하거나 추가할 수 있도록설계해야 한다는 의미입니다.


<br>

### 😊 Liskov Substitution Principle (리스코프 치환 원칙)

---

> <strong>자식 클래스는 부모 클래스에서 가능한 행위를 수행할 수 있어야 한다.</strong><br>
> 리스코프 치환 원칙은 MIT 컴퓨터 사이언스 교수인 리스코프가 제안한 설계 원칙입니다.
> 이는 객체 지향 프로그래밍에서는 부모 클래스의 인스턴스 대신 자식 클래스의 인스턴스를 사용해도 문제가 없어야 한다는 내용입니다.
>

<br>

### 😊 Interface Segregation Principle (인터페이스 분리 원칙)

---

> <strong>한 클래스는 자신이 사용하지 않는 인터페이스는 구현하지 말아야 한다.<br>
> 하나의 일반적인 인터페이스 보다는 여러개의 구체적인 인터페이스가 좋다.</strong><br>
> 해당 내용은 우리가 사용하지 않는 기능에는 영향을 받지 말아야 한다는 의미이다.

<br>

### 😊 Dependency Inversion Principle (의존 역전 원칙)

---

> <strong>의존 관계는 변하기 쉬운것 보다 변하기 어려운 것에 의존해야 한다는 원칙</strong><br>
> 의존 관계를 맺을때 구체적인 클래스보다, 인터페이스나 추상클래스와 관계를 맺는다는것을 의미.