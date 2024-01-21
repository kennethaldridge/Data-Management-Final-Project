DELIMITER $$

CREATE FUNCTION num_checked_in(
	last_name VARCHAR(50),
    first_name VARCHAR(50)
)
RETURNS INT
DETERMINISTIC
BEGIN
	DECLARE num_checked_in INT;
    
	SELECT SUM(r.visitor_count) INTO num_checked_in
    FROM visit AS v
    JOIN reservation AS r
    ON v.visitor_id = r.visitor_id
    JOIN employee AS e
    ON e.employee_id = v.receptionist_id
    WHERE e.last_name = last_name and e.first_name = first_name;
    
    RETURN num_checked_in;
END $$

DELIMITER ;