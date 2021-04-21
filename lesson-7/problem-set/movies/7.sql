select title, rating
from ratings
join movies on movies.id = ratings.movie_id
where year = 2010 and rating > 0
order by rating