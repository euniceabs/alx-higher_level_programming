-- A script that lists all Comedy shows in the database hbtn_0d_tvshows.
-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 14-my_genres.sql)
SELECT t.title
FROM tv_shows t
JOIN tv_show_genres s ON t.id = s.show_id
JOIN tv_genres g ON s.genre_id = g.id AND g.name = 'Comedy'
ORDER BY t.title;
