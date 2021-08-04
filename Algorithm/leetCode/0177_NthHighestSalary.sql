CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  -- N 번째의 값을 구해야 하기 때문에 N 에서 -1을 해준다. 
  SET N = N - 1;

  RETURN (
    SELECT MAX(Salary) AS getNthHighestSalary
    FROM employee
    WHERE salary
      NOT IN (
        SELECT *
        FROM (
          SELECT DISTINCT Salary
          FROM Employee
          ORDER BY Salary DESC LIMIT N
        ) AS tmp
      )
  );
end 