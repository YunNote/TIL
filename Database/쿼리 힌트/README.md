## 쿼리 힌트

---
> MySQL 서버는 우리가 서비스 하는 비지니스를 100% 이해하지 못합니다.<br>
> 그래서 해당 서비스의 개발자 or DBA보다 MySQL 서버가 부족한 실행 계획을 수립할 가능성이 있다.
> 
> 이러한 경우 옵티마이저에게 쿼리의 실행 계획을 수립해야 할지 알려줄 수 있는 방법이 필요하다
> 이 방법을 `쿼리 힌트`라고 한다.


### MySQL 에서 사용 가능한 쿼리 힌트 

 - 인덱스 힌트
 - 옵티마이저 힌트 

`인덱스 힌트`들은 모두 SQL의 문법에 맞게 사용해야 하기때문에 `ANSI-SQL`표준 문법을 준수하지 못하게 되는 단점이 있다.<br>
 그와 반대로 `옵티마이저 힌트`들은 `인덱스 힌트`와는 달리 MySQL서버를 제외한 RDBMS에서는 주석으로 해석되기 때문에 `ANSI-SQL`표준을 준수한다고 볼 수 있다.

가능하다면 `인덱스 힌트`가 아닌 `옵티마이저 힌트`를 사용하는것을 추천한다고 한다.

----


### ⭐ 인덱스 힌트

#### 인덱스 힌트는 예전 버전의 MySQL 서버에서 사용되던 `USE INDEX`와 같은 힌트를 의미한다.

`STRAIGHT_JOIN` 과 `USE INDEX`등을 포함한 인덱스 힌트들은 MySQL 서버에 옵티마이저 힌트가 도입되기 전부터 사용되던 기능들입니다.

인덱스 힌트들은 모두 SQL의 문법에 맞게 사용해야 하기때문에 `ANSI-SQL`표준 문법을 준수하지 못하게 되는 단점이 있다.

또한 인덱스 힌트는 `SELECT`와 `UPDATE`명령에서만 사용 가능하다.


### ⭐ 옵티마이저 힌트

#### 옵티마이저 힌트는 MySQL 5.6버전부터 새롭게 추가되기 시작한 힌트들을 지칭하는 용어입니다.

`옵티마이저 힌트`들은 `인덱스 힌트`와는 달리 MySQL서버를 제외한 RDBMS에서는 주석으로 해석되기 때문에 `ANSI-SQL`표준을 준수한다고 볼 수 있다.

---



#### ☝ STRAIGHT_JOIN
> STRAIGHT_JOIN은 MySQL5.6 이전부터 추가되었지만 옵티마이저 힌트이기도함과 동시에 조인 키워드이기도 하다.

STRAIGHT_JOIN의 역할은 `SELECT`, `UPDATE`, `DELETE`쿼리에서 여러 개의 테이블이 조인되는 경우 조인 순서를 고정하는 역할을 한다.

```sql
EXPLAIN
SELECT *
FROM employees e, dept_emp de, departments d 
WHERE e.emp_no = de.emp_no AND d.dept_no = de.dept_no;
```
위의 쿼리를 실행시켜서 나오는 실행 계획을 확인 해본다면 밑의 사진처럼 나올것입니다.

<img src="./straight_join.PNG" alt="" width="450" />

위 쿼리의 실행계획을 확인해보면 `department as d` 테이블을 드라이빙 테이블로 선택한것을 볼수 있고,<br>
두번재로는 `dept_emp as de` 테이블을 읽은 뒤에 마디막으로 `departments as d` 테이블을 읽었음을 확인할 수 있다.

실행계획은 일반적인 경우 `인덱스 여부` 로 조인의 순서가 결정되며 조인 컬럼의 인덱스에 아무런 문제가 없는 경우에는
`WHERE 조건`이 있는경우 해당 조건을 만족한 이후, 레코드가 적은 테이블을 드라이빙테이블로 선택한다.


>위의 내용만 본다면 rows 가 가장작은 `employees as e`가 드라이빙 테이블로 선택되어야 할듯 하지만 9건의 rows를 가지고 있는 `departments as d`가 드라이빙 테이블로 선택되어있다
> 
> 해당 이유는 type을 보면 알 수 있다. eq_ref는 조인시 기본 키나 고유키를 사용하여 하나의 값으로 접근( 최대 1행만을 정확하게 패치)한다고 합니다.
> 그렇다는건 rows의 갯수는 많지만 조건식으로 인하여 최대 1개로 판단되어 드라이빙 테이블 우선순위에서 밀린듯하다.


하지만 위의 쿼리 조인 순서 말고 사용자가 직접 STRAIGHT_JOIN 힌트를 통해 조인 순서를 변경 할 수 있다.  

```sql
SELECT STRAIGHT_JOIN
 e.first_name, e.last_name, d.dept_name
FROM employees e, dept_emp de, departments d
WHERE e.emp_no = de.emp_no AND d.dept_no = de.dept_no;

-- 위아래의 코드는 동일하게 동작한다.

SELECT /*! STRAIGHT_JOIN */
 e.first_name, e.last_name, d.dept_name
FROM employees e, dept_emp de, departments d
WHERE e.emp_no = de.emp_no AND d.dept_no = de.dept_no;

```

위의 쿼리를 실행하면 STRAIGHT_JOIN 힌트를 통하여 FROM절에 명시된 테이블의 순서대로 조인을 수행하도록 유도한다.
따라서 해당 쿼리의 실행계획을 보면 FROM절에 선언된 순서대로 조인을 수행합니다.

1. employees
2. dept_emp
3. departments 순입니다.

그렇다면 어떤 경우에 STRAIGHT_JOIN 힌트로 조인 순서를 조정하는 것이 좋을까 ?

1. 임시테이블과 일반 테이블의 조인
2. 임시 테이블끼리 조인
   >임시 테이블은 항상 인덱스가 없기 때문에 어느 테이블을 먼저 드라이빙으로 읽어도 무관하기 때문에 크기가 작은 테이블순으로 드라이빙되도록 선택해주는것이 좋다.
3. 일반 테이블끼리 조인
   > 양쪽 테이블 모두 조인 컬럼에 인덱스가 있거나, 조인컬럼에 인덱스가 없는경우에는 레코드 수가 적은 테이블을 드라이빙으로선택해주는 것이 좋다, 그 외의 경우에는 조인 컬럼에 인덱스가 없는 테이블을 드라이빙으로 선택하는것이 좋다.


---