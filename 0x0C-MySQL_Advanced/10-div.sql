-- 10. Safe divide 
-- This SQL script creates a function SafeDiv that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.
DELIMITER $$
CREATE FUNCTION SafeDiv(a INT,b INT)
    RETURNS FLOAT
    BEGIN
        DECLARE total FLOAT;
        IF b = 0 THEN
            SET total = 0;
        ELSE
            SET total = a / b;
        END IF;
        RETURN (total);
    END$$
DELIMITER ;
