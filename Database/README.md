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
> - `Caching SHA-2 Pluggable Authentication`
> 
> 
> - `PAM Pluggable Authentication`
> 
> - `LDAP Pluggable Authentication`
