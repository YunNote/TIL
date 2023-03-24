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

