CREATE VIEW space_art AS
SELECT p.name, p.description
FROM piece AS p
JOIN exhibit AS e
ON e.exhibit_id = p.exhibit_id
WHERE e.theme = 'Space Exploration';