from sqlalchemy import Boolean, Column, Integer, String
from db import Base


class Details(Base):
    """
    This is a model class. which is having the movie table structure with all the constraint
    """
    __tablename__ = "Adresses"

    names = Column(String,primary_key=True) # it always should have primary key

    address = Column(String(255))
    phone_numbers = Column(String(255))
