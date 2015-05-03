CREATE TABLE cup_matches (
	mid serial PRIMARY KEY,
	round varchar(20),
	year integer ,
	num_ratings integer ,
	rating real
);

CREATE TABLE played_in(
	mid integer references cup_matches(mid),
	name varchar(80) ,
	year integer ,
	position integer ,
	PRIMARY KEY(mid,name)

);

-- A.1

EXPLAIN SELECT * from played_in WHERE position=1;

-- A.3

CREATE INDEX position_index ON played_in(position);

-- B.1

SELECT * from played_in WHERE name like '%pele%';


-- B.3

CREATE INDEX name_index ON played_in(name);
