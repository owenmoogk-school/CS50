select people.name, people.birth
from people
join stars on stars.person_id = people.id
join movies on movies.id = stars.movie_id
where movies.year = 2004

-- removing duplicates
group by people.name, people.id

order by people.birth