-- Query database for tv shows genres and name
SELECT tvs.title, tsg.genre_id
FROM tv_shows tvs
LEFT JOIN tv_show_genres tsg
ON tvs.id = tsg.show_id
WHERE tsg.genre_id IS NOT NULL
ORDER BY tvs.title, tsg.genre_id;
