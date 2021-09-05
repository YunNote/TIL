> 평소 Javascript 를 좋아하는 저로써 흥미로운책을 발견했습니다. Java로 치면 `Effective Java`같은 Javascript의 `자바스크팁트 코딩의 기술`이라는 책이었습니다.
> 주저 없이 구매하였고 해당 내용을 공부하면서 내용을 정리하고자 합니다.
>
> 프론트 개발 및 Javascript를 공부하신다면 한번쯤 보시는걸 꼭 추천드리고 싶습니다.
>
> 자세한 내용은 도서를 참고해 주세요

<br>

## 😊 Tip 5. 배열로 유연한 컬렉션을 생성하라.

---

배열로는 다양한 연산 및 계산등 놀라운 수준의 유연성을 가지고 있다. 예를들면 다음과 같이 말이다.

```javascript
// sort()메서드를 사용하면 기존에 있던 배열의 값에 영향을 미치기 때문에
// 펼침 연산자를 통해 새로운 배열을 만들고 정렬한 값을 리턴하도록 하였다.
const numbers = [1,5,3,6,2,0,9]

const numberSort = numbers => {
    return [...numbers].sort();
}
// 출력결과 
numberSort(numbers) //[0, 1, 2, 3, 5, 6, 9]
```

또한 map(), filter(), reduce()등과 같은 메서드를 이용하면 한 줄로 쉽게 변경하거나 갱신이 가능합니다.

```javascript
const numbers = [1,5,3,6,2,0,9]

// list에서 홀수 값들만 출력
const oddNumbers = () => {
    return numbers.filter(v => v % 2 == 1)
}
```


## 😊 Tip 6. includes()로 존재 여부를 확인하라.

---

include() 가 나오기전에 우리는 어떤 특정 값이 존재하는지를 찾기위해 indexOf를 사용해왔습니다.

indexOf()는 있다면 해당 위치를, 없다면 -1을 반환하도록 되어있죠.

코드를 보면 다음과 같이 작성할 수 있을듯 합니다.

```javascript
// 우리는 if 문 조건안에 있냐 없냐에 대한 값만 궁금할뿐이다.
// 하지만 다음 로직은 false를 반환한다. 왜냐하면 찾고자 한느 YunNote의 index 는 0이기 때문에 거짓으로 판단하기 때문이다.
const list = ["YunNote"];
const isYunNote = list => {
    if(list.indexOf("YunNote")) {
        return true
    }
    return false
}
```
그래서 다음과 같은 작업들이 항상 들어갔어야 했습니다.

```javascript
// 없는 경우 -1이기 때문에 해당 값보다 높다면 있는것으로 판정
const list = ["YunNote"];
const isYunNote = list => list.indexOf("YunNote") > -1;
```

하지만 `includes()` 메서드가 나오면서 다음과 같이 작성할 수 있습니다.

```javascript
// 없는 경우 -1이기 때문에 해당 값보다 높다면 있는것으로 판정
const list = ["YunNote"];
const isYunNote = list => list.includes("YunNote");
```

<br>

## 😊 Tip 7. 펼침 연산자로 배열은 본떠라.

---

기존에 배열을 복사하기 위해서는 다음과 같은 코드를 작성하였을것입니다.
```javascript
const names = ["YunNote", "YunJin", "YunJinNote"];
const copyNames = [];

for (let i = 0; i < names.length; i++) {
    copyNames.push(names[i]);
}
```

이럴때 펼침 연산자로 배열을 copy하게 되면 다음과 같이 작성할 수 있습니다.
```javascript
const names = ["YunNote", "YunJin", "YunJinNote"];
const copyNames = [...names];
```
딱봐도 간단하지 않은가요 ??<br> 
이와 같이 펼침연산자를 사용하게 되면 코드가 단순해지고, 코드를 읽고 이해하기 쉬워집니다.

<br>

## 😊 Tip 8. push() 메서드 대신 펼침 연산자로 원본 변경을 피하라.

---

```javascript
const names = ["YunNote", "Hello"]
names.push("World!!");

let names = ["YunNote", "Hello"]
names = [...names, "World!!"];
```

<br>

## 😊 Tip 9. 펼침 연산자로 정렬에 의한 혼란을 피하라.

---

배열에서 sort() 를 사용하는경우 원본 배열을 변경해버리는 문제(?)가 있습니다.

의도하지 않은 처리를 해버리게 되는거죠 . 그렇기 때문에 정렬을 사용할때는 펼침연산자를 통한 sort를 return 하도록 하면 좋습니다.

```javascript
// 일반 정렬방법 (원본이 변경됨)
const numbers = [9,4,5,1,2,8,0,3,6,7];
numbers.sort();

// 펼침 연산자를 사용하여 정렬한 방법
const numbers = [9,4,5,1,2,8,0,3,6,7];
[...numbers].sort();
```


---

> 펼침연산자를 너무 잘 사용하고있는 입장에서 보니 다시봐도 좋은듯합니다.
