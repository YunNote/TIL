#  Fixture를 활용한 테스트코드 작성, 그런데 🙉 `FixtureMonkey`를 곁들인...   

안녕하세요.  😀<br>
올리브영 트랜잭션개발팀에서 백엔드 개발을 하고 있는 윤노트입니다.

이번 글에서는 테스트 코드를 작성하면서 사용하게되는 Fixture에 대한 설명과 어떻게 사용하여 
테스트코드를 작성하였는지데 대해서 정리하였습니다.

해당 글은 Fixture를 처음 경험한다는 가정하에 설명하도록 하겠습니다.

---
## 🛠️ Fixture

먼저 `Fixture`가 무엇인지 알아보겠습니다. `Fixture`는 말그대로 `고정되어있는 물체`를 의미합니다.

개발을 함에 있어서 제가 생각하는 `Fixture` 란 다음과 같습니다.

> 특정 객체에 대해서 사전에 미리 정의하여 필요시 정의된 객체를 호출해서 사용하는 용도. <br>
> 한마디로 `객체 생성 및 초기화 코드를 Fixture로 정의하고 테스트 코드에서 필요한 객체르 호출하여 사용하는 용도` 라고 생각합니다.

---

## 🤔 Fixture 어떻게 사용하고 있는데?

테스트 코드를 작성하면서 <b>한.번.쯤</b>은 누구나 테스트용 객체를 어떻게 구성해야 할지.<br>
어떻게 데이터를 넣어여 재사 및 운영할때 좋은 객체가 생성될지 고민을 해보셨을거라고 생각합니다.

이러한 고민을 해결해주기 위한 방법으로는 `생성자를 통해 생성하는 방식`, `패턴을 활용하는 방식`, `JSON 파일로 만들어놓고 ObjectMapper를 통해 불러오는 방식` 등등 
 다양한 방식을 활용하여 객체를 사용할 수 있습니다.

여러가지 방식중 <b>파트너스쿼드</b> 에서는 `Test Data Builder 패턴`과 `Object Mother 패턴` 을 활용한 방식과, `JSON 파일을 Object로 변환`하는 방식을 활용하여 
테스트 코드를 사용하였었습니다.

<br>

---

## 🛠️ 직접 생성자를 통해 Fixture 생성 방법

> 말그대로 사용하는 테스트 시점에 생성하거나, @BeforeAll 또는 @BeforeEach 를 통하여 테스트 시작 전에 생성할 수 있다. 

```java

public class SampleTest {

    private static User user;

    @BeforeAll
    static void setup() {
        System.out.println(1);
        user = new User(/* name */ "윤노트",  /* age */ 32,  /* intro */"🧑‍💻");
    }

    @Test
    void sampleTest() {

        final String expectName = "윤노트";
        final int age = 32;
        final String intro = "🧑‍💻";
        final User actual = UserFixture.createUser();

        Assertions.assertAll(
                () -> Assertions.assertEquals(expectName, actual.getName()),
                () -> Assertions.assertEquals(age, actual.getAge()),
                () -> Assertions.assertEquals(intro, actual.getIntro())
        );
    }
}
```

---

## 🛠️ Test Data Builder 패턴과 Object Mother 패턴을  통해 Fixture 생성

> Builder를 직접 구현하여 편의메서드를 만들거나, Lombok에서 제공하는 @Builder를 사용하여 구성 하는 방법도 있습니다.

아래와 같이 직접 구현하면 필요한 부분에 대해서는 편의메서드로 직접 생성하여 사용할 수 있습니다.  대부분 Stub

[//]: # ()
[//]: # (<details>)

[//]: # ( <summary> <b style="font-size: 18px;">User 코드</b> </summary>)

[//]: # ()
[//]: # (## User.class)

[//]: # (```java)

[//]: # (/** User.class */)

[//]: # (@Getter)

[//]: # (@Builder)

[//]: # (public class User {)

[//]: # ()
[//]: # (    private String name;)

[//]: # (    private int age;)

[//]: # (    private String intro;)

[//]: # ()
[//]: # (    private User &#40;UserBuilder userBuilder&#41; {)

[//]: # (        this.name = userBuilder.name;)

[//]: # (        this.age = userBuilder.age;)

[//]: # (        this.intro = userBuilder.intro;)

[//]: # (    })

[//]: # ()
[//]: # (    public static class UserBuilder {)

[//]: # ()
[//]: # (        private String name;)

[//]: # (        private int age;)

[//]: # (        private String intro;)

[//]: # ()
[//]: # (        public UserBuilder name&#40;String name&#41; {)

[//]: # (            this.name = name;)

[//]: # (            return this;)

[//]: # (        })

[//]: # ()
[//]: # (        public UserBuilder age&#40;int age&#41; {)

[//]: # (            this.age = age;)

[//]: # (            return this;)

[//]: # (        })

[//]: # ()
[//]: # (        public UserBuilder intro&#40;String intro &#41; {)

[//]: # (            this.intro = intro;)

[//]: # (            return this;)

[//]: # (        })

[//]: # ()
[//]: # (        public User build&#40;&#41; {)

[//]: # (            return new User&#40;this&#41;;)

[//]: # (        })

[//]: # (    })

[//]: # (})

[//]: # ()
[//]: # (```)

[//]: # (</details>)

### User 코드

```java
/** User.class */
@Getter
@Builder
public class User {

    private String name;
    private int age;
    private String intro;

    private User (UserBuilder userBuilder) {
        this.name = userBuilder.name;
        this.age = userBuilder.age;
        this.intro = userBuilder.intro;
    }

    public static class UserBuilder {

        private String name;
        private int age;
        private String intro;

        public UserBuilder name(String name) {
            this.name = name;
            return this;
        }

        public UserBuilder age(int age) {
            this.age = age;
            return this;
        }

        public UserBuilder intro(String intro ) {
            this.intro = intro;
            return this;
        }

        public User build() {
            return new User(this);
        }
    }
}

```


[//]: # (<details>)

[//]: # ( <summary> <b style="font-size: 18px;">UserFixture 코드</b> </summary>)

[//]: # ()
[//]: # (## UserFixture.class)

[//]: # (```java)

[//]: # (public class UserFixture {)

[//]: # (    public static User createUser&#40;&#41; {)

[//]: # (        // 직접 작성한 Builder )

[//]: # (        return new User.UserBuilder&#40;&#41;)

[//]: # (                .name&#40;"윤노트"&#41;)

[//]: # (                .age&#40;32&#41;)

[//]: # (                .intro&#40;"🧑‍💻"&#41;)

[//]: # (                .build&#40;&#41;;)

[//]: # (    })

[//]: # ()
[//]: # (    public static User createUserBuilderType&#40;&#41; {)

[//]: # (        // Lombok을 사용한 Builder)

[//]: # (        return User.builder&#40;&#41;)

[//]: # (                .name&#40;"윤노트"&#41;)

[//]: # (                .age&#40;32&#41;)

[//]: # (                .intro&#40;"🧑‍💻"&#41;)

[//]: # (                .build&#40;&#41;;)

[//]: # (    })

[//]: # (})

[//]: # (```)

[//]: # (</details>)

### UserFixture 코드

```java
public class UserFixture {
    public static User createUser() {
        // 직접 작성한 Builder 
        return new User.UserBuilder()
                .name("윤노트")
                .age(32)
                .intro("🧑‍💻")
                .build();
    }

    public static User createUserBuilderType() {
        // Lombok을 사용한 Builder
        return User.builder()
                .name("윤노트")
                .age(32)
                .intro("🧑‍💻")
                .build();
    }
}
```


### 테스트 코드

[//]: # (<details>)

[//]: # ( <summary> <b style="font-size: 18px;">테스트 코드</b> </summary>)

[//]: # ()
[//]: # (## Test.class)

[//]: # (```java)

[//]: # ()
[//]: # (@DisplayName&#40;"[User] 직접 구현한 Builder Test"&#41; // Success)

[//]: # (@Test)

[//]: # (void builderTypeTest&#40;&#41; {)

[//]: # ()
[//]: # (    final String expectName = "윤노트";)

[//]: # (    final int age = 32;)

[//]: # (    final String intro = "🧑‍💻";)

[//]: # (    final User actual = UserFixture.createUser&#40;&#41;;)

[//]: # ()
[//]: # (    Assertions.assertAll&#40;)

[//]: # (            &#40;&#41; -> Assertions.assertEquals&#40;expectName, actual.getName&#40;&#41;&#41;,)

[//]: # (            &#40;&#41; -> Assertions.assertEquals&#40;age, actual.getAge&#40;&#41;&#41;,)

[//]: # (            &#40;&#41; -> Assertions.assertEquals&#40;intro, actual.getIntro&#40;&#41;&#41;)

[//]: # (    &#41;;)

[//]: # ()
[//]: # (})

[//]: # ()
[//]: # (@DisplayName&#40;"[User] Lombok Builder Test"&#41; // Success)

[//]: # (@Test)

[//]: # (void lombokBuilderTypeTest &#40;&#41; {)

[//]: # ()
[//]: # (    final String expectName = "윤노트";)

[//]: # (    final int age = 32;)

[//]: # (    final String intro = "🧑‍💻";)

[//]: # (    final User actual = UserFixture.createUser&#40;&#41;;)

[//]: # ()
[//]: # (    Assertions.assertAll&#40;)

[//]: # (            &#40;&#41; -> Assertions.assertEquals&#40;expectName, actual.getName&#40;&#41;&#41;,)

[//]: # (            &#40;&#41; -> Assertions.assertEquals&#40;age, actual.getAge&#40;&#41;&#41;,)

[//]: # (            &#40;&#41; -> Assertions.assertEquals&#40;intro, actual.getIntro&#40;&#41;&#41;)

[//]: # (    &#41;;)

[//]: # (})

[//]: # (```)

[//]: # (</details>)

```java

@DisplayName("[User] 직접 구현한 Builder Test") // Success
@Test
void builderTypeTest() {

    final String expectName = "윤노트";
    final int age = 32;
    final String intro = "🧑‍💻";
    final User actual = UserFixture.createUser();

    Assertions.assertAll(
            () -> Assertions.assertEquals(expectName, actual.getName()),
            () -> Assertions.assertEquals(age, actual.getAge()),
            () -> Assertions.assertEquals(intro, actual.getIntro())
    );

}

@DisplayName("[User] Lombok Builder Test") // Success
@Test
void lombokBuilderTypeTest () {

    final String expectName = "윤노트";
    final int age = 32;
    final String intro = "🧑‍💻";
    final User actual = UserFixture.createUser();

    Assertions.assertAll(
            () -> Assertions.assertEquals(expectName, actual.getName()),
            () -> Assertions.assertEquals(age, actual.getAge()),
            () -> Assertions.assertEquals(intro, actual.getIntro())
    );
}
```

<br>

---

## 🤔 기존방식에서 변경하려는 이유

파트너스쿼드에서 사용하고 있던 JSON to Object 방식과 직접 객체를생성해주는 방식을 사용하던중 `Fixture Monkey` 를 찾게 되었고 아래와 같은 이유로 변경을 하게 되었습니다.

1. 유연성 부족 및 코드 동기화 어려움.
   > API에 대해서 테스트 코드 작성 후 API의 응답 형식 및 API 자체가 변경될 경우 테스트 코드도 함께 수정이 필요하다. 또한 빠르게 API를 수정하다 보니 테스트 코드를 수정하지 못하여 동기화가 되지 못하는 경우.

2. 개발자가 개발 하고 테스트 코드를 작성하다보니 놓치게 되는 엣지케이스.
   > 테스트 코드를 미리 작업하고 API를 작성하면 좋지만 그렇지 못한 경우 API를 작성한 후 테스트 코드를 작성하다보니 <br> 
   > 이미 나의 뇌가 어떻게 데이터를 넣어야 에러가 안나는지 학습해버려서 .. 엣지케이스를 놓치는 경우..

3. 다양한 테스트 객체를 생성하여 테스트 커버리즈를 높이기 위해 오히려 복잡해지는 코드.















⬜⬛⬛⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬛⬛⬛⬜⬜⬛⬛⬛⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬛
⬛⬛⬜⬜⬛⬛⬛⬛⬛⬛⬛⬜⬜⬛⬜⬜⬛⬛⬜⬜⬜⬛⬜⬜⬜⬛⬜⬜⬛⬛⬛⬛⬛⬛
⬛⬜⬜⬛⬛⬛⬛⬛⬛⬛⬜⬜⬛⬛⬛⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬛⬛⬛⬛⬜⬜
⬛⬜⬜⬛⬛⬛⬜⬜⬜⬛⬜⬜⬛⬛⬛⬜⬜⬛⬜⬜⬛⬜⬛⬜⬜⬛⬜⬜⬜⬜⬜⬛⬜⬜
⬛⬜⬜⬛⬛⬛⬛⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬛⬛⬛⬜⬜⬛⬜⬜⬛⬛⬛⬛⬜⬜
⬛⬛⬜⬜⬛⬛⬛⬜⬜⬛⬜⬜⬛⬛⬛⬜⬜⬛⬜⬜⬛⬛⬛⬜⬜⬛⬜⬜⬛⬛⬛⬛⬛⬛
⬜⬛⬛⬜⬜⬜⬜⬜⬜⬛⬜⬜⬛⬛⬛⬜⬜⬛⬜⬜⬛⬛⬛⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬛
⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
⬛⬛⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬛⬛⬛⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬛⬛
⬛⬜⬜⬛⬛⬛⬛⬜⬜⬛⬜⬜⬛⬛⬛⬜⬜⬛⬜⬜⬛⬛⬛⬛⬛⬛⬜⬜⬛⬛⬛⬜⬜⬛
⬛⬜⬜⬛⬛⬛⬛⬜⬜⬛⬜⬜⬛⬛⬛⬜⬜⬛⬜⬜⬛⬛⬛⬛⬛⬛⬜⬜⬛⬛⬛⬜⬜⬛
⬛⬜⬜⬛⬛⬛⬛⬜⬜⬛⬜⬜⬜⬛⬜⬜⬜⬛⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬛⬛⬜⬜⬜⬛
⬛⬜⬜⬛⬛⬛⬛⬜⬜⬛⬛⬜⬜⬜⬜⬜⬛⬛⬜⬜⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬛⬛⬛
⬛⬜⬜⬛⬛⬛⬛⬜⬜⬛⬛⬛⬜⬜⬜⬛⬛⬛⬜⬜⬛⬛⬛⬛⬛⬛⬜⬜⬛⬜⬜⬜⬛⬛
⬛⬛⬜⬜⬜⬜⬜⬜⬛⬛⬜⬛⬛⬜⬛⬛⬜⬛⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬛⬛⬜⬜⬜⬛
⬜⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬛⬛⬛⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
