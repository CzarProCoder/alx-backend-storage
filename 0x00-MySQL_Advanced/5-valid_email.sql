-- SQL trigger to change the attribute valid_email
-- After email update
DELIMITER && ;
CREATE TRIGGER validate BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	IF new.email != old.email THEN
		SET NEW.valid_email = 0;
END IF;
END;&&
delimiter ;
