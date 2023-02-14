-- Alter unicode of database, table and column
-- database
ALTER DATABASE hbtn_0c_0 COLLATE utf8mb4_unicode_ci;

-- table => `first_table`
ALTER TABLE hbtn_0c_0.first_table CONVERT TO CHARACTER SET utf8
	COLLATE utf8mb4_unicode_ci;

-- column => `name`
ALTER TABLE hbtn_0c_0.first_table MODIFY name VARCHAR(256) COLLATE utf8mb4_unicode_ci;
