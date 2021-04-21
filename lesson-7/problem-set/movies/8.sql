select people.name
from movies
join stars on movies.id = stars.movie_id
join people on people.id = stars.person_id
where movies.title = "Toy Story"