# Docker Compose Data Pipeline
In one docker compose file we initialize PostgeSQL database, PGAdmin and launch a Python script to download and put csv data into the DB. Put your credentials into .env and secrets file

# Homework questions answers
## Question 1. Understanding docker first run
```bash
docker run -it --entrypoint "bash" python:3.12.8
pip --version
```
- 24.3.1
## Question 2. Understanding Docker networking and docker-compose
- postgres:5432
- db:5432
## Question 3. Trip Segmentation Count
```SQL
SELECT 
	case
		when trip_distance <= 1 then 'Up to 1 mile'
		when trip_distance > 1 and trip_distance <= 3 then 'In between 1 (exclusive) and 3 miles (inclusive)'
		when trip_distance > 3 and trip_distance <= 7 then 'In between 3 (exclusive) and 7 miles (inclusive)'
		when trip_distance > 7 and trip_distance <= 10 then 'In between 7 (exclusive) and 10 miles (inclusive)'
		when trip_distance > 10 then 'Over 10 miles'
	end as trip_bin,
	case
		when trip_distance <= 1 then 1
		when trip_distance > 1 and trip_distance <= 3 then 2
		when trip_distance > 3 and trip_distance <= 7 then 3
		when trip_distance > 7 and trip_distance <= 10 then 4
	when trip_distance > 10 then 5
	end as trip_bin_sort,
	count(*)
from trips
where
	lpep_dropoff_datetime >= '2019-10-01'
	and lpep_dropoff_datetime < '2019-11-01'
group by trip_bin,trip_bin_sort
order by trip_bin_sort
```
- 104,802; 198,924; 109,603; 27,678; 35,189
## Question 4. Longest trip for each day
```SQL
select
	lpep_pickup_datetime
from trips
order by trip_distance desc
limit 1
```
- 2019-10-31
## Question 5. Three biggest pickup zones
```SQL
select
	zones."Zone",
	sum(trips.total_amount)
from trips
	left outer join zones on zones."LocationID"=trips."PULocationID"
where
	cast(trips.lpep_pickup_datetime as date) = '2019-10-18'
group by zones."Zone"
having
	sum(trips.total_amount)>13000
order by sum(trips.total_amount) desc
```
- East Harlem North, East Harlem South, Morningside Heights
## Question 6. Largest tip
```SQL
select
	dropoff_zones."Zone"
from trips
	left outer join zones pickup_zones on pickup_zones."LocationID"=trips."PULocationID"
	left outer join zones dropoff_zones on dropoff_zones."LocationID"=trips."DOLocationID"
where
	trips.lpep_pickup_datetime >= '2019-10-01'
	and trips.lpep_pickup_datetime < '2019-11-01'
	and pickup_zones."Zone" = 'East Harlem North'
order by trips.tip_amount desc
limit 1
```
- JFK Airport
