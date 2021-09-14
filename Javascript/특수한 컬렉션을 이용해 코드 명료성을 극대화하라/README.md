> 평소 Javascript 를 좋아하는 저로써 흥미로운책을 발견했습니다. Java로 치면 `Effective Java`같은 Javascript의 `자바스크팁트 코딩의 기술`이라는 책이었습니다.
> 주저 없이 구매하였고 해당 내용을 공부하면서 내용을 정리하고자 합니다.
>
> 프론트 개발 및 Javascript를 공부하신다면 한번쯤 보시는걸 꼭 추천드리고 싶습니다.
>
> 자세한 내용은 도서를 참고해 주세요
>


## 😊 Tip 10. 객체를 이용하여 정적인 키값을 탐색하라

---
우리는 배열을 이용하여 다음과 같은 값을 만들 수 있습니다.

```javascript
const colors = ["#FFFFFF", "#000000", "#FF00000"];
```
무슨색인지 아시나요 ? (물론 간단한 값이라 알수 도있다..)

해당 값은 흰색, 검정색, 빨간색을 의미합니다. 바로 알 수 있는 이유는 너무 많이 본 컬러값들이라 그렇지만 처음 접하는 사람들은
해당 값이 무슨색을 의미하는지 알 수 없다.

이럴경우 키-값을 통하여 간단하게 표현 할 수 있습니다.

```javascript
const colors = {
    white : "#FFFFFF",
    black : "#000000",
    red : "#FF00000",
};
```

다음과 같이표현하면 처음 보는 개발자도 해당 Hex값이 어떠한 색상을 의미하는지 유추할 수 있습니다.

마치 `colors.white` or `color["white"]` 처럼 접근할 수 있습니다. 

더 자세한 내용은 뒤의 Tip에서 확인할 수 있다.

<br>

## 😊 Tip 11. Object.assign()으로 조작 없이 객체를 생성하라.

```javascript
// default에 입력받은 info 추가하기  
const defaultInfo = {
    name : "",
    age: 0,
    address : ""
}

const myInfo = {
    name: "최윤진",
    age: 29
}

const addInfo = (defaultInfo , myInfo) => {
    const keys = Object.keys(defaultInfo);
    const updateInfo = {};
    
    for (let i = 0; i< keys.length; i++) {
        updateInfo[keys] = myInfo[keys] || defaultInfo[keys];
    }
    return updateInfo;
}
```
나 또한 Object.assign() 알기 전까지 위와 같이 복사를 했습니다.

하지만 Object.assign()을 활용하면 쉽게 할 수 있습니다 한번 볼까요 

```javascript
const defaultInfo = {
    name : "",
    age: 0,
    address : ""
}

const myInfo = {
    name: "최윤진",
    age: 29
}

Object.assign(defaultInfo, myInfo);
```

Object.assign 을 사용하면서 코드를 한줄로 간단하게 작성도 할 수 있었습니다. 하지만 위의 코드는 defaultInfo 객체 자체를 변경해버리기 때문에
기존의 defaultInfo 는 더이상 사용할 수 없습니다.

따라서 다음과 같이 사용한다면 원본 객체가 변경되는 걱정 없이 사용할 수 있습니다. 

```javascript
Object.assign({}, defaultInfo, myInfo);
```

---

### ⭐ 주의사항
deep copy 또는 deep merge는 되지 않습니다. 따라서 `deep copy` or `deep merge`를 사용하기 위해서는 코드를 좀 더 추가하여 Object.assign()를 더 잘 활용하면 됩니다.

아니면 `Lodash` 라이브러리를 사용하면 쉽게 해결 할 수 있습니다.

<hr>

## 😊 Tip 12. 객체 펼침 연산자 (Spread Operator)로 정보를 갱신하라. 

`객체 펼침 연산자(Spread Operator)`에서는 서로 다른 값을 추가하면 가장 마지막에 선언된 값을 사용한다.
```javascript
const defaultInfo = {
    name : "",
    age: 0,
    address : ""
}

const myInfo = {
    name: "최윤진",
    age: 29
}

console.log({...defaultInfo, ...myInfo})
// 실행 결과
// {name: "최윤진", age: 29, address: ""}
```

Object.assign()을 이용하는것과 비슷하다고 보면된다. 하지만 `객체 펼침 연산자(Spread Operator)`도 역시 deep copy, deep merge를 지원하지는 않는다.

하지만 매우 편하게 사용할수 있으며 `React`에서도 많이 사용하니 알아두면 좋을듯 합니다.

<hr>

## 😊 Tip 13. 맵으로 명확하게 Key-Value 데이터를 갱신하라

Javascript에서 Map을 사용하면 Key-Value를 명확하게 사용할 수 있다.<br>
다음 예제처럼 사용할 수 있다.
```javascript
let myInfo = new Map()
myInfo.set("name", "최 윤진")
myInfo.set("age", "29")

// 출력 결과 Map(2) {"name" => "최 윤진", "age" => "29"}
console.log(myInfo)
```

Map()을 사용하기 위해서는 기본적으로 다음 메서드를 사용할 수 있다.
 - `get(key)` - `myInfo.get("name");` myInfo에서 Key가 name인 Value를 가져온다.
 - `set(key,value)` - `myInfo.set("address", "서울시 관악구");` Key가 address이고 Value가 "서울시 관악구"인 값을 등록
 - `delete(key)` - `myInfo.delete("name");` myInfo에서 Key가 name인 Key-Value쌍을 제거한다.   
 - `clear()` - `myInfo.clear()` 모든 Key-Value 쌍을 제거.


### 개인적으로 생각하는 Map의 장점 
```javascript
const status = {
    200 : "정상"
}
status.200 // 접근 불가
status[200] // 접근 가능, 하지만 실제로 200이라는 값은 문자열로 변환되어있음
Object.keys(status) // ['200'] 반환한다.
```

하지만 Map을 사용하면 배열을 반환하지 않는다. 반환된 값은 맵이터레이터라고 부릅니다.

```javascript
const status = new Map().set(200, "정상")
status.get(200);
Object.keys(status) // {200} 반환.
```

## 😊 Tip 14. 맵과 펼침 연산자로 Key-Value 데이터를 순회하라

```javascript
const status = new Map()
    .set(200, "OK")
    .set(404, "Page Not Found")
    .set(500, "Server Error")

[...status].map( ([key,value]) => `${key} :: ${value}`)
```

Map과 펼침 연산자를 이용하면 다양한 방식으로 코드를 작성할 수 있다.

해당 Tip은 따로 깊게 정리하지 않았습니다.

<hr>

## 😊 Tip 15. 맵 생성 시 부수 효과를 피하라

Map 또한 `Spread Operator`, `객체`와 마찬가지로 동일한 Key값에 대해서 값은 마지막으로 선언한 값을 사용하게 된다.

하지만 걱정할 것은 없는것 같다. `Spread Operator` 를 통하여 해당 내용을 합칠 수 있다.

```javascript
const before = {
    name : "최 윤진"
}

const after = {
    name: "YunNote"
}

const newMap = new Map([...before, ...after])
newMap.get("name") // YunNote 출력 
```

`Spread Operator` 만 잘 이용하면 코드를 간편하게 작성할 수 있다.

<hr>

## 😊 Tip 16. Set 을 이용하여 고윳값을 관리하라.

배열에서 중복값을 제거하고 싶을 경우 코드를 어떻게 짜야했을까요 

```javascript
// numbers의 배열안에서 중복 숫자를 버리고 고유 숫자만 출력
const numbers = [1,3,2,5,3,4,2,1,2,3,1,4,2,3,5,1,5];
const unique = numbers => {
    const copy = [...numbers];
    const uniques = [];
    copy.map(v => {
        if(!uniques.includes(v)) {
            uniques.push(v)
        }
    })
    return uniques;
}

// Set을 사용하면 다음과 같이 변경 가능
const unique = numbers => new Set([...numbers])
```
단 한줄로 작성이 가능하다. Set을 사용하여 중복을 제거하는 내용은 저도 이책을 보면서 처음 알았습니다.

앞으로는 Set과 Map을 더 잘 사용하면 깔끔한 코드를 짤 수 있을듯합니다.