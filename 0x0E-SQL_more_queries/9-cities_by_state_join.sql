-- Will list out all the cities in the hbtn_0d_usa DB

-- lists all records of a particular field in a DB
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON states.id = cities.state_id ORDER BY cities.id;
