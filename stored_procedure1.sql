DELIMITER $$

CREATE PROCEDURE get_visits_by_day(
	IN visit_date DATE
)
BEGIN
	SELECT v1.visitor_id, v1.first_name, v1.last_name, v1.email
    FROM visitor AS v1
    JOIN visit AS v2
    ON v1.visitor_id = v2.visitor_id
    WHERE v2.date = visit_date;
END $$

DELIMITER ;