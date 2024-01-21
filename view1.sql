CREATE VIEW hr_employees AS
SELECT e.employee_id, e.first_name, e.last_name
FROM employee AS e
JOIN department AS d
ON e.dept_id = d.dept_id
WHERE d.dept_name = 'HR';