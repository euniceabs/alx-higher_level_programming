-- A script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 15-comedy_only.sql)
SELECT t.title, g.name
FROM tv_shows t
LEFT JOIN tv_show_genres s ON t.id = s.show_id
LEFT JOIN tv_genres g ON s.genre_id = g.id
ORDER BY t.title ASC, g.name ASC;
