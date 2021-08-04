--  가장 큰값으 제외한 가장큰값을 구하면 2번째로 큰값이 나옴 .
SELECT MAX(salary) AS SecondHighestSalary
FROM   employee
WHERE  salary
    NOT IN(
        SELECT MAX(salary)
        FROM employee
    )