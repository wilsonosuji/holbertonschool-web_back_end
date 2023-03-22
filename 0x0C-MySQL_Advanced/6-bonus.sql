-- 6. Add bonus
-- This SQL script creates a stored procedure AddBonus that adds a new correction for a student.
DELIMITER |
CREATE PROCEDURE AddBonus(user_id INT, project_name VARCHAR(255), score FLOAT)
BEGIN
DECLARE idProject INT;
IF (SELECT COUNT(*) FROM projects WHERE name = project_name) = 0 THEN
    INSERT INTO projects(name) VALUES(project_name);
END IF;
SET idProject = (SELECT id FROM projects WHERE name = project_name);
INSERT INTO corrections (user_id, project_id, score) VALUES(user_id, idProject, score);
END;
|
