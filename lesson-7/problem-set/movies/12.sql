select movies.title
from people
join stars on stars.person_id = people.id
join movies on movies.id = stars.movie_id
join ratings on ratings.movie_id = movies.id
where people.name = "Johnny Depp"

Intersect

select movies.title
from people
join stars on stars.person_id = people.id
join movies on movies.id = stars.movie_id
join ratings on ratings.movie_id = movies.id
where people.name = "Helena Bonham Carter"