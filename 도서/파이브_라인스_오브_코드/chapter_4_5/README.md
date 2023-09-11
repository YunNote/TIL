## 4. 타입 코드 처리하기


### 규칙 : if 에서 else를 사용하지 말것

정의 - 프로그램에서 이해하지 못하는 타입인지를 검사하지 않는 한 if 문에서 else를 사용하지 마라.

if-else를 사용하면 코드에서 결정이 내려지는 지즘을 고정하게 된다. 그럴 경우 if-else가 있는
위치 이후에서는 다른 변형을 도입할 수 없기 때문에 코드의 유연성이 떨어지게 된다.

결과적으로 `if-else`는 하드코딩된 결정으로 볼 수 있다. 코딩에서 하드코딩된 상수가 좋지 않은것처럼
하드코딩된 결정또한 좋지 않다.

이러한 상황으로 보면 하드코딩은 하지 않는것이 좋은데, `if`와 함께 `else`를 함께 사용하지 않는것이다.

주로 코드작성시 독립된 if문은 검사로 간주하고, if-else문은 의사결정으로 간주한다.

우리는 구현을 알기 때문에 아래 코드가 이해가 되지만 사용자에게는 도움이 되지 않아 다음과 같이 이해할 수 있는
오류를 발생시킨다.

```typescript
// 변경 전
function average(ar: number[]) {
  if(size(ar) === 0) {
    throw "Empty array not allowed";
  }else {
    return sum(ar) / size(ar);
  }
}
```

```typescript
// 변경 후 
function assertNotEmpty(ar: number[]) {
  if(siez(ar) === 0) {
    throw "Empty array not allowed";
  }
}

function average(ar: number[]) {
  assertNotEmpty(ar);
  return sum(ar) / size(ar);
}

```

---

#### 스멜 

해당 규칙은 스멜로 인식되는 `이른 바인딩(early binding)`과 관련 있다.
프로그램을 컴파일할 때 `if-else`같은 의사결정 동작은 컴파일 시 처리되어 애플리케이션에 고정되며 재컴파일 없이는
수정할 수 없다. `이른 바인딩(early binding)`의 반대는 코드가 실행되는 순간에 동작이 결정되는 `늦은 바인딩(late binding)`이다.

이른 바인딩은 if문을 수정해야 변경할 수 있기 때문에 추가에 의한 변경을 방해한다. 늦은 바인딩은 추가를 통한
변경을 가능하게 한다.

---

#### 의도

