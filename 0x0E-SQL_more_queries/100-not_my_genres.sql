-- script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter.
-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 16-shows_by_genre.sql)
SELECT tv_genres.name
FROM tv_genres
LEFT JOIN (
    SELECT DISTINCT g.id
    FROM tv_genres g
    INNER JOIN tv_show_genres s ON g.id = s.genre_id
    INNER JOIN tv_shows t ON s.show_id = t.id
    WHERE t.title = "Dexter"
) AS linked_genres ON tv_genres.id = linked_genres.id
WHERE linked_genres.id IS NULL
ORDER BY tv_genres.name;
