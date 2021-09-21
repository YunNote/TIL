> 모든 내용은 저의 개인적인 생각입니다. 잘못된 부분은 문의 부탁드립니다.

## Interface를 사용하는 이유

> 인터페이스(interface)를 사용하는 이유는 상속, 코드 종속성이 낮은 프로그래밍,표준화의 가능이지 않을까 싶다.

---

### 😊 상속의 이점

예를 들어서 `사과`와 `포도`에 대한 클래스가 있다고 가정하겠습니다. <br>
프로그램상에서 `사과`와`포도`를 과일 바구니에 담아서 관리하려고 합니다. 그렇다면 과일을 담을 수 있는 바구니에 
`사과`와 `포도`를 넣어야 합니다. 하지만 `Bucket` 클래스 입장에서는 `사과`와 `포도`를 어떻게 관리해야 할까요  
```java
class Apple {
    private static final double discountRate = 0.05;
    private Long sugarContent;
    private Long size;
    private Long price;
}

class Grape {
    private Long sugarContent;
    private Long size;
    private Long price;
}

class Main() {
    
    public static void main(String[] args) {
        Apple apple = new Apple(...);
        Grape grape = new Grame(...);
    }
}

```

상속을 사용하여 `과일`에 대한 클래스를 생성한다면 쉽게 관리할 수 있습니다.

```java

class Bucket {
    List<Fruit> fruit = new ArrayList<Fruit>();
    
    public void addFruit(Fruit fruit) {
        this.fruit.add(fruit);
    }
}

interface Fruit {
    ...
}

class Apple implements Fruit{...}
class Grape implements Fruit {...}



class Main() {
    public static void main(String[] args) {
        Apple apple = new Apple(...);
        Grape grape = new Grame(...);
    }
}

```

---

### 😊 코드 종속성이 낮은 프로그래밍 

위에 내용에서 예를 `사과`중에서도 `호주산 사과`가 추가되고 최대 할인률이 있다고 가정하겠습니다.
국산사과는 5%, 호주산 사과는 10%라고 가정합니다. 


```java
// 이전 코드 
class Apple {
    
    private Long sugarContent;
    private Long size;
    private Long price;
    
    public koreaPrice() {
        return price - (rice * 0.05);
    }
    
    public australiaPrice(){
        return Math.round(price - (price * 0.1));
    }
}
```
한국산 사과의 가격과, 호주산 사과의 가격을 각각 가져오는 메소드를 생성해야 하는것일까 ??

그렇다면 나라별 사과 품종이 추가될때마다 메소드를 추가해야하는걸까요? 아니면 계속 수정을 해야하는걸까요 .

이러한 방식은 유연하지 못하고 기능의 추가가 될때마다 문제가 발생할 수 있는 매우 않좋은 방식입니다.

이러한 문제를 interface를 이용하여 해결하면 다음과 같습니다.

```java
interface Fruit { ...
}

interface ApplePrice {
    Long price();
}

// default Apple는 국산 사과라고 치겠습니다.
class Apple implements Fruit, ApplePrice {...
}

// 호주 사과에 대한 클래스를 추가
class AustraliaApple implements Fruit, ApplePrice {
    private static final double discountRate = 0.1;

    @Override
    public Long price() {
        return Math.round(price - (price * discountRate));
    }...
}
```

위와 같이 class를 추가하고 메소드 오버라이딩을 사용하면 어느 나라의 사과의 price인지는 알필요 없이 price()를 호출하면 각 나라에 대하여 계산한 값이 나온다.

따라서 직접적으로 기존 코드의 수정을 하지 않아도 되기때문에 OCP인 Open Closed Principle 개방 폐쇠 원칙에 맞게 코드를 작성할 수 있다.

