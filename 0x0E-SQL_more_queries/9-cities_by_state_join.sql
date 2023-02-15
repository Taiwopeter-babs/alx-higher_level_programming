-- Join multiple tables
SELECT c.id, c.name, st.name
	FROM cities c
	LEFT JOIN states st
	ON c.state_id = st.id
	ORDER BY c.id;
