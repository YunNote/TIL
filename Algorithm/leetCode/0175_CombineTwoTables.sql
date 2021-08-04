-- Join 을 사용하여 풀수있는 간단한 문제였다.
SELECT p.FirstName,
       p.LastName,
       a.City,
       a.State
FROM   Person AS p
       LEFT JOIN Address AS a
              ON p.Personid = a.Personid;

