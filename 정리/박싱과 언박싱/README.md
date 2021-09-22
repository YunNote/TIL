## Java의 박싱과 언박싱 (Boxing & UnBoxing)

---

Java의 박싱과 언박싱의 핵심만 보면 다음과 같다.

> `Boxing`<br>
> Primitive Type의 자료형을 Wrapper Type의 자료형으로 변환하는 것


> UnBoxing<br>
> Wrapper Type의 자료형을 Primitive Type의 자료형으로 변환하는 것 


우리가 아는 Primitive Type은 무엇이 있고 Wrapper Type에는 무엇이 있는지 알아야 한다.


### ⭐ Primitive Type
`boolean`, `byte`, `char`, `short`, `int`, `long`, `float`, `double`

---

### ⭐ Primitive Type
`Boolean`, `Byte`, `Char`, `Short`, `Int`, `Long`, `Float`, `Double`


---


## 오토박싱과 오토언박싱 (AutoBoxing & AutoUnBoxing)

Java 1.5 버전 이상부터 박싱과 언박싱은 자동으로 해결해주는 개념이 추가되었습니다.

```java
Integer a = new Integer(3); // 일반 박싱
Integer a = 3; // 오토 박싱 
```

```java

Integer a = new Integer(3);

int b = a.intValue(); // 일반 언박싱 
int b = a; // 오토 언박싱 
```



