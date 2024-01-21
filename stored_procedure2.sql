DELIMITER $$

CREATE PROCEDURE get_employee_work_day(
	IN work_date DATE
)
BEGIN
	SELECT e1.employee_id, e2.first_name, e2.last_name, e1.check_in, e1.check_out
    FROM employee_check_in AS e1
    JOIN employee AS e2
    ON e1.employee_id = e2.employee_id
    WHERE e1.date = work_date;
END $$

DELIMITER ;