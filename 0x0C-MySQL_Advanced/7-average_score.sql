-- 7. Average score 
-- This a SQL script creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student.
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER |
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
DECLARE prom FLOAT;
SET prom = (SELECT AVG(score) FROM corrections AS newTable WHERE newTable.user_id=user_id);
UPDATE users SET average_score=prom WHERE id=user_id;
END;
|