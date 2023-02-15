-- Retrieve distinct query results
SELECT DISTINCT ts.title
 FROM tv_shows ts
 LEFT JOIN tv_show_genres tsg
 ON ts.id = tsg.show_id
 WHERE ts.id NOT IN
 	(SELECT ts.id
	  FROM tv_shows ts
	  LEFT JOIN tv_show_genres tsg
	  ON ts.id = tsg.show_id
	  LEFT JOIN tv_genres tg
	  ON tg.id = tsg.genre_id
	  WHERE tg.name = "Comedy")
 ORDER BY ts.title;
	 

