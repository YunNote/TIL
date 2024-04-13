## 7장 비동기 호출 

---

fetch 를 사용하여 네트워크 API 구현이 가능하나, 내장 라이브러리이기 때문에 많은 기능을 사용하려면
직접 구현하여 사용해야 한다. 따라서 이러한 번거로움때문에 fetch 대신 Axios 라이브러리를 사용한다.

Axios를 사용하면 각 서버의 기본 URL을 호출하도록 Request를 따로 구성할 수 있으며 별도의
헤더를 설정해야 하는 로직이 있을 경우 인터셉터 기능을 사용하여 처리할 수 있다.

```typescript
AxiosInstance.interceptors.request.use(AxiosRequestComfig)를 반환받아 인터셉터 기능을 설정할 수 있다.
```

---

런타임 응답타입을 검증하기 위해 Superstruct 라이브러리를 사용할 수 있다.

P.214 참고하면 예제를 볼 수 있음. assert, is , validate 모듈은 데이터의 유효성 검사를 도와준다.