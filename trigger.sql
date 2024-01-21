DELIMITER //

CREATE TRIGGER assign_to_least_employee_slot
AFTER INSERT ON employee
FOR EACH ROW
BEGIN
    DECLARE least_employee_slot INT;

    SELECT slot_id INTO least_employee_slot
    FROM (
        SELECT slot_id, COUNT(*) AS employee_count
        FROM employee_work_slot
        GROUP BY slot_id
        ORDER BY employee_count
        LIMIT 1
    ) AS least_employee_count;

    INSERT INTO employee_work_slot (slot_id, employee_id)
    VALUES (least_employee_slot, NEW.employee_id);
END //

DELIMITER ;