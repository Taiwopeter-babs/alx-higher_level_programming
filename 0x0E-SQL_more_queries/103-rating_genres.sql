-- Use PK & FK to retrieve values
SELECT tg.name, SUM(tsr.rate) AS "rating"
 FROM tv_genres tg
 	LEFT JOIN tv_show_genres tsg
 		ON tg.id = tsg.genre_id
 	LEFT JOIN tv_shows ts
 		ON ts.id = tsg.show_id
 	LEFT JOIN tv_show_ratings tsr
 		ON ts.id = tsr.show_id
 GROUP BY tg.name
 ORDER BY rating DESC;
