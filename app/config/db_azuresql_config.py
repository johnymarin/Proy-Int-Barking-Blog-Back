import urllib
import os


from sqlalchemy import create_engine,MetaData



server = "ec2-3-209-65-193.compute-1.amazonaws.com"
database = "d9nn55o8s8kmda"
username = "rwnythmvtembhp"
password = "cfe9c5889071b376c6749fa3c2711364b5699b2ece5e8542ca0204cceecc245a"
port = "5432"


#params = urllib.parse.quote_plus("'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password")
#engine = create_engine(f"mssql+pymssql://{username}@{SQLservername}:{password}@{server}")
engine = create_engine(f"postgresql+asyncpg://{username}:{password}@{server}:{port}/{database}")
meta = MetaData()
#meta.reflect(bind=engine)

#print(engine.table_names())
#print(meta.tables.keys())
#for table in meta.sorted_tables:
#    print(table)

azuresql_conn = engine.connect()
