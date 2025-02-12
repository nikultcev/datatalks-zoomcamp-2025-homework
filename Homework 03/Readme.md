## Question 1
```SQL
SELECT
  count(*)
FROM `datatalks-zoomcamp-2025.datatalks_zoomcamp2025_homework_03.yellow_taxi_data`
```
## Question 2
```SQL
SELECT
  COUNT(DISTINCT PULocationID)
FROM `datatalks-zoomcamp-2025.datatalks_zoomcamp2025_homework_03.yellow_taxi_data_materialized`

SELECT
  COUNT(DISTINCT PULocationID)
FROM `datatalks-zoomcamp-2025.datatalks_zoomcamp2025_homework_03.yellow_taxi_data`
```
## Question 3
```SQL
SELECT
  PULocationID
FROM `datatalks-zoomcamp-2025.datatalks_zoomcamp2025_homework_03.yellow_taxi_data_materialized`

SELECT
  PULocationID,
  DOLocationID
FROM `datatalks-zoomcamp-2025.datatalks_zoomcamp2025_homework_03.yellow_taxi_data_materialized`
```
## Question 4
```SQL
SELECT
  count(*)
FROM `datatalks-zoomcamp-2025.datatalks_zoomcamp2025_homework_03.yellow_taxi_data_materialized`
where fare_amount=0
```
## Question 5
```SQL
create or replace table `datatalks_zoomcamp2025_homework_03.yellow_taxi_data_partitioned`
partition by date(tpep_dropoff_datetime)
cluster by VendorID
as
  select * from `datatalks_zoomcamp2025_homework_03.yellow_taxi_data_materialized`
```
## Question 6
```SQL
select
  distinct VendorID
from `datatalks_zoomcamp2025_homework_03.yellow_taxi_data_materialized`
where tpep_dropoff_datetime > '2024-03-01' and  tpep_dropoff_datetime <= '2024-03-15'

select
  distinct VendorID
from `datatalks_zoomcamp2025_homework_03.yellow_taxi_data_partitioned`
where tpep_dropoff_datetime > '2024-03-01' and  tpep_dropoff_datetime <= '2024-03-15'
```