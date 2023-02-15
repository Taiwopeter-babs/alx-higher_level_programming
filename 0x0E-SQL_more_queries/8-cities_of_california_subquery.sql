-- use subqueries to retrieve data from tables
SELECT cities.id, cities.name
FROM cities
WHERE cities.state_id =
	(SELECT st.id
	FROM states st
	WHERE st.name = "California");

