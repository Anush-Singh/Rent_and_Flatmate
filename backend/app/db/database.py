from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import urllib

connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=RentFlatmateDB;"
    "Trusted_Connection=yes;"
)

connection_url = urllib.parse.quote_plus(connection_string)

DATABASE_URL = f"mssql+pyodbc:///?odbc_connect={connection_url}"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()