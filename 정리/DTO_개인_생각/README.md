> 어느 한 면접에서 다음과 같은 질문을 받았다.<br>
>
> 🧑 면접관 A : `메서드에 파라미터가 많아질경우  클래스를 이용하여 분리하기도 하는데 이렇게 하는 이유가 뭘까요 ?`
> 
> 💻 나 : `여러개의 파라미터중 서로 연관이 있거나 의미있는 파라미터끼리 묶어서 클래스로 묶어서 사용 한 경험이 있다. 
> 그렇게 한 이유는 연관된 파라미터끼리는 어떠한 로직 또는 계산이 들어갈 수 있다.
> 즉 행위를 가져갈 수 있습니다.
> 따라서 다양한 API의 비지니스 로직에서 사용될 수 있는데 이렇게 DTO가 행위를 가져가게 된다면 
> 중복되는 내용을 방지 할 수 있을듯하다. 또한 클래스 자체의 이름으로 어떠한 객체인지도 쉽게 파악이 가능하다.`


저는 위와 같이 답변을 드렸습니다. 그렇다면 어떠한 경우 이러한 일이 발생할수 있는지 간단하게 소스코드로 확인해볼까 합니다 .

지금 나오는 예제는 대략적인 느낌을 주기위해 살짝 억지로 만들어낸 예제라는 것을 알아주시면 감사하겠습니다.

```java
// 해당 API는 Image의 width와 height값을 통해 Ratio를 구하는 로직이라고 가정하겠습니다.
// 또한 생성과 수정로직에 해당 로직이 실행된다고 가정합니다.
// 다음과 같은 소스가 생성될 것입니다.

public void createImage(int width, int height, ...) {
    double ratio = width / height;
    ...
}

public void updateImage(int width, int height, ...) {
    double ratio = width / height;
    ...
}

// 그런데 갑자기 
// 👨 : Ratio는 기존 Ratio에 2배로 저장시켜주세요  (억지)

// 💻(개발자) : 아 어디어디 수정해야하는거지 찾아봐야겠다...
 ```
<img src="./one_hour_later.jpg" alt="" width="640" />


```java
// 💻(개발자) : 수정 다했습니다. 배포할꼐요 
// create 할때만 ratio를 계산하는줄 알고 createImage만 수정해버린 개발자...
// 당연히 이렇게 된다면 updateImage를 할때 잘못된 ratio 계산이 들어가게 될것입니다.
public void createImage(int width, int height, ...) {
    double ratio = (width / height) * 2;
    ...
}

public void updateImage(int width, int height, ...) {
    double ratio = width / height;
    ...
}
```

위와 같은 상황이 발생이 안할것 같지만 실제로 저도 이러한 경험이 있습니다 ...

또한 해당 메서드가 Image의 Width와 Height라는것을 모르는 사람이라면 당연히 어떤 값인지 한번 생각하게 될것입니다.

이럴때 DTO를 사용하게 되면 어떻게 되는지 사용해보겠습니다.

```java

// 이미지의 정보를 가지고 있는 class 
class ImageInfo {
    private int width;
    private int height;
    
    public double ratio() {
        return width / height;
    }
}


public void createImage(ImageInfo image ...) {
    double ratio = image.ratio();
    ...
}

public void updateImage(ImqgeInfo image, ...) {
    double ratio = image.ratio();
    ...
}
```

```java
// 👨 : Ratio는 기존 Ratio에 2배로 저장시켜주세요  (억지)
```

위와 같이 DTO 를 생성하여 사용하면 ImageInfo자체가 ratio를 계산하는 행위 자체를 가져가게 된다. 
만약 위와 같은 코드에서 다음과 같은 요청이 다시 왔을때는 ImageInfo Class의 ratio()메서드만 수정하면 되는것이다. 
이렇게 된다면 기존에 image.ratio()를 사용하는 곳은 변경이 일어나지 않게 되는 것이기도 하다.

---

### 개인적인 생각

위의 내용처럼 우리가 흔히 부르는 DTO or VO를 사용하였을때 위와 같은 이점도 있을것이고, 파라미터를 클래스로 만들었을때 해당 파라미터가 무엇을하는, 또는 어떤 기능을 하는 
파라미터인지 `이름`을통해서도 쉽게 파악할 수 있을것 같다.

해당 면접질문에 대해 다시한번 고민할 수 있는 시간을 가져보니 DTO를 사용하는 이유에 대해 다시한번 생각해볼 수 있어서 좋았던 경험인듯 하다.



