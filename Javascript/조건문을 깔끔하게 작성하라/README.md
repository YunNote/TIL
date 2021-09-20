> 평소 Javascript 를 좋아하는 저로써 흥미로운책을 발견했습니다. Java로 치면 `Effective Java`같은 Javascript의 `자바스크팁트 코딩의 기술`이라는 책이었습니다.
> 주저 없이 구매하였고 해당 내용을 공부하면서 내용을 정리하고자 합니다.
>
> 프론트 개발 및 Javascript를 공부하신다면 한번쯤 보시는걸 꼭 추천드리고 싶습니다.
>
> 자세한 내용은 도서를 참고해 주세요
>


## 😊 Tip 17. 거짓 값이 있는 조건물을 축약하라.

---

Javascript 에서 false 값의 목록은 다음과 같습니다.

 - `false`
 - `null`
 - `0`
 - `Nan(숫자가 아님)`
 - `''`
 - `""`

true, false에 관심을 가져야 하는 이유는 긴 표현식을 짧게 축약할 수 있기 때문이다. 

```javascript
const employee = {
    name: 'YunNote',
    equipmentTraining: ''
}

// 틀린 코드
// if(employee.equipmentTraining.length == 0) {
//     return "작동 권한 없어요 ..."
// }

if(!employee.equipmentTraining) {
    return "작동 권한 없어요 ..."
}
```

위와 같은 코드를 보면 문제없이 false를 출력하여 제대로 동작하는것처럼 보일 수 있지만. 
해당 코드는 equipmentTraining에 'YunNote'라고 집어넣고 코드를 돌리게 된다면. 정상적으로 코드가 동작하지 않을 것이다.

따라서 strict equivalency를 이용하여 값이 있는지, 원하는 형식인지 엄격하게 확인하는것이 좋습니다.

<br>


## 😊 Tip 18. 삼항 연산자로 빠르게 데이터를 확인하라.

---
저는 처음에 삼항연산자를 제대로 쓰지 못하였을때 다음과 같이 코딩을 했습니다.
```javascript
function isChecked() {
    let check;
    if(isTrue) {
        check = true;
    }else {
        check = false;
    }
    
    return check;
}
```

삼항연산자를 학습한후 다음과 같은 코드로 간편하게 짤 수 있었습니다.
```javascript
function isChecked() {
    return isTrue ? true : false;
}
```
삼항연산자는 어떻게 사용하느냐에 따라 장점과 단점이 있는듯 하다.
조건이 2개 이상인 경우는 어떻게 표현하는게 더 깔금해 보이나요 ?

```javascript
const permission = rank == 'diamond' ? "다이아" : rank == 'platinum' ? '플래티넘' : '나머지'

// vs

function permission ({rank}) {
    if(rank =='diamond') {
        return '다이아몬드'
    }else if(rank == 'platinum') {
        return '플래티넘'
    }else {
        return '나머지'
    }
}
```
삼항연산자를 쓰면 훨씬 깔끔하고 예측 가능하도록 짤수 있지만 다음과 같이 과도하면 오히려 더 보기 힘들어지는 문제가 생깁니다.

<br>


## 😊 Tip 19. 단락 평가를 이용해 효율성을 극대화하라.

---

`단락 평가(short circulting)`

