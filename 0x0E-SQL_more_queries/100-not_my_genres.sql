-- Retrieve distinct query results
SELECT DISTINCT tg.name
 FROM tv_genres tg
 LEFT JOIN tv_show_genres tsg
 ON tg.id = tsg.genre_id
 WHERE tg.id NOT IN
 	(SELECT tg.id
	  FROM tv_genres tg
	  LEFT JOIN tv_show_genres tsg
	  ON tg.id = tsg.genre_id
	  LEFT JOIN tv_shows ts
	  ON ts.id = tsg.show_id
	  WHERE ts.title = "Dexter")
 ORDER BY tg.name;
	 

