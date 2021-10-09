import urllib
import os


from sqlalchemy import create_engine,MetaData

os.environ['http_proxy'] = os.environ.get('IPB_HTTP', '')
os.environ['https_proxy'] = os.environ.get('IPB_HTTPS', '')

server = "udeademodbserver.database.windows.net"
database = "udeademodb"
username = "hkudeabdlab2021"
password = "PHoXBJpBKqRI5"


#params = urllib.parse.quote_plus("'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password")
#engine = create_engine(f"mssql+pymssql://{username}@{SQLservername}:{password}@{server}")
engine = create_engine(f"mssql+pymssql://{username}:{password}@{server}/{database}")
meta = MetaData()
#meta.reflect(bind=engine)

#print(engine.table_names())
#print(meta.tables.keys())
#for table in meta.sorted_tables:
#    print(table)

azuresql_conn = engine.connect()
