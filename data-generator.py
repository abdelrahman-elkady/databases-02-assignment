from random import randint
from random import uniform
import csv

# cup_matches table mock

# len(rounds) = 5
rounds = ['32nd', '16th', 'Quarter Final', 'Semi Final', 'Final']

records = []

for i in range(0, 2680):
    record = []

    random_index = randint(0, 4)
    random_year = randint(1980, 2015)
    random_viewers = randint(20000, 90000)
    random_avg_rating = round(uniform(1, 10), 1)

    record.append(rounds[random_index])
    record.append(random_year)
    record.append(random_viewers)
    record.append(random_avg_rating)

    records.append(record)

with open("data-cup-matches.csv", "wb") as file:
    writer = csv.writer(file)
    writer.writerows(records)

# played_in table mock

# some random names to select from !
names = ["Adam Nilson", "William  Phillips", "Stephen  Garcia", "Jeffrey  Patterson", "Matthew  Hernandez", "Bobby  Ross", "Fred  Green", "Henry  Perez", "Willie  Jenkins", "Christopher  Price", "Phillip  Davis", "Jeremy  Evans", "Philip  Lewis", "Peter  Gonzalez", "Steven  Alexander", "Douglas  Simmons", "Craig  Coleman", "Walter  Brown", "Frank  Foster", "Eugene  Thompson", "Wayne  Johnson", "Howard  Clark", "Jose  Baker", "Kenneth  Stewart", "Martin  Hill", "Sean  Sanchez", "Eric  Jones", "Jonathan  Campbell", "Randy  Griffin", "Richard  Young", "Louis  White", "Justin  Hall", "Larry  Adams", "Daniel  Martin", "George  Powell", "John  Peterson", "Ryan  Bailey", "Earl  Scott", "Clarence  Ward", "Mark  Roberts", "Andrew  Rogers", "Carlos  Harris", "Brandon  Morris", "Kevin  Wood", "Lawrence  Walker", "Bruce  Gonzales", "Joseph  Morgan", "Russell  Barnes", "Jason  Diaz", "Joe  Wilson",
         "Gregory  Taylor", "Paul  Russell", "Donald  Bennett", "Ralph  Gray", "Brian  Rodriguez", "Jerry  Watson", "Ernest  Cook", "Robert  Cox", "Joshua  Edwards", "Nicholas  Martinez", "Juan  Richardson", "Alan  King", "Albert  Collins", "Harry  Carter", "Thomas  Moore", "Ronald  Sanders", "Jack  Bell", "Jesse  Turner", "Aaron  Murphy", "Michael  Kelly", "James  Washington", "Terry  Anderson", "Scott  Torres", "Roy  Bryant", "Steve  Ramirez", "Adam  Wright", "Todd  Reed", "Gary  Rivera", "Gerald  Cooper", "Carl  Thomas", "Jimmy  Robinson", "Charles  Hughes", "David  Long", "Chris  Flores", "Victor  Butler", "Shawn  Brooks", "Billy  Henderson", "Keith  Lopez", "Anthony  Perry", "Roger  Jackson", "Harold  James", "Patrick  Parker", "Timothy  Miller", "Raymond  Williams", "Benjamin  Lee", "Samuel  Mitchell", "Dennis  Smith", "Arthur  Nelson", "Edward  Howard", "Johnny  Allen"]


# to not mess with scary references !
records[:] = []

for i in range(0, 58960):
    record = []

    random_index = randint(0, 99)
    random_mid = randint(1, 2860)
    random_year = randint(1980, 2015)
    random_position = randint(1, 16)

    record.append(random_mid)
    record.append(names[random_index])
    record.append(random_year)
    record.append(random_position)

    records.append(record)

for i in range(0, 118):
    random_index = randint(0, 58959)
    records[random_index][1] = "pele"

with open("data-played-in.csv", "wb") as file:
    writer = csv.writer(file)
    writer.writerows(records)
