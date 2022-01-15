
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./address_database.db"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# bind – An optional Connectable, will be assigned the bind attribute on the MetaData instance.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# A simple constructor that allows initialization from kwargs.
Base = declarative_base()