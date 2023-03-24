## 보안 제어 

---

### 🌱 IP 주소 기반 접근 제어

```shell
location /test/ {
  deny 10.0.0.1;
  allow 10.0.0.0/20
  allow 2001:0db8::/32;
  deny all
}
```

`allow`와 `deny` 지시자는 http, server, location 과 TCP/UDP 에 대한 stream server 컨텍스트에서 사용 가능.

`allow` 의 경우 해당 IP에 대한 접근을 허용을 의미하며 `deny`의 경우에는 거부하는것으로 한다. 
접근이 차단되면 403응답을 받는다.