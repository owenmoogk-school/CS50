select distinct(people.name)
from stars join people on stars.person_id = people.id
where movie_id in(
    select movie_id
    from people join stars on stars.person_id = people.id
    where birth = 1958 and name = 'Kevin Bacon'
)
and name != 'Kevin Bacon'