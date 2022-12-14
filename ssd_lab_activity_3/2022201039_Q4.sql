USE COMPANY;

SELECT DEPARTMENT.Dnumber, Dname, COUNT(Dlocation)
FROM DEPARTMENT JOIN DEPT_LOCATIONS ON DEPARTMENT.Dnumber=DEPT_LOCATIONS.Dnumber
WHERE DEPARTMENT.Dnumber IN (SELECT Dnumber FROM DEPARTMENT
WHERE Mgr_ssn IN (SELECT Essn
FROM (SELECT Essn, COUNT(Sex) AS COUNT_Sex
FROM (SELECT Essn, Sex FROM DEPENDENT WHERE Sex = 'F') AS DEPENDENT_F
GROUP BY Essn) AS DEPENDENT_COUNT_F
WHERE (2 <= COUNT_Sex)))
GROUP BY DEPARTMENT.Dnumber, Dname;
