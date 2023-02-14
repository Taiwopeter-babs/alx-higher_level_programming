-- retrieve data with name value, excluding NULL name values
SELECT score, name FROM second_table
	WHERE name IS NOT NULL
	ORDER BY score DESC;
