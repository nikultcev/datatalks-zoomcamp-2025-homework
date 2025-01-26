import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus
from dotenv import load_dotenv
import os
from time import time
import requests

def download_source(files):

    for file in files:
        file_url = file['url']
        file_name = file['name']

        with open(file_name, 'wb') as file_out:
            file_bytes = requests.get(file_url, stream=True).content
            file_out.write(file_bytes)

def main():

    files_to_download = [
    {'url':'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-10.csv.gz',
     'name':'trips.csv.gz'},
     {'url':'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv',
      'name':'zones.csv'}]

    download_source(files_to_download)

    load_dotenv()

    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = quote_plus(os.getenv("DB_PASSWORD"))
    DB_ADDRESS = os.getenv("DB_ADDRESS")
    DB_PORT = os.getenv("DB_PORT")
    DB_DATABASE = os.getenv("DB_DATABASE")

    print(DB_USER, DB_PASSWORD, DB_ADDRESS, DB_PORT, DB_DATABASE)


    db_engine = create_engine(
        f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_ADDRESS}:{DB_PORT}/{DB_DATABASE}'
    )

    columns_to_datetime = ['lpep_pickup_datetime','lpep_dropoff_datetime']

    trips = pd.read_csv('trips.csv.gz',compression="gzip",chunksize=100000,parse_dates=columns_to_datetime)

    trips.get_chunk(1).to_sql(con=db_engine,name='trips',if_exists='replace')

    for t in trips:
        i_start = time()

        t.to_sql(con=db_engine,name='trips',if_exists='append')

        i_end = time()
        print("Succesfully inserted {} rows in {:.2f} seconds".format(len(t),i_end-i_start))

    zones = pd.read_csv('zones.csv')
    zones.to_sql(con=db_engine,name='zones',if_exists='replace')

if __name__=='__main__':
    main()