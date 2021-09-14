> 해당 예제는 MySQL 8.0.21 버전으로 작성되었습니다.


### 😊 계정 생성 

`MySQL 5.7` 버전까지는 GRANT 명령으로 권한의 부여와 동시예 계정 생성이 가능했다면 
`MySQL 8.0`버전 부터는 계정의 생성은 `CREATE USER`명령어로, 권한 부여는 `GRANT`명령으로 구분해서 실행하도록 변경되었다.


> 계정 생성시 사용 가능한 옵션

- 계정의 인증 방식과 비밀번호
- 비밀번호 관련 옵션( 유효기간, 이력 개수, 재사용 불가기간)
- 기본 역할
- SSL 옵션
- 계정 잠금 여부 


>`계정의 인증 방식과 비밀번호 (IDENTIFIED WITH)`<br>
> IDENTIFIED WITH 뒤에는 인증방식을 명시해야 한다. MySQL 서버의 기본 인증 방식을
> 사용하고자 한다면 IDENTIFIED BY 'password' 형식으로 명시해야한다.
> 
> 다양한 인증 박식을 플러그인 형태로 제공하지만 다음 4가지는 가장 대표적인 방식이다.
> -  `Native Pluggable Authentication` : 5.7버전까지 default로 사용되던 방식이다, 단순하게 비밀번호에 대한 해시값만 저장해두고
>    Client가 보낸 값과 해시값이 일치하는지만 비교하는 인증 방식.
> 
> 
> - `Caching SHA-2 Pluggable Authentication` : 암호화 해시값 생성을 위해 SHA-2알고리즘을 사용한다. Native Authentication 플러그인은
> 입력이 동일 해시값을 출력하지만 Caching SHA-2 Authentication은 내부적으로 Salt키를 사용한다. 따라서 동일한 키 값에 대해서도
> 결과값이 달라진다. 하지만 해시값을 계산하는 방식은 시간이 많이 소모되어 성능이 떨어지는데, 이를 보완하기위해서, 해시 결과값을 메모리에
> 캐시해서 사용하게 된다. 따라서 인증방식의 이름에 Caching가 포함된 것이다. <br>
> 해당 인증 방식을 사용하기 위해서는 SSL/TLS 또는 RSA 키페어를 반드시 사용해야하는데, 이를 위해서 SSL옵션을 활성화 해야한다.
> 
> 
> - `PAM Pluggable Authentication` : 유닉스나 리눅스 패스워드 or LDAP같은 외부 인증을 사용할 수 있게 해주는 인증방식으로, MySQL 엔터프라이즈 에디션에서만 사용 가능
> 
> 
> - `LDAP Pluggable Authentication` :  LDAP를 이용한 외부 인증을 사용할 수 있게 해주는 인증방식으로 MySQL 엔터프라이즈 에디션에서만 사용 가능하다.
> 
> `LDAP`프로토콜은 다음에 공부해서 어떠한 내용인지 올리겠습니다.


MySQL 5.7버전 까지는 Native Authentication이 기본 인증 방식으로 사용되었지만, MySQL 8.0버전부터는 Caching SHA-2 Authentication이 기본인증 방식으로 변경되었다.

하지만 위에 나온 것처럼 기존 방식과 다른 방식으로 접속해야한다. 하지만 실습을 위해서는 Native Authentication을 기본방식으로 설정할 것이다..

```sql
SET GLOBAL default_authentication_plugin="mysql_native_password"
```

<hr>

>`⭐ 비밀번호 관련 옵션( 유효기간, 이력 개수, 재사용 불가기간)`
> 
> - Password Expire (유효 기간) : 비밀번호의 유효 기간을 설정하는 옵션, 명시하지 않으면 default_password_lifetime은 시스템 변수에 저장된 기간으로 유효기간 설정.
>   password expire에 설정 가능한 옵션은 다음과 같다<br><br>
> 
>   `PASSWORD EXPIRE` - 계정 생성과 동시에 비밀번호의 만료 처리<br>
>   `PASSWORD EXPIRE NEVER` - 계정 비밀번호의 만료기간이 없음.<br>
>   `PASSWORD EXPIRE DEFAULT` - default_password_lifetime 시스템 변수에 저장된 기간으로 비밀번호의 유효기간 설정<br>
>   `PASSWORD EXPIRE INTERVAL n DAY` - 비밀번호의 유효 기간을 오늘부터 n 일자로 설정<br>

<hr>

>`⭐ PASSWORD HISTORY (비밀번호 이력 개수)`
> 
>  - 해당 옵션은 한번 설정하였던 비밀번호는 재사용하지 못하게 설정하는 옵션이다. 
> 
>   `PASSWORD HISTORY DEFAULT` - password_history 시스템 변수에 저장된 개수만큼 비밀번호의 이력을 저장하고, 이력에 남아있다면 해당 비밀번호는 재사용 할 수 없다.<br>
>   `PASSWORD HGISTORY n` - 비밀번호의 이력을 최근 n개 까지만 저장한다. 이력에 남아있다면 해당 비밀번호는 사용할 수 없다.
> 
>  만약 history 를 확인하고 싶다면 아래명령어로 history 테이블을 확인하면 됩니다.
> 
> ```sql
> SELECT * FROM mysql.password_history; 
> ```


<hr>

>`⭐ PASSWORD REUSE INTERVAL (비밀번호의 재사용 금지 기간 설정)`
> 
> 한번 사용했던 비밀번호의 재사용 금지 기간을 설정하는 옵션, 직접 명시 하지 않는다면 password_reuse_interval 시스템 변수에 저장된 기간으로 설정.
>
>   `PASSWORD REUSE INTERVAL DEFAULT` - password_reuse_interval 변수에 저장된 일로 설정.<br>
>   `PASSWORD REUSE INTERVAL n DAY` - n일자 이후에 해당 비밀번호를 재사용 할 수 있다. <br>


<hr>

>`⭐ PASSWORD REQUIRE (비밀번호 변경 관련)`
> 
> 비밀번호가 만료되어서 변경할때 현재 비밀번호의 입력 여부를 설정하는 옵션
> 
>   `PASSWORD REQUIRE CURRENT` - 비밀번호 변경시 현재 비밀번호를 먼저 입력하도록 설정<br>
>   `PASSWORD REQUIRE OPTIONAL` - 비밀번호를 변경할 때 현재 비밀번호를 입력하지 않아도 되도록 설정<br>
>   `PASSWORD REQUIRE DEFAULT` - password_require_current 시스템 변수의 값으로 설정

<hr>

>`⭐ ACCOUNT LOCK / UNLOCK (잠금)`
> 
>  계정 생성시 or ALTER USER 명령시 계정 정보를 변경할 때 계정을 사용하지 못하게 잠금유무에 대한 결정
> 
>   `ACCOUNT LOCK` - 계정을 사용하지 못하도록 잠금<br>
>   `ACCOUNT UNLOCK` - 계정을 다시 사용 가능하도록 잠금 해제