FROM python:latest

RUN pip install pandas 
RUN pip install requests
RUN pip install python-dotenv 
RUN pip install sqlalchemy 
RUN pip install psycopg2

WORKDIR /app
COPY data_ingestion.py data_ingestion.py
COPY .env .env

ENTRYPOINT [ "python","data_ingestion.py" ]