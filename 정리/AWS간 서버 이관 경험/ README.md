>#### 처음 하는 작업이라 해당 내용이 정답이다 아니다라는 내용은 없습니다. 다만 경험했던 내용을 적었습니다.


`A`라는 별칭의 AWS에 있는 FrontServer를 `B`라는 별칭의 AWS 계정으로 이관해야하는 작업이었습니다.

또한 BitBucket Pipeline -> Jenkins 로도 옮겨야 하는 설정도 같이 들어갔어야 했으며, 추가되는 파라미터들도 있었습니다.

 
작업을 하기전에 순서를 나름대로 정해봤습니다. 

`1. 어떠한 Domain을 옮겨야 하는가 Route53에서 확인.` <br>
`2. 해당 Route53에 어떤 ALB가 매핑되어있는지 확인.` <br>
`3. 옮기고자 하는 Front Server에서 호출하는 API들은 무엇이 있는가` <br>
`4. API를 호출할 경우 API Server는 어떻게 호출해야 하는가, Public인지 Private인지` <br>
`5. 별칭 B AWS에서 도메인이 A AWS에 있어도 SSL이 발급이 되는지.` <br>
`6. 해당 Domain으로 들어오는 URL들이 뭐뭐 있는지. ALB를 통하여 확인` <br> 
`7. ALB, RDS, ECS 등 보안그룹(Security Group) 이 어떻게 설정되어 있고 어떠한 포트들을 개방하여야 하는가 `<br>
`8. BitBucket Pipeline -> Jenkins 로 변경하면서 taskDefinition은 어떻게 작성하고 추가되야할 Parameter들은 무엇인가`



