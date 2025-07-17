USE moviesdb;
select * from movies;
select * from movies where industry = "Bollywood";
select count(*) from movies where industry = "HOllywood";
select * from movies where title like "%THOR%";
SELECT * FROM movies where studio like "" ;
select * from movies where imdb_rating >=7 and imdb_rating<=9;
select * from movies where imdb_rating between 8 and 9;
select * from movies where release_year = 2022 or release_year = 2019 or release_year = 2018;
select * from movies where release_year in (2022,2019,2018);
select * from movies where imdb_rating is null;
select * from movies where imdb_rating is not null;
select * from movies where industry = "Bollywood" order by imdb_rating desc;
select * from movies where industry = "Bollywood" order by imdb_rating desc limit 5;
select * from movies where industry = "Bollywood" order by imdb_rating desc limit 5 offset 2;
select * from movies where industry = "Bollywood" order by imdb_rating;
select 
max(imdb_rating) as max_rating,
min(imdb_rating) as min_rating,
round(avg(imdb_rating),2)as avg_rating 
from movies where industry = "Hollywood";
select studio,count(*) as cnt from movies group by studio 
order by cnt desc;
select industry, count(industry) as cnt, round(avg(imdb_rating),2) as avg_rating from movies group by industry;
# Having   from ---> where ---> group by ---> having ---> order by
# the element target by having is in the select line but for where nothing required
select release_year, count(*) as movies_count from movies group by release_year having movies_count > 2 order by movies_count desc;

# FINANTIALS 
select *, (revenue - budget) as profit from financials;
SELECT 
  *,
  
  -- Normalize revenue and budget based on 'unit'
  CASE 
    WHEN unit = 'Billons' THEN 1000 * revenue 
    WHEN unit = 'Thousands' THEN ROUND(revenue / 1000, 2) 
    ELSE revenue 
  END AS normalized_revenue,

  CASE 
    WHEN unit = 'Billons' THEN 1000 * budget 
    WHEN unit = 'Thousands' THEN ROUND(budget / 1000, 2) 
    ELSE budget 
  END AS normalized_budget,

  -- Convert profit to INR based on currency
  CASE 
    WHEN currency = 'USD' THEN 83 * (revenue - budget)
    ELSE (revenue - budget)
  END AS profit_inr

FROM financials;

# JOINS
#inner joins bydefault basically intersection
# left join inplace left join and it also includes left database data
# left join inplace right join and it also includes right database data
select 
	m.movie_id, title, budget, revenue, currency, unit
from movies m
join financials f
on m.movie_id = f.movie_id;

# when same columns name we used to join
select 
	movie_id, title, budget, revenue, currency, unit
from movies 
right join financials 
using(movie_id);
# full join
#outer join ---> left, right & full join
select 
	m.movie_id, title, budget, revenue, currency, unit
from movies m
left join financials f
on m.movie_id = f.movie_id

union

select 
	f.movie_id, title, budget, revenue, currency, unit
from movies m
right join financials f
on m.movie_id = f.movie_id;