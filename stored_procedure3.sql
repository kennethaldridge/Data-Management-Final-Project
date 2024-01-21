DELIMITER $$

CREATE PROCEDURE get_art_by_artist(
	IN last_name VARCHAR(50),
    IN first_name VARCHAR(50)
)
BEGIN
	SELECT p.name, p.description
    FROM piece AS p
    JOIN artist AS a
    ON p.artist_id = a.artist_id
    WHERE a.first_name = first_name AND a.last_name = last_name;
END $$

DELIMITER ;