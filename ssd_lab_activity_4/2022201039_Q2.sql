CREATE PROCEDURE getNames(
    IN city varchar(35)
)
BEGIN
    SELECT CUST_NAME FROM customer WHERE WORKING_AREA = city;
END
