>String, StringBuilder, StringBuffer를 정리하면서 String Constant Pool 에 대해 정리하면 좋을듯 하여 이렇게 정리를 합니다.


## 😊 String Constant Pool

---

String 객체를 생성하는 방법에는 2가지 방법이 있습니다.
1. String 리터럴 객체 생성 `"" 쌍따옴표를 이용한 객체 생성 `
2. new 연산자를 통한 String 객체 생성 `new String(""")`

`리터럴 객체 생성방식`과 `new 연산자 생성방식`은 뭐가 다른걸까.

흔히 new 연산자를 통해 생성하는 객체들은 Heap Memory 영역에 저장되는것을 알고 있다.<br>
그렇다면 리터럴 객체로생성하는 String 은 Heap Memory 영역에 저장되는것이 아닌것인가??<br>
물론 두가지 방식 모두 Heap Memory 에 저장이됩니다. 다만 리터럴로 생성된 String 객체는 
Heap 영역 내의 <strong>`String Constant Pool`</strong>에 저장이 됩니다.

생성되는 그림은 다음과 같습니다.

<img src="./string_constant_pool.jpg" alt="" width="450" />

