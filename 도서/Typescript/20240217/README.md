## Typescript 2주차 스터디

---

### 2.16 함수와 메서드를 타이핑 하자

> 매개변수에 스프레드 문법, 필수값등 다양한 파라미터 설정을 통하여 기입할 수 있다.
> 
> function sample(...args: [number, number, string ]) {}
> 
> 위 와같이 작성하여 number, number, string순서로 값을 대입할 수 있으며, 매개변수 명은 임의로 정해지지만
> 지정해주고 싶다면 직접 지정 가능.
> 
> `스프레드 문법이라고 위에 선언된 갯수 이외의 값을 넣으면 에러 표시`

> 주의할점은 구조분해 할당을 적용할때는 타이핑이 헷갈리니 주의해야 한다. 
> <br>
> function sample({props: {nested}} : {props: {nested : string}) 과 같이 기입해야함.

> this사용시 명시적으로 표기해야함, 표기하지 않으면 any로 추론하고 에러 발생 this는 매개변수의 첫번째 자리에 표기하면 된다.
> 다른 매개변수들은 한자리씩 뒤로 밀린다. 타입스크립트에서 매개변수 자리에 존재하는 this는 실제 매개변수가 아니다.

---

### 2.17 같은 이름의 함수를 여러번 선언할 수 있다.

> 자바스크립트에서는 호출하는 사람 마음대로 값과 개수를 바꿔넣을 수 있다. 하지만 타입스크립트에서는 어떤
> 타입과 값이 들어올지 미리 선언해야 한다.

```typescript

function sample (a : string | number , b : string | number) {
  ...
}

sample(1,2)
sample("1","2")
sample("1",2)
sample(1,"2")
// 위와 같이 원치 않지만 호출이됨. 따라서 이럴떄 필요한것이 오버로딩이다.
```

오버로딩 - 호출할 수 있는 함수의 타입을 미리 여러 개 타이핑해두는 기법.
```typescript
function add(x:number, y:number): number
function add(x:string, y:string): string
function add(x:any, y:any) {
  return x + y;
}
```

만약 위에 선언된 선언부의 파라미터대로 들어오지 않는다면 어디에도 해당하지 않는다는 에러 발생.

주의해야할 점은 오버로딩 선언 순서가 타입 추론에 영향을 미친다. 만약 여러 오버로딩에 동시에 해당될 수 있는 경우
제일 먼저 선언된 오버로딩에 해당된다. 

추가로 함수 선언 외에도 interface 및 연산자를를 이용한 선언도 가능하다
```typescript
interface Add {
  (x: string, y: string) : string;
  (x: number, y: number) : number;
}
const add: Add = (x:any, y:any) => x + y;


type Add1 = (x: number, y: number) => number;
type Add2 = (x: string, y: string) => string;
type Add = Add1 & Add2;
const add : Add = (x: any, y: any) => x + y;

```

---

### 2.18 콜백 함수의 매개변수는 생략 가능하다.

```typescript
function sample(callback: (error: Error, result: string) => void) {}
sample((e,r) => {});
sample(() => {});
sample(() => true);
```

---

### 2.19 공변성과 반공변성을 알아야 함수끼리 대입할 수 있다.

공변성, 반공변성, 이변성, 무공변성

공변성 : A -> B 일 때 `T<A> -> T<B>`   

반공변성 : A -> B 일 때 `T<B> -> T<A>`

이변성 : A -> B 일 때 `T<A> -> T<B>` 도 되고 `T<B> -> T<A>`도 되는 경우

무공변성 A -> B 일 때 `T<A> -> T<B>` 도 안 되고 `T<B> -> T<A>`도 안 되는 경우

기본적으로 타입스크립트는 공변성을 갖고있다. 하지만 함수의 매개변수는 반공변성을 갖고 있다. 

TS Config 메뉴에서 strictFunctionTypes 옵션이 체크되어있어야 한다. strictFunctionTypes옵션은 strict 
옵션이 체크되어 있을떄 자동 활성화되고 모두 체크되어있지 않다면 매개변수에 대해 이변성을 갖는다.

```typescript
function a(x: string): number {
  return 0;
}

type B = (x: string) => number | string;
let b : B = a;

// type B가 function a보다 더 넓은 타입이기 때문에 a의 반환값을 b 에 대입할 수 있다 이 관계를
// a -> b 라고 한다. 따라서 a -> b 를 T<a> -> T<b>라고 대입하면 공변성을 갖고있다고 본다.
```

위 내용을 반대로 하면 에러가 발생한다. 따라서 반환값에 대해서는 항상 공변성을 가진다고 볼 수 있다.

매개변수의 경우는 strict 옵션에서 반공변성을 갖는다. 
```typescript
function a(x: string | number) : number {
  return 0;
}

type B = (x: string) => number;
let b: B = a;

// 매개변수는 b -> a인 상황이지만 a를 b에 대입할 수 있다. 따라서 배개변수가 반공변성을 갖고 있다고 본다.
```

---

### 2.20 클래스는 값이면서 타입이다.

```typescript

class Person {
  name;
  age;
  married;

  constructor(name: string, age: number, married: boolean) {
    this.name = name;
    this.age = age;
    this.married = married;
  }
}
// name, age, married에 타입을 생략해도 생성자를 통해 자동 추론해준다.
```

클래스표현식으로도 선언 가능 
```typescript
const Person = class {
  name;
  age;
  married;

  constructor(name: string, age: number, married: boolean) {
    this.name = name;
    this.age = age;
    this.married = married;
  }
}
```

멤버는 항상 constructor 내부와 짝이 맞아야한다.

조금 더 엄격하게 클래스의 멤버 및 메서드가 제대로 들어있는지 검사할 수 있다 interface를 사용하면 된다. 기존에 작성하던
Java와 유사해서 예제는 패스.

### private vs # 차이 
> private 는 자식 클래스에서 중복이 안되나 #을 사용하면 중복 사용 가능  private 보다는 # 선호


### 상속관계에서 메서드 오버라이드 하려면 명시적으로 override 수식어를 붙여야 한다.
> 장점은 부모 클래스의 메서드가 바뀌면 자연스럽게 하위 클래스의 메서드에서 에러 발생하여 확인하기 쉬움.

다만 확인하기 위해서는 noImplicitOverride 옵션을 직접 활성화 해줘야 한다.

---

### 2.21 enum은 자바스크립트에서도 사용할 수 있다.

> 열거형 타입은 자바스크립트에 원래 없는 타입지만 자바스크립트의 값으로 사용할 수 있는 특이한 타입이다.
> 
> 예제는 자바나 다른 언어들과 동일한 내용이라 패스하였습니다.

특징은 아래와 같다
- 기본적으로 0부터 숫자를 할당한다. 
- 0대신 다른 숫자도 할당 가능하다 만약 3으로 첫번쨰를 선언했다면 그다음에 나오는 enum의 값은 1을 더한 값이 자동으로 할당된 4를 의미하게 된다.
- 숫자대신 문자열도 할당이 가능한데 만약 문자열로 할당하였다면 이후에 나오는 값은 모두 직접 값을 할당해줘야 한다.
- enum 타입의 속성은 값으로도 활용 가능.
```typescript
enum Level {
  A,
  B,
  C
}
const a = Level.A // 0
```

---

### 2.22 infer로 타입스크립트의 추론을 직접 활용하자.

> infer 예약어는 타입스크립트의 타입 추론 기능을 극한까지 활용하는 기능이다. 

주의사항은 컨디셔널 타입에서는 타입 변수는 참 부분에서만 사용 가능. 거짓 부분에서는 사용 불가. (P.199)

---

### 2.23 타입을 좁혀 정확한 타입을 얻어내자

> 타입스크립트가 코드를 파악해서 타입을 추론하는 것을 제어 흐름 분석이라고 부른다. 다만 완벽하지는 않다는것을
> 염두해야 한다.
> 
> typeof or == 비교를 통해 비교 가능. (타입스크립트도 자바스크립트 문법을 사용한다!)
> 
> Array의 경우 Array.isArray를 사용하면 된다. 다만 비교문 순서를 조정해서도 조율 가능 ! P.208<br>
> Class는 instanceof를 통해 비교 가능 

---

### 2.24 자기 자신을 타입으로 사용하는 재귀 타입이 있다.
```typescript
type Recursive = {
  name: string;
  children: Recursive[];
}

const recursive1: Recursive = {
  name: 'test',
  children: [],
}

const recursive2: Recursive = {
  name: 'test',
  children: [
      // 자기 자신을 타입으로 다시 사용하는 것을 재귀 타입이라고 한다.
    {name: 'test1', children: []},
    {name: 'test2', children: []}
  ],
}
```

---

### 2.25 정교한 문자열 조작을 위해 템플릿 리터럴 타입을 사용하자.

P.223 참고

---

### 2.26 정교한 문자열 조작을 위해 템플릿 리터럴 타입을 사용하자.

P.226 참고

---

### 2.27 타입스크립트는 건망증이 심하다
P.231

> as 로 강제 주장한 것은 일시적이기 때문에 if문이 참인지 거짓인지를 판단할때만 주장한 타입이 사용되고 판단 후에는 원래 타입으로 돌아간다.<br>
> 계속 기억하게 만들기 위해서는 변수를 사용한다.
```typescript
try {} catch (error) {
  const err = error as Error; // 이와 같이 사용한다
  if(err) {
    err.message;
  }
}
``` 

가장 좋은 방법은 as 를 사용하지 않는것이다. 

```typescript
try {} catch (error) {
  // 아래와 같이 사용 가능 
  if(error instnaceof Error) {
    err.message;
  }
}
```

---

### 2.28 원시 자료형에도 브랜딩 기법을 사용할 수 있다.

> 해당 기법을 사용한다면 기존 원시자료형 타입에 속성을 추가할 수 있다.

```typescript
function kmToMile(km: number) {
  return km * 0.62;
}
const mile = kmToMile(3);
// 숫자 3이 km인지 m인지 확인이 어렵다. 따라서 브랜드 기법을 사용하면 아래와 같이 사용 가능하다.

type Brand<T,B> = T & { __brand: B};
type KM = Brand<number, 'km'>;
type Mile = Brand<number, 'mile'>

function kmToMile(km: KM) {
  
}
```
