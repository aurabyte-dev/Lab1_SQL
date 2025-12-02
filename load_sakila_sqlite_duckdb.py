import dlt
from dlt.sources.sql_database import sql_database
from pathlib import Path

# Setting up paths
DATA_PATH = Path(__file__).parent / "data" # finds the folder where this py file lives and look inside it's data folder
SQLITE_PATH = DATA_PATH / "sqlite-sakila.db" # source path    
DUCKDB_PATH = DATA_PATH / "sakila.duckdb" # destination path

# Connecting to the source databse
source = sql_database(credentials=f"sqlite:///{SQLITE_PATH}", schema="main")

# Create the pipeline
pipeline = dlt.pipeline(
    pipeline_name="sakila_sqlite_duckdb", # pipeline name
    destination=dlt.destinations.duckdb(str(DUCKDB_PATH)), # which databse to MOVE the data to
    dataset_name="staging", # at the destination, put all the data in a folder called staging
    )

# Move tha data
load_info = pipeline.run(source, write_disposition="replace")
# run(source) = start moving the data
# write_disposition="replace" = If tables already exist at the destination, DELETE them and replace with fresh data

print(load_info)