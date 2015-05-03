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

-- B.5

SET enable_seqscan = off; -- Y U NO USE MY INDEX ?
EXPLAIN SELECT * from played_in WHERE name like '%pele%';

-- C.1

EXPLAIN SELECT * from cup_matches WHERE rating*3 > 20;

-- C.3

CREATE INDEX rating_index ON cup_matches(rating);

-- D.1

EXPLAIN SELECT * from cup_matches, played_in WHERE cup_matches.year=played_in.year;

-- D.2

CREATE INDEX year_index ON cup_matches(year) ;

-- D.4

CREATE INDEX year_index_played_in ON played_in(year);

-- D.5

SET enable_seqscan = OFF ;

EXPLAIN SELECT * from cup_matches, played_in WHERE cup_matches.year=played_in.year;
