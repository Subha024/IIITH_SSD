CREATE PROCEDURE addNumbers(
    IN inputNum1 INT,
    IN inputNum2 INT,
    OUT outputNum INT
)
BEGIN
    SELECT inputNum1+inputNum2 INTO outputNum;
END