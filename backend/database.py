import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# from google.cloud.sql.connector import Connector

load_dotenv()

#PostgreSQL connection
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, 
                      pool_size=5,
                      max_overflow=50,
                      pool_timeout=30,
                      pool_recycle=1800,
                      )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

#Cloud SQL connection

# DB_USER = os.getenv("DB_USER")
# DB_PASSWORD = os.getenv("DB_PASSWORD")
# DB_NAME = os.getenv("DB_NAME")
# INSTANCE_CONNECTION_NAME = os.getenv("INSTANCE_CONNECTION_NAME")

# def getconn():
#     connector = Connector()
#     conn = connector.connect(
#         INSTANCE_CONNECTION_NAME,
#         "pg8000",
#         user=DB_USER,
#         password=DB_PASSWORD,
#         db=DB_NAME
#     )
#     return conn

# # Create the SQLAlchemy engine
# engine = create_engine(
#     "postgresql+pg8000://",
#     creator=getconn,
# )

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()