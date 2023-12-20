-- Will list every show in hbtn_0d_tvshows DB by their ratings.

-- lists every record of a table by addition of linked record.
SELECT title, SUM(tv_show_ratings.rate) 'rating'
FROM tv_shows
LEFT JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_shows.id
GROUP BY title
ORDER BY rating DESC;
