-- Retrieve genre and number of shows linked to it
SELECT tvg.name AS "genre", COUNT(tsg.genre_id) AS "number_of_shows"
FROM tv_genres tvg
LEFT JOIN tv_show_genres tsg
ON tvg.id = tsg.genre_id
WHERE tsg.genre_id IS NOT NULL
GROUP BY genre
ORDER BY number_of_shows DESC;
