## 😊 쿼리 작성과 연관된 시스템 변수

대 소문자 구분, 문자열 표기 방법 등과 같은 SQL 작성 규칙은 MySQL 서버의 시스템 설정에 따라 달라진다

### 📚 SQL 모드

MySQL 서버의 sql_mode라는 시스템 설정에는 여러 개의 값이 동시에 설정될 수 있다.<br>
MySQL 서버의 설정 파일에서 sql_mode를 설정할 때는 구분자(,)를 사용하여 키워드를 동시에 설정할 수 있다.

#### - STRICT_ALL_TABLES & STRICT_TRANS_TABLES

> MySQL 서버에서 INSERT나 UPDATE 문장으로 데이터를 변경하는 경우 컬럼의 타입과 저장되는 값의
> 타입이 다를 때 자동으로 타입 변경을 수행한다. 만약 적절하게 변환되기 어렵거나 컬럼에 저장될 값이 없거나, 값의
> 길이가 컬럼의 최대 길이보다 큰 경우 MySQL 서버가 INSERT나 UPDATE문장을 계속 실행할지, 아니면 에러를 발생시킬지를 결정한다.

#### - ANSI_QUOTES

> MySQL에서는 문자열값을 표현하기 위해 홑따옴표와 쌍따옴표를 동시에 사용할 수 있다.<br>
> ANSI_QUOTES 설정을 하면 문자열 값 표기로 홑따옴표만 사용할 수 있고, 쌍따옴표로는 컬럼명이나 테이블 명과 같은 식별자를 표기하는 데만 사용할 수 있다.

#### - ONLY_FULL_GROUP_BY

> GROUP BY 절에 포함되지 않는 컬럼이더라도 집합 함수의 사용 없이 그대로 SELECT 절이나 HAVING절에 사용할수 있지만. 해당 설정을 통해 문법에 조금 더 엄격한 규칙을 적용한다.<br>
> MySQL 5.7에서는 해당 옵션이 기본적으로 비활성화 되어있지만 8.0이상부터는 기본적으로 활성화 되어있다.

#### - PIPE_AS_CONCAT

> `||`는 or 연산자와 같은 의미로 사용된다. 하지만 sql_mode 시스템 변수에서 해당 값을 설정하면 오라클과 같이 문자열 연견 연산자로 사용할 수 있다.

#### - PAD_CHAR_TO_FULL_LENGTH

> CHAR타입이더라도 문자열을 가져올때 뒤의 공백 문자는 제거되어 반환된다. 하지만 CHAR타입의 컬럼값을 가져올 때 뒤쪽의 공백이
> 제거되지 않고 반환돼야 한다면 sql_mode 시스템 설정에 `PAD_CHAR_TO_FULL_LENGTH`를 추가하게 되면 공백을 포함해서 가져온다.

#### - NO_BACKSLASH_ESCAPES

> 역슬래시 문자를 이스케이프 문자로 사용할 수 있다. sql_mode 시스템 설정에 NO_BACKSLASH_ESCAPES를 추가하면 역슬래시를 문자의 이스케이프
> 용도로 사용하지 못한다.

#### - IGNORE_SPACE

> 스토어 프로시저나 함수의 이름 뒤에 공백이 딨다면 `스토어드 프로시저나 함수가 없습니다` 라는 에러가 출력될 수도 있다.<br>
> sql_mode 시스템 변수에 `IGNORE_SPACE`를 추가하면 프로시저나 함수명과 괄호 사이의 공백은 무시한다.

#### - REAL_AS_FLOAT

> 서버에서 부동 소수점 타입은 FLOAT과 DOUBLE 타입이 지원이 된다, REAL타입은 DOUBLE타입의 동의어로 사용된다.
> 하지만 해당 옵션을 활성화하게 되면 MySQL 서버는 REAL이라는 타입이 FLOAT타입의 동의어로 바뀐다.

#### - NO_ZERO_IN_DATE & NO_ZERO_DATE

> 해당 두 옵션이 활성화 되면 MySQL 서버는 DATE 또는 DATETIME 타입의 컬럼에 "2020-00-00" or "0000-00-00"과 같은
> 잘못된 날짜를 저장하는 것이 불가능해진다.<br>
> 이처럼 실제 존재하지 않는 날짜를 저장하지 못하게 하려면 해당 옵션을 활성화하면된다.

#### - ANSI

> 해당 설정은 여러가지 옵션을 조합하여 MySQL 서버가 최대한 SQL 표준에 맞게 동작하게 만들어준다.<br>
> ANSI모드는 "REAL_AS_FLOAT,PIPES_AS_CONCAT,ANSI_QUOTES"와 같은 조합으로 구성된 모드이다.

#### - TRADITIONAL

> STRICT_TRANS_TABLES나 STRICT_ALL_TABLES와 비슷하지만 조금 더 엄격한 방법으로 SQL의 작동을 제어한다.<br>
> `TRADITIONAL`모드는 `STRICT_TRANS_TABLES,STRICT_ALL_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION`모드의 조합으로 구성된 모드이다.<br>
> 해당모드가 활성화되면 활성 모드가 아닐 때 경고로 처리되던 상황이 모두 에러로 변경되고 SQL문이 실패한다.

---

### 📚 영문 대소문자 구분

MySQL 서버는 설치된 운영체제에 따라 테이블명의 대소문자를 구분한다. DB나 테이블이 디스크의 디렉터리나 파일로 매핑되기 떄문이다.

> #### 윈도우</b> - 대소문자를 구분하지 않는다.<br>
>#### 유닉스 계열 - 대소문자를 구분한다.

윈도우에서 운영되는 MySQL 데이터를 리눅스로 가져오거나 그 반대의 경우 문제가 되기도 한다.<br>
따라서 대 소문자 구분의 영향을 받지 않게 하려면 MySQL 서버의 설정 파일에 `lower_case_table_names` 시스템 변수를 설정하면 된다.

해당 변수르 1로 설정하면 모두 소문자로만 저장 되고, MySQL 서버가 대소문자를 구분하지 않게 해준다.<br>
해당 설정의 기본값은 0으로, DB나 테이블명에 대해 대소문자를 구분한다.<br>

또한 윈도우와 macOS에서는 2를 설정할 수도 있는데. 해당 경우에는 대소문자를 구분하지만 쿼리에서는 대소문자를 구분하지 않게 해준다.<br>
이러한 설정 자체를 떠나 가능하면 초기 DB나 테이블을 생성할 때 대문자 또는 소문자만으로 통일해서 사용하는것이 좋다.


---

### 📚 MySQL 예약어

생성하는 테이블,컬럼의 이름을 예약어와 같은 키워드로 생성해야 한다면 항상 역따옴표(`)로 감싸서 사용해야한다.<br>
해당 책에서는 테이블의 생성 또는 컬럼명을 작성할때 항상 역따옴표로 테이블이나 칼럼의 이름을 둘러싸지 않은 상태로 생성하길 권장한다.<br>
그래야만 해당 단어가 예약어인지 아닌지를 MySQL 서버가 에러로 알려주기 때문이다. 만약 테이블 생성이 실패하는 경우라면 해당 예약어는 역따옴표로 감싸지 않고는 사용할 수 없다는 것을 의미한다.

---

## MySQL 연산자의 내장 함수

### :) 문자열

문자열의 사용에는 `홑따옴표('')`를 사용하여 표시한다. 하지만 MySQL 에서는 `쌍따옴표("")`를 사용하여 문자열을 표기할 수 도 있다. MySQL 에서는 역따옴표(``)를 사용하여 감싸서 사용하면 예약어와의
충돌을 피할 수 있다.

만약 SQL 표준 표기법만 사용할 수 있게 강제하고자 한다면 sql_mode 시스템 변수값에 ANSI를 설정하면 된다.<br>
다만 주의해야 한다면 프로젝트 중간에 변경하게 된다면 기존의 쿼리 작동 방식에 영향도가 있기 때문에 초기에 적용하는것이 좋다. 운영하는 프로젝트에 설정을 변경하는것은 위험하기때문에 추천하지 않는다.

---

### :) 숫자

숫자값 또한 다른 DBMS와 마찬가지로 `따옴표('' or "")`를 통하여 입력하면 된다.

```sql
SELECT *
FROM test
WHERE number_column = '1001';
SELECT *
FROM test
WHERE string_column = 1001;
```

문자열 형태로 따옴표를 사용하여 비교할때 비교 대상이 숫자 값이거나 숫자 타입의 컬럼이면 MySQL서버가 문자열 값을 숫자 값으로 자동 변환한다,<br>
하지만 숫자 값과 문자열 값을 비교할 때는 한 가지 주의해야할 사항이 있ㄷ다.

위의 쿼리를 보게되면 첫번째 쿼리는 주어진 상수값을 숫자로 변환하는데, 이때는 상수값 하나만 변환하기 때문에 성능과 관련된 문제가 발생하지 않는다.

두번째 쿼리는 주어진 상숫값이 숫자인데, 비교되는 컬럼은 문자열 컬럼이다. 이때 MySQL은 문자열 컬럼 값을 숫자로 변환하여 비교하게 된다. 따라서 모든 문자열을 숫자로 변환해야 하기 때문에 인덱스가 있더라도 해당
인덱스를 이용하지 못한다. string_column에 알파벳과 같은 문자가 포함된 경우에는 숫자 값으로 변환할 수 없어 쿼리 자체가 실패할 수 있다.

> 원천적으로 해당 문제점을 발생시키지 않도록 `숫자 값은 숫자 타입의 컬럼에만 저장`하여야 한다.

---

### :) 날짜

다른 DBMS에서는 날짜 타입을 비교하거나 INSERT하기 위해서 문자열을 DATE 타입으로 변환하는 코드가 필요하지만<br>
MySQL에서는 정해진 형태의 날짜 포맷으로 표기하면 서버가 자동으로 DATE나 DATETIME 값으로 변환하기 때문에 복잡한 함수들을 사용할 필요가 없다.

---

### :) 동등 비교

동등 비교는 다른 DBMS와 마찬가지로 `=` 기호를 사용하여 비교를 수행한다, 하지만 MySQL에서는 동등 비교를 위해 <br>
`<=>`연산자도 제공한다, 연산자는 `=`연산자와 같으며 부가적으로 NULL값에 대한 비교까지 수행한다. 따라서 MySQL에서는 해당 연산자를 NULL-SAFE 비교 연산자라고도 부른다.

```sql
-- 출력 결과 : 1, NULL, NULL
SELECT 1 = 1, NULL = NULL, 1 = NULL;

-- 출력 결과 : 1, 1, 0
SELECT 1<=>1, NULL <=> NULL, 1 <=> NULL;
```

`NULL` 값은 `IS NULL` 연산자 이외에는 비교할 방법이 없다,

---

### :) 부정 비교(Not-Equal)

`같지않다` 라는 비교를 위한연산자로는 `<>`를 일반적으로 많이 사용한다, 이와 함께 `!=`도 제공한다. 두가지 방식 모두 문제가 되지 않지만 혼용해서 사용하지 않기를 권장한다.

---

### :) Not

```sql
-- 출력 결과 : 1
select True;

-- 출력 결과 : 0
select ! True;

```

---

### :) AND(&&) , OR(||) 연산자

일반적으로 DBMS에서는 불리언 표현식의 결과를 결합하기 위해 `AND, OR` 연산자를 주로 사용한다, MySQL에서는 추가적으로 `&&, ||`의 사용도 허용한다<br>
하지만 Oracle에서는 `||`를 불리언 표현식의 결합 연산자가 아니라 문자열을 결합하는 연산자로 사용한다.

Oracle에서 운영되던 애플리케이션을 MySQL로 이관한다거나 문자열 결합 연산에 `||`를 사용하고 싶다면
`sql_mode`의 설정 값을 `PIPE_AS_CONCET`으로 설정하면 된다.

---

### :) 나누기(/)와 나머지(%) 연산자

```sql
-- 실행 결과 : 5.8000
SELECT 29 / 5;

-- 실행 결과 : 4
select 29%5;
```

---

### :) LIKE

LIKE 는 간단하게 설명하면 `%`를 이용하여 다양한 조건검색을 할 수 있다.<br>

```sql
-- 
SELECT 'abcdef' LIKE 'abc%';
SELECT 'abcdef' LIKE '%abc';
SELECT 'abcdef' LIKE '%ef';
```

LIKE 에서 사용할 수 있는 와이르 카드 문자는 `%`와 `_`가 전부다.<br>

> % : 0또는 1개 이상의 모든 문자에 일치(문자의 내용과 관계없이)

> _ : 정확히 1개의 문자에 일치

LIKE 연산자는 와일드카드 문자인 (%,_)가 검색어의 뒤쪽에 있다면 인덱스 레인지 스캔으로 사용할 수 있지만, 와일드 카드가 검색어의 앞쪽에 있다면 인덱스 레인지 스캔을 사용할 수 없기 때문에 주의하여
사용하여야한다.

---

### :) BETWEEN

해당 연산자는 `크거나 같다`와 `작거나 같다`라는 두개의 연산자를 하나로 합친 연산자이다.

---

### :) IN

여러 개의 값에 대해 동등 비교 연산을 수행하는 연산자이다. 여러 개의 값이 비교되지만 범위로 검색하는 것이 아니라 여러 번의 동등 비교로 실행하기 때문에 일반적으로 빠르게 처리된다.

- 상수가 사용된 경우 : ... IN (?, ?, ?, ...);
- 서브쿼리가 사용된 경우 : ... IN (SELECT ... FROM ...);

---

### :) NULL 값 비교 및 대체

NULL값 비교 및 대체에는 `IFNULL`과 `ISNULL`이 있다.

`IFNULL` - 해당 컬럼이나 값이 NULL인지 비교한 후 , NULL이라면 다른 값으로 대체하는 용도로 사용할 수 있는 함수.
`ISNULL` - 인자로 전달한 표현식이나 컬럼의 값이 NULL인지 아닌지 비교하는 함수, ISNULL은 True일 경우 1, False일 경우 0을 반환

```sql
-- 실행 결과 : HELLO
SELECT IFNULL(NULL, 'HELLO');
```

---

### :) 현재 시각 조회(NOW, SYSDATE)

`NOW`와 `SYSDATE`는 같은기능을 수행한다, 하지만 NOW()와 SYSDATE()함수는 작동 방식에서 큰 차이가 있다.

하나의 SQL에서 모든 NOW()는 동일한 값을 가지지만 SYSDATE()함수는 하나의 SQL 에서도 호출되는 시점에 따라 결과값이 달라진다.

```sql
-- now()를 통해 나오는 결과값은 동일함
SELECT NOW(), SLEEP(3), NOW();

-- 앞의 SYSDATE() 값보다 뒤의 SYSDATE값이 3초 추가되어 나옴. 3초동안 대기하게 되었기때문
-- 실제로도 쿼리 실행시 3초 지연
SELECT SYSDATE(), SLEEP(3), SYSDATE()

```

그렇다면 위의 2개는 동일한 결과를 뱉는데 어떤것을 사용해야 할까 ?<br>

SYSDATE()함수는 큰 잠재적인 문제가 두가지가 있다.

1. SYSDATE()함수가 사용된 SQL은 레플리카 서버에서 안정적으로 복제되지 못한다.
2. SYSDATE()함수와 비교되는 컬럼은 인덱스를 효율적으로 사용하지 못한다.
   > 호출될때 마다 다른값을 반환하기 때문에 상수가 아니다, 따라서 인덱스를 스캔할 때도 매번 비교되는 레코드마다 함수를 실행해야 한다.
   <br> 하지만 NOW()함수는 실행되는 시점에 할당받아 모든 부분에서 사용하기 때문에 해당쿼리가 1시가니 소모되더라도 위치나 시점에 관계없이 항상 같은 값을 보장 할 수 있다.

만약 운영중인 애플리케이션에 SYSDATE()가 있다면 NOW()로 바꾸는것을 권장하며 만약 바꾸기 힘들다면
`my.cnf`나 `my.ini` 설정 파일에서 sysdate-is-now 시스템 변수를 넣어서 SYSDATE()를 호출하여도 NOW()처럼 동작하도록 설정을 하는것을 권장한다.

---

### :) 날짜와 시간의 포맷

DATETIME 타입의 컬럼이나 값을 원하는 형태의 문자열로 변환해야 할 때는 DATE_FORMAT()함수를 이용하면된다.<br>

DATE_FORMAT을 표현하기 위한 지정문자는 https://www.w3schools.com/sql/func_mysql_date_format.asp 다음 사이트를 참고하면됩니다.

```sql
-- 다음과 사용 가능 
SELECT DATE_FORMAT(now(), '%Y%m%d %H:%i:%s');
```

---

### :) 날짜와 시간의 포맷

특정 날짜에서 연도나 월을 더하거나 뺄때는 `DATE_ADD()`, `DATE_SUB()`함수를 사용한다.<br>
사실 `DATE_ADD()`로도 빼기연산을 수행할 수 있어서 `DATE_SUB()`가 크게 필요로 하지는 않는다.

```sql
-- NOW()에서 +1일 
SELECT DATE_ADD(NOW(), INTERVAL 1 DAY ) as tommow;

-- NOW()에서 -1일
SELECT DATE_ADD(NOW(), INTERVAL -1 DAY ) as yesterday;
```

추가 또는 뺴기에는 다양한 옵션이 있으며 해당 사이트 확인
https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_date-add

---

### :) 문자열 처리

`PRAD()`와 `LPAD()`함수는 문자열의 좌측 또는 우측에 문자를 덧붙여서 지정된 길이의 문자열로 만드는함수다.

```sql
-- 출력 결과 : HELLO_____
SELECT RPAD('HELLO', 10, '_');

-- 출력 결과 : _____HELLO
SELECT LPAD('HELLO', 10, '_');
```

#### 🔖 `RTRIM()`, `LTRIM()`, `TRIM()`

- RTRIM() : 우측에 있는 공백을 제거한다.
- LTRIM() : 좌측에 있는 공백을 제거한다.
- TRIM() : 좌 우측에 있는 공백을 제거한다.

#### 🔖 `CONCAT()` 문자열을 결합한다

```sql
-- 출력 결과 :  HELLOYUNJINWORLD
SELECT CONCAT('HELLO', 'YUNJIN', 'WORLD');
```

#### 🔖 `GROUP CONCAT`  문자열 결합

`GROUP_CONCAT()` 함수는 값들을 먼저 정렬한 후 연결하거나 각 값의 구분자 설정도 가능하며, 여러 값중에서 중복을 제거하고 연결하는 것도 가능하다.

```sql
-- 컬럼에 데이터가 1,2,3,4,5가 있다고 가정
-- 출력 결과 : 12345
SELECT GROUP_CONCAT(sample)
FROM sample;

-- 출력 결과 1|2|3|4|5
SELECT GROUP_CONCAT(sample SEPARATOR '|')
FROM sample;
```

#### 🔖 `CASE WHEN ... THEN ... END` 값으 ㅣ비교와 대체

CASE WHEN 은 함수가 아니라 SQL 구문이다. CASE WHEN 은 프로그래밍 언어에서 제공하는 SWITCH구문과 같은 역할을 한다. CASE로 시작하고 END로 끝나야 하며, WHEN ... THEN ...
은 필요한 만큼 반복해서 사용할 수 있다.

다음과 같이 사용 가능

```sql

SELECT CASE
           WHEN (select 1 + 1) = 2 THEN '같음'
           ELSE '다름' END as result;
```

#### 🔖 타입의 변환(CAST, CONVERT)

SQL은 텍스트 기반으로 작동하기 때문에 SQL에 포함된 모든 입력값은 무자열처럼 취급된다. 이럴 때 명ㅁ시적으로 타입의 변환이 필요하다면 `CAST()`함수를 이용하면된다.
`CONVERT()` 함수도 CAST()와 거의 비슷하며, 단지 함수의 인자 사용 규칙만 조금 다르다.

사용방법은 다음과 같다.

```sql
-- 문자열 12345를 숫자 12345로 변환해준다.
-- 중간에 문자열이 들어가 있더라도 숫자만 반환한다.
SELECT CAST('12345' as signed INTEGER) as converted_integer;
```

#### 🔖 암호화 및 해시 함수(MD5, SHA, SHA2)

MD5와 SHA 모두 비대칭형 암호화 알고리즘이다, 인자로 전달한 문자열을 각각 지정된 비트 수의 해시 값을 만들어내는 함수다.<br>
SHA()함수는 SHA-1 암호화 알고리즘을 사용하며, 결과로 160비트 해시 값을 반환한다.

`SHA2()`함수는 SHA 암호화 알고리즘보다 더 강력한 224비트부터 512비트 암호화 알고리즘을 사용하여 생성된 해시 값을 반환한다. MD5()함수는 메시지 다이제스트 알고리즘을 사용하여 128비트 해시값을
반환한다.

```sql
-- 실행 결과 : 31dff6ef956b7f5d45e9b266fdf3bf41 (32글자)
SELECT MD5('YUNJINCHOI');

-- 실행 결과 : 4562f16bb139ac24609320e0f7d979445ff4e86e (40글자)
SELECT SHA('YUNJINCHOI');

-- 실행 결과 : a4235000575868b9f3076cc261276780bbf60b7f53d045e5a38bdcb97ed3c819 (64글자)
SELECT SHA2('YUNJINCHOI', 256);
```

#### 🔖 처리 대기 (SLEEP)

`SLEEP()`함수는 DBMS쿼리 실행 도중 멈춰서 대기하는 기능이다.

```sql
-- 해당 쿼리가 실행되면 1.5초 뒤에 결과를 확인할 수 있다.
SELECT SLEEP(1.5);
```

#### 🔖 JSON 포맷 (JSON PRETTY)

MySQL 에서는 JSON 데이터의 기본적인 표시 방법은 단순 텍스트 포맷인데, 해당 포멧은 JSON 컬럼값에대한 가독성이 떨어진다. 하지만 JSON_PRETTY()함수를 사용하면 JSON 컬럼의 값을 읽기 쉬운
포맷으로 변환해준다.

#### 🔖 JSON 필드 크기 (JSON_STORAGE_SIZE)

JSON 데이터는 텍스트 기반이지만 MySQL 서버는 디스크의 저장 공간을 절약하기 위해 JSON 데이터를 실제 디스크에 저장할 때 BSON 포맷을 사용한다, 하지만 BSON으로 변환하였을때 저장 공간의 크기가
얼마나 되ㄹ지 예측하기가 어렵다. 이를 위해 MySQL 서버에서는
`JSON_STORAGE_SIZE()`함수를 제공한다.

---

## 😊 SELECT

#### 🔖 SELECT 절의 처리 순서

해당 책에서 설명하는 절에서는 (SELECT, FROM, JOIN, WHERE, GROUP BY, HAVING, ORDER BY, LIMIT)과 그 뒤에 기술된 표현식을 묶어서 말한다.
 
개발을 통해 SQL을 작성할때 어느 절이 먼저 실행되는지를 모르면 처리 내용이나 처리결과를 예측할 수 없다.

1. FROM
2. ON
3. JOIN
4. WHERE
5. GROUP BY
6. HAVING
7. SELECT
8. DISTINCT
9. ORDER BY

순으로 실행이 됩니다.


#### 🔖 WHERE 절과 GROUP BY절 ORDER BY 절에서의 인덱스 사용

인덱스를 사용하기 위한 기본 규칙은 기본적으로 인덱스된 컬럼의 값 자체를 변환하지 않고 그대로 사용한다는 조건을 만족해야 한다.<br>
인덱스는 컬럼의 값을 변환 없이 B-Tree에 정렬한다음 저장한다. Where 조건이나 Group By 또는 Order by 에서도 원본값을 검색하거나 정렬할 때만 B-Tree에 정렬된 인덱스를 이용한다.

```sql
# 다음과 같이 변형해서 사용하게 되면 올바르게 인덱스를 이용하지 못한다.
SELECT * FROM salaries WHERE salary * 1000;
```


#### 🔖 WHERE 절의 비교 조건 사용 시 주의사항

다른 DBMS와는 다르게 MySQL에서는 NULL 값이 포함된 레코드도 인덱스로 관리가 된다. 이는 즉 MySQL의 인덱스는 NULL값을 값으로 인정해서 관리한다는 것을 의미한다.

MySQL에서 NULL 값을 비교하기 위해서는 `IS NULL` 이나 `<=>`연산자를 사용해야 한다.

#### 🔖 문자열이나 숫자 비교
문자열 컬럼이나 숫자 컬럼을 비교할 때는 반드시 그 타입에 맞는 상숫 값을 사용해야 한다.
즉 비교 대상 컬럼이 문자열 컬럼이라면 문자열 리터럴을 사용하고, 숫자 타입이라면 숫자 리터럴을 이용하는 규칙만 지켜주면된다.

> 10001 이라고 해서 '10001' 이라고 비교하지 말라고 파악하면 될듯하다.


#### 🔖 날짜 비교

날짜만 저장하는 DATE와 날짜와 시간을 함께 저장하는 DATETIME과 TIMESTAMP가 있으며 시간만 저장하는 TIME이라는 타입도 있어서 복잡하다고 느낄 수 있다.

하지만 자주 사용되는것은 DATE와 DATETIME 비교 방식과 함께 TIMESTAMP와 DATETIME 비교에대해 알아본다.

#### 🔖 DATE 또는 DATETIME과 문자열 비교

DATE or DATETIME 타입의 값과 문자열을 비교할 때는 문자열 값을 자동으로 DATETIME 타입의 값으로 변환해서 비교를 수행한다.

개발자 or 사용자가 STR_TO_DATE() 함수를 이용하여 변경해서 비교하지 않아도 MySQL이 내부적으로 변환을 수행한다.

```sql
-- hire_date를 문자열로 강제로 변경하기 때문에 인덱스를 효율적으로 이용하지 못한다.
SELECT COUNT(*) FROM emplyees WHERE hire_date > '2022-01-08';

-- 다음과 같이 하는것이 좋음
SELECT COUNT(*) FROM emplyees WHERE DATE_FORMAT(hire_date,'%Y-%m-%d') > '2022-01-08';
```

---

#### 🔖 DATE 또는 DATETIME과 비교

DATETIME 타입의 값을 DATE 타입으로 만들지 않고 그냥 비교하게 된다면 MySQL서버가 DATE타입의 값을 DATETIME 값으로 변환을하여비교하게 된다.
하지만 DATE-> DATETIME 으로 값을 변경할 경우 `2022-01-08 00:00:00`으로 변환되게 되어 DATETIME의 값이 `2022-01-08 00:00:01` 이라면 비교시 false가 뜨게 된다.

---

#### 🔖 DATETIME과 TIMESTAMP 비교 
DATE나 DATETIME 타입과 TIMESTAMP의 값을 별도의 타입 변환 없이 비교하면 인덱스를 사용하여 문제가 없을듯 하지만 실제로는 그러지 않다.

비교하고자 하는 컬럼이 DATETIME 타입이라면 FROM_UNIXTIME()함수를 이용하여 TIMESTAMP값을 DATETIME 타입으로 만들어서 비교해야 한다.

---

#### 🔖 Short-Circuit Evaluation 을 사용할것

---

#### 🔖 DISTINCT
특정 컬럼의 유니크한 값을 조회화려면 SELECT 쿼리에 DISTINT를 사용한다.<br>
개발시 DISTINCT를 많이 사용하지만 해당 DISTINCT를 남용하게 되면 성능적인 문제도ㅓ 있지만 쿼리의 결과도 의도한 바와 달라질 수 있다.


---


#### 🔖 LIMIT n
LIMIT는 지정된 순서에 위치한 레코드만 가져오고자 할 때 사용한다.
```sql
-- 조회한 employees의 결과에서 상위 5개만 반환한다.
SELECT * FROM employees LIMIT 0, 5;
```

---


#### 🔖 COUNT
COUNT() 함수는 모두가 잘 알고 있듯이 결과 레코드의 건수를 반환하는 함수다.

MyISAM 스토리지 엔진을 사용한다면 테이블의 메타 정보에 전체 레코드 건수를 관리한다.<br>
하지만 WHERE조건이 있는 COUNT(*)쿼리는 그조건에 일치하는 레코드를 읽어 보지 않는 이상 알 수 없으므로 일반적인 DBMS와 같이 처리된다.

---

#### 🔖 JOIN