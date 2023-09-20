from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.ext.declarative import declarative_base

# Define Database Models
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    country_of_residence = Column(String, nullable=False)

    driver_id = Column(Integer, ForeignKey('drivers.id'),nullable=True)
    driver = relationship("Driver") #defines one to many relations

class Driver(Base):
    __tablename__ = 'drivers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    car_make_model = Column(String, nullable=False)
    rating = Column(Float)
    seats_available = Column(Integer, nullable=False)
    seats_taken = Column(Integer, default=1)
    current_route_id = Column(Integer, ForeignKey('hitch_routes.id'))