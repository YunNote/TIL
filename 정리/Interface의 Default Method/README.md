
## Interface의 Default Medthod란

---

>대학교에서 Java공부를 하고, 학원에서 6개월을 공부하면서 Java 1.8이상에서 `Default Method`와 `Static Method`를 지원하는 것은 알았으나
실제로 코드로 구현해본적이 없었다. 그러던 중 면접에서 다음과 같은 내용들이 자주 나온다는 이야기를 듣고 해당 내용을 정리하고자 쓴 글입니다.


먼저 우리가 흔히 알고 사용하는 interface 의 구조를 보겠습니다. 

```java
interface Car{
    public static final Long MAX_SPEED = 200L;
    public static final Long MIN_SPEED = 0L;
    
    public abstract Long maxSpeed();
    public abstract Long minSpeed();
}
```

`public static final`로 선언된 상수와, `public abstract`로 구성된 추상 메서드로 구현되어 있습니다.

그렇다면 Java 1.8에서 추가된 `default method`에 대해 알아보도록 하겠습니다. 

---

### ⭐ default method
> default Method는 interface내부에 구현체가 있는 Method의 작성을 지원하는 기능입니다.

```java
interface Car{
    public static final Long MAX_SPEED = 200L;
    public static final Long MIN_SPEED = 0L;
    
    public abstract Long maxSpeed();
    public abstract Long minSpeed();
    
    public default void checkDrive(boolean drive) {
        if(!drive) {
            System.out.println("운전중이지 않습니다");
            return;
        }
        System.out.println("운전중 입니다");
    }
}
```

그래서 default method는 언제사용할까. 실제로 어디에 사용되었나 찾아보니 List와 ArrayList를 보면 찾아볼수 있었습니다.

List interface와 ArrayList의 replaceAll을 보면 다음과 같이 되어있습니다.

```java
// List Interface
public interface List<E> extends Collection<E> {
    ...
    
    default void replaceAll(UnaryOperator<E> operator) {
        Objects.requireNonNull(operator);
        final ListIterator<E> li = this.listIterator();
        while (li.hasNext()) {
            li.set(operator.apply(li.next()));
        }
    }
}

// ArrayList
public class ArrayList<E> extends AbstractList<E>
        implements List<E>, RandomAccess, Cloneable, java.io.Serializable {
    @Override
    public void replaceAll(UnaryOperator<E> operator) {
        replaceAllRange(operator, 0, size);
        modCount++;
    }
}
```

List와 ArrayList를 보니 다음과 같은 생각을 할 수 있었습니다. interface 에 default method가 없었다면.

List를 상속 또는 구현한 모든 클래스에서 replaceAll 메소드를 재구현해야 하는 문제가 발생합니다. 

하지만 default method를 통해 replaceAll 메서드를 선언해 놓고나니 재구현이 필요한 곳에서만 @Override 를 하여 재구현하여 사용하면 됩니다 .

따라서 interface에 새로운 메소드가 구현되었다고 하여 구현체에서 변경해야할 필요가 필수로 있는것은 아니다.

---


### ⭐ static method

static method 는 말그대로 interface에 static method를 작성할 수 있는 기능입니다.

```java

interface A {
    
    public static void print() {
        System.out.println("Hello YunNote");
    }
}

// A.print()와 같이 호출 가능 
```

