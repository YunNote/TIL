
# InnoDB 스토리지 엔진 잠금

---

먼저 `InnoDB`는 MySQL의 데이터베이스 엔진입니다.


### ⭐ InnoDB 스토리지 엔진의 특징
- `InnoDB 스토리지 엔진`은 스토리지 엔진 내부에서 레코드 기반의 잠금 방식을 탑재하고 있다.
- `InnoDB 스토리지 엔진`은 레코드 기반의 잠금 방식 때문에 MyISAM보다 훨씬 뛰어난 동시성 처리를 제공한다.
하지만 이원화된 잠금처리로인해 잠금에 대한 정보를 MySQL 명령어를 통해 접근하기가 까다롭다.
  
- 구 버전 MySQL 서버에서는 InnoDB 잠금 정보를 진달할 수 있는 도구는 `lock_monitor`와 `SHOW ENGINE INNODB STATUS` 명령이 전부였으며, 이 또한 거의 어셈블리 코드를 보는 것 같아서 이해하기가 상당히 어려웠다.
- 최근 버전에서의 InnoDB는 트랜잭션과 잠금, 잠금 대기 중인 트랜잭션의 목록을 조회할 수 있는 방법이 도입되었다.
    > 조회 방법은 MySQL서버의 infomation_schema DB에 존재하는 `INNODB_TRX`, `INNODB_LOCKS`, `INNODB_LOCK_WAITS` 테이블을 조인하면 어떤 트랜잭션이 어떠한 잠금을 대기하고 있으며, 해당 잠금을 어느 트랜잭션이 가지고 있는지 확인 가능하고, 해당 잠금을 가지고있는 클라이언트를 찾아서 종료도 가능하다.
  > 
- Performance Schema를 이용하면 InnoDB스토리지 엔진의 내부 잠금에 대한 모니터링 방식도 추가되었다.
  ```sql
  select substring_index(name, '/',1) as category, count(*) from performance_schema.setup_instruments group by  substring_index(name, '/',1);
  ```
  다음과 같이 쿼리를 작성하면 대략적으로 어떠한 대분류 카테고리가 있는지 확인 할 수 있다.

---

### ⭐ InnoDB 스토리지 엔진의 잠금

InnoDB 에는 `레코드 락`뿐만 아니라 레코드와 레코드 사이의 간격을 잠그는 `갭 락`이라는것이 존재한다.

그렇다면 `레코드 락`과 `갭락 그리고 `넥스트 키 락`에대해 보겠습니다.

<br>

#### ⭐ 레코드락 (Record lock, Record only lock)
`레코드 락`이란 레코드 자체만을 잠그는 것을 의미한다. 다른 DBMS들의 `레코드 락`과 동일한 역할을 한다.<br>
다만 InnoDB의 레코드락과 다른 이유는 `InnoDB`의 `레코드 락`은 레코드 자체가 아니라 인덱스 레코드를 잠근다는 점이다.<br>

그렇다면 인덱스를 설정하지 않는다면 `레코드 락`이 동작하지 않는걸까 ??<br>
그것은 아닙니다. 인덱스가 하나도 없는 테이블이라도 내부적으로 자동 생성된 클러스터 인덱스를 이용하여 잠금을 설정한다.

> 레코드만 잠구느냐, 인덱스를 잠그느냐는 상당히 크고 중요한 차이를 만들어 내기 때문에 뒷부분에서 더 심화된 내용으로 나옴. 일다는 알고만 있자.

InnoDB 에서는 대부분 보조 인덱스를 이용한 변경 작업은 `넥스트 키 락` or `갭 락`을 사용하지만 PK or Unique Key에 대해서는 갭에 대해서는 잠그지않고 레코드 자체에 대해서만 락을 건다.

---

#### ⭐ 갭 락 (Gap lock)
`갭 락` 이란 레코드 자체가 아니라 레코드와 바로 인접한 레코드 사이의 간격만을 잠구는 것을 의미.<br>
`갭 락`의 역할은 레코드와 레코드 사이의 간격에 새로운 레코드가 생성되는 것을 제어하는 것이다. 갭락은 자체보다는 
`넥스트 키 락`의 일부로 자주 사용된다.

---

#### ⭐ 넥스트 키 락(Next key lock)
`넥스트 키 락`은 `레코드 락`과 `갭 락`을 합쳐 놓은 형태의 잠금을 의미한다.
STATEMENT 포맷의 바이너리 로그를 사용하는 MySQL 서버에서는 REPEATABLE READ 격리 수준을 사용해야 한다.

의외로 `넥스트 키 락`과 `갭 락`으로 인하여 데드락이 발생하거나 다른 트랜잭션을 기다리게 하는 일이 자주 발생한다.
따라서 간으하다면 바이너리 로그포맷을 ROW형태로 바꿔서 `넥스트 키 락`이나 `갭 락`을 줄이는것이 좋다.

---

#### ⭐ 자동 증가 락(Auto Increment lock)
MySQL에서는 자동 증가하는 숫자값을 추출하기위하여 우리가 흔히 알고 있는 `AUTO_INCREMENT` 컬럼 속성을 제공한다.

`AUTO_INCREMENT` 속성이 정의된 테이블에 여러개의 레코드가 INSERT될 경우 중복되지 않고 각 순서대로 증가하는 일련번호를 가져야하는데
이러한 경우 InnoDB 엔진에서 내부적으로 `AUTO_INCREMENT 락`이라고 하는 테이블 수준의 잠금을 사용한다.

<br>

#### 📚 자동 증가 락(Auto Increment lock) 특징 
- `AUTO_INCREMENT 락`은 INSERT와 REPLACE 쿼리 문장과 같이 새로운 레코드를 저장하는 쿼리에서만 필요하며, UPDATE나 DELETE등 쿼리에서는 걸리지 않는다.

  
- `AUTO_INCREMENT 락`은 테이블에 단 하나만 존재하기 때문에 두개 이상의 INSERT 쿼리가 동시에 실행되는 경우 하나의 쿼리가 AUTO_INCREMENT 락을 걸면
나머지 쿼리는 AUTO_INCREMENT 락을 기다려야 한다.(컬렘에 AUTO_INCREMENT 를 명시적으로 값을 설정하더라도 자동 증가락을 걸게된다.)

#### 📚 자동 증가 락(Auto Increment lock) 동작 방식의 변경

- innodb_autoinc_lock_mode=0
  > MySQL 5.0 과 동일한 잠금 방식으로 모든 INSERT 문장은 자동 증가 락을 사용한다.

- innodb_autoinc_lock_mode=1 (연속모드라고도 부름)
  > 한건 or 여러 건의 레코드를 INSERT하는 SQL중에서 MySQL 서버가 INSERT되는 레코드의 건수를 정확히 예측할 수 있을 경우에는 자동
  > 증가 락을 사용하지 않고, 훤씬 가볍고 빠른 래치를 이용해 처리한다.<br>
  > 개선된 래치는 자동 증가 락과 달리 아주 짧은 시간 동안만 잠금을 걸고 필요한 자동 증가 값을가져오면 즉시 잠금이 해제된다.<br>
  > 레코드의 건수를 정확히 예측할 수 없는 경우에는 자동 증가 락을 사용한다.

- innodb_autoinc_lock_mode=2
  > 절대 자동 증가 락을 걸지 않고 경량화된 래치를 사용한다. 다만 이 설정에서는 하나의 INSERT문장으로 INSERT되는 레코드라고 하더라도 연속된 자동 증가 값을 보장하지 않는다.
  > 동시에 다른 커넥션에서도 INSERT를 수행할 수 있으므로 동시 처리성능은 높아진다. 다만 바이너리 로그를 사용하는 복제에서는 소스 서버와 레플리카 서버의 자동 증가 값이 달라질 수도 있기 때문에 주의해야 한다.
  
> MySQL 5.7 버전까지는 default 값이 1이었지만 MySQL8.0 부터는 default 값이 2로 변경되었으며, 바이너리 로그 포맷이 STATEMENT -> ROW로 변경되었다.
> 따라서 STATEMENT 포맷의 바이너리 로그를 사용한다면 innodb_autoinc_lock_mode를 1로 변경해서 사용할 것을 권장한다고 한다.

---


### ⭐ 인덱스와 잠금
InnoDB의 잠금과 인덱스는 상당히 중요한 연관 관계가 있다.
```sql
-- users라는 Table에 last_name 컬럼만 인덱스가 걸려있다고 가정하겠습니다.
SELECT COUNT(*) FROM users WHERE last_name = 'Choi';
+------+
|  100 |
+------+

SELECT COUNT(*) FROM users WHERE last_name='Choi' AND first_name='YunJin';
+------+
|    1 |
+------+

UPDATE users SET updatedAt=NOW() where last_name='Choi' AND first_name='YunJin';
```

위의 SQL을 실행하면 1건의 레코드의 업데이트가 발생하게 된다. 하지만 이 한건의 레코드를 업데이트 하기 위해서는 
총 100건의 데이터가 잠기게 된다. 왜냐하면 `first_name`은 인덱스로 잡혀있지 않기 때문이다. 

그렇다면 함께 변경되는 조건에 대하여 인덱스가 같이 걸려있어야 하는것 같다...

> 만약 해당 테이블에 인덱스가 하나도 없다면, 테이블을 풀 스캔하면서 UPDATE작업을 하게되어 모든 레코드를 잠구게 된다.

---

### ⭐ 레코드 수준의 잠금 확인 및 해제

`테이블 레코드 수준` 잠금은 `테이블 수준`의 잠금보다 조금 더 복잡하다.

`테이블 잠금`에서는 잠금의 대상이 테이블 자체이기 대문에 문제의 원인이 쉽게 발견되고 해결이 될 수 있다.<br>
하지만 `테이블 레코드 수준의 잠금`에서는 테이블의 레코드 각각에 잠금이 걸리기 떄문에 해당 레코드가 자주 사용되지 않는다면 오랜시간동안 
잠금상태로 남아있어도 쉽게 발견되지 않는다.

MySQL5.1 이전에는 레코드 잠금에 대한 메타정보를 제공하지 않아 더더욱 어려웠지만 해당 버전 이후로는 `레코드 잠금`과 `레코드 잠금 대기`
에 대한 조회가 가능하기 때문에 쿼리만 실행해 보면 `잠금`과 `잠금 대기`를 바로 확인할 수 있다.


확인하는 방법은 MySQL 5.1부터 infomation_schema DB에 `INNODB_TRX`, `INNODB_LOCKS`, `INNODB_LOCK_WAITS`테이블을 통해 확인 가능.

> MySQL 8.0버전 부터는 `information_schema` -> `performance_schema`의 data_locks, data_lock_waits테이블로 대체 되는중

> 쿼리를 작성하여 확인해보고 싶지만.. 도서의 이미지로 대체 ...

---

## ⭐ MySQL의 격리 수준

트랜잭션의 격리 수준(Isolation Level) 이란 여러 트랜잭션이 동시에 처리될 때 특정 트랜잭션이 다른 트랜잭션에서 변경하거나 조회하는 
데이터를 볼 수 있게 허용할지 말지를 결정하는 것이다.

격리 수준에는 크게 `READ UNCOMMITTED`, `READ COMMITTED`, `REPEATABLE READ`, `SERIALIZABLE`의 4가지 로 나뉜다.

### ⭐ READ UNCOMMITTED
트랜잭션에서의 변경 내용이 COMMIT 이나 ROLLBACK 여부와 상관없이 다른 트랜잭션에서 보인다.

`READ UNCOMMITTED`에서 제일 중요한 내용은 트랜잭션에서 처리한 작업이 완료되지도 않았는데 다른 트랜잭션에서 볼 수 있는 현상을
`더티 리드(Dirty Read)`라고 하고 더티 리드가 허용되는 격리 수준이 `READ UNCOMMITTED` 이다.

`READ UNCOMMITTED`는 RDBMS 표준에서는 트랜잭션의 격리 수준으로 인정하지 않을 정도로 정합성에 문제가 많은 격리 수준이다.
따라서 MySQL을사용한다면 최소한 READ COMMITTED 이상의 격리 수준을 사용할 것을 권장한다.

---

### ⭐ READ COMMITTED

`READ COMMITTED`는 어떤 트랜잭션에서 변경한 내용이 커밋되기 전까지는 다른 트랜잭션에서 그러한 변경 내역을 조회할 수 없다.

`READ COMMITTED`는 오라클 DBMS에서 가장 기본으로 사용되는 격리 수준이며, 온라인 서비스에서 가장 많이 선택되는 격리 수준이다.

`READ COMMITTED`에서는 `더티 리드(Dirty Read)`와 같은 현상을 발생하지 않는다. 이 말은 즉 어떤 트랜잭션에서 데이터를
변경했더라도 COMMIT 이 완료된 데이터만 다른 트랜잭션에서 조회가 가능하다.