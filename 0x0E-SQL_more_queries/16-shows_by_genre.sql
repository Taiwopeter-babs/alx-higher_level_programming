-- Join three tables and retrieve values
SELECT ts.title, tg.name
 FROM tv_genres tg
	 LEFT JOIN tv_show_genres tsg
		ON tg.id = tsg.genre_id
	RIGHT JOIN tv_shows ts
		ON ts.id = tsg.show_id
 ORDER BY ts.title, tg.name;
