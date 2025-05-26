from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = 'sqlite:///./admission.db' #sqlite is file-base database

engin = create_engine(DATABASE_URL, connect_args={'check_same_thread': False}) #connect app to db

sessionLocal = sessionmaker(bind=engin, autoflush=False, autocommit=False) #used to make DB queries and insertion..

Base = declarative_base() #track all model with base

def create_tables():
    Base.metadata.create_all(bind=engin)