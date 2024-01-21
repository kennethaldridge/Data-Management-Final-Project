DELIMITER $$

CREATE FUNCTION money_date(
	visit_date DATE
)
RETURNS INT
DETERMINISTIC
BEGIN
	DECLARE money INT;
    
	SELECT SUM(r.visitor_count * t.price) INTO money
    FROM visit AS v
    JOIN ticket AS t
    ON t.ticket_id = v.ticket_id
    JOIN reservation AS r
    ON v.visitor_id = r.visitor_id
    WHERE v.date = visit_date;
    
    RETURN money;
END $$

DELIMITER ;