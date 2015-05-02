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
