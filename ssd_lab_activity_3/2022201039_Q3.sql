USE COMPANY;

SELECT Essn AS 'Manager ssn', COUNT(Pno) AS 'Number of projects'
FROM WORKS_ON
WHERE Essn IN (SELECT Mgr_ssn
FROM DEPARTMENT
WHERE Dnumber IN (Select Dnum
FROM PROJECT
WHERE Pname = 'ProductY'))
GROUP BY Essn;
