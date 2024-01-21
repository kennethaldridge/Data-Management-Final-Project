DELIMITER $$

CREATE FUNCTION dept_employee_num(
	dept_name VARCHAR (50)
)
RETURNS INT
DETERMINISTIC
BEGIN
	DECLARE employees_num INT;
    
	SELECT COUNT(*) INTO employees_num
    FROM employee AS e
    JOIN department AS d
    ON d.dept_id = e.dept_id
    WHERE d.dept_name = dept_name;
    
    RETURN employees_num;
END $$

DELIMITER ;