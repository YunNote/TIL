## 옵저버 패턴 (Observer Pattern)

---

### 👉 Observer Pattern 정의
> 한 객체의 상태그 바뀌면 해당 객체에 의존하는 다른 객체들에게 변경사항에 대해 알려주고, 자동으로 내용이 갱신되는 방식으로 1:N의 의존성을 정의한다.

그렇다면 실생활에서 옵저버 패턴이 사용되고 있는데, 예를 들어 간단하게 설명해보겠습니다.

우리가 항상 보는 Youtube의 채널같은경우 <span style="font-size:16px; font-weight:600;">구독</span>을 하게되면 해당 채널에 새로운 영상 또는 글이 
게시되었을때 해당 채널을 구독하고있는 구독자들에게 알림이 가게 됩니다.

옵저버 패턴(Observer Pattern)에서는 <span style="font-size:16px; font-weight:600;">주제(subject)</span>와
<span style="font-size:16px; font-weight:600;">옵저버(observer)</span> 라고 부릅니다

<hr>

### 👉 Observer Pattern의 특징
 - Observer Pattern의 1:N 관계는 주제(subject) 와 옵저버(observer)에 의해 결정된다.
 - 옵저버(observer)는 주제에 의존한다. 주제(subject)의 상태가 변경이 되면 옵저버(observer)에게 연락이 간다.

<hr> 

### 👉 Observer Pattern의 장,단점

#### 장점
 - 실시간으로 한 객체의 변경사항을 다른 객체에 전파할 수 있다.
 - 느슨한 결합으로 시스템이 유연하고 객체간의 의존성을 제거할 수 있다.
    > 느슨한 결합이란 상호작용을 하지만 서로에 대해 서로 잘 모른다는 의미.

#### 단점
 - 너무 많이 사용하게 되면, 상태관리가 힘들어 질 수 있다.
 - 데이터 배분에 문제가 생기게 된다면 큰 문제로 이어질 수 있다 .

<hr>

### 👉 Observer Pattern 의 사용 예

사용예시는 무조건 맞다가 아니라 대략적으로 이러한 느낌을 가지고 있다고 보시면됩니다.

```java
// 주제를 의미하는 Class
package observer;

import java.sql.Array;
import java.util.ArrayList;
import java.util.List;

/**
 * <pre>
 * observer
 *      YouTubeNotice
 * </pre>
 *
 * @author YunJin Choi(zzdd1558@gmail.com)
 * @since 2021-08-18 오전 2:12
 */

public class YouTubeChannel {

   private String channelName;
   private List<YouTubeSubscriber> subscribers = new ArrayList<>();

   public YouTubeChannel(String channelName) {
      this.channelName = channelName;
   }

   public void subscribe(YouTubeSubscriber subscriber) {
      System.out.println(String.format("%s 유저가 %s 채널을 구독하기 시작했습니다.",subscriber.nickname(), channelName ));
      this.subscribers.add(subscriber);
   }

   public void unsubscribe(YouTubeSubscriber subscriber) {
      System.out.println(String.format("%s 유저가 %s 채널을 구독 취소 하였습니다.",subscriber.nickname(), channelName ));
      this.subscribers.remove(subscriber);
   }

   public void notifySubscribers(String title) {
      subscribers.stream().forEach(v -> {
         v.videoNotifications(channelName, title);
      });
   }
}
```

```java
// 옵저버(observer) 를 의미하는 abstract class 
package observer;

/**
 * <pre>
 * observer
 *      YouTubeSubscriber
 * </pre>
 *
 * @author YunJin Choi(zzdd1558@gmail.com)
 * @since 2021-08-18 오전 2:13
 */

public abstract class YouTubeSubscriber {

   public abstract String nickname();
   public void videoNotifications(String channel, String title) {
      System.out.println("-- 알림 -- ");
      System.out.println(String.format("%s님이 구독중인 채널 '%s' 에 새로운 영상 '%s' 가 추가되었습니다",nickname(), channel, title));
      System.out.println("-----------");
   }
}
```

```java
// 옵저버(observer)를 구현한 User class

package observer;

/**
 * <pre>
 * observer
 *      YoutubeUser
 * </pre>
 *
 * @author YunJin Choi(zzdd1558@gmail.com)
 * @since 2021-08-18 오전 2:16
 */

public class YouTubeUser extends  YouTubeSubscriber{

    private String nickname;

    public YouTubeUser(String nickname) {
        this.nickname = nickname;
    }

    @Override
    public String nickname() {
        return this.nickname;
    }
}

```


```java
// Main Class 
package observer;

/**
 * <pre>
 * observer
 *      YouTube
 * </pre>
 *
 * @author YunJin Choi(zzdd1558@gmail.com)
 * @since 2021-08-18 오전 2:28
 */

public class YouTube {
   public static void main(String[] args) {

      YouTubeChannel channel = new YouTubeChannel("YunNote Channel");


      YouTubeSubscriber user1 = new YouTubeUser("최윤진");
      YouTubeSubscriber user2 = new YouTubeUser("Yundle Yundle");

      channel.subscribe(user1);
      channel.subscribe(user2);

      channel.notifySubscribers(" 매트릭스 1");

      channel.unsubscribe(user1);

      channel.notifySubscribers(" 매트릭스 2");
   }
}

// 실행 결과

최윤진 유저가 YunNote Channel 채널을 구독하기 시작했습니다.
Yundle Yundle 유저가 YunNote Channel 채널을 구독하기 시작했습니다.
        
-- 알림 --
최윤진님이 구독중인 채널 'YunNote Channel' 에 새로운 영상 ' 매트릭스 1' 가 추가되었습니다
-----------
        
-- 알림 --
Yundle Yundle님이 구독중인 채널 'YunNote Channel' 에 새로운 영상 ' 매트릭스 1' 가 추가되었습니다
-----------
        
최윤진 유저가 YunNote Channel 채널을 구독 취소 하였습니다.
        
-- 알림 --
Yundle Yundle님이 구독중인 채널 'YunNote Channel' 에 새로운 영상 ' 매트릭스 2' 가 추가되었습니다
-----------
```


