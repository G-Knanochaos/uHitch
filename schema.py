from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import tools

# Define Database Models
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    country_of_residence = Column(String, nullable=False)

    current_route_id = Column(Integer, ForeignKey('hitch_routes.id'),nullable=True)
    route = relationship("HitchRoute") #defines many to one relationship with driver

class Driver(Base):
    __tablename__ = 'drivers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    car_make_model = Column(String, nullable=False)
    rating = Column(Float)
    seats_available = Column(Integer, nullable=False)
    seats_taken = Column(Integer, default=0)

    current_route_id = Column(Integer, ForeignKey('hitch_routes.id'), nullable = True)

class HitchRoute(Base):
    __tablename__ = 'hitch_routes'

    id = Column(Integer, primary_key=True)
    start_point = Column(String,nullable = False) #JSONify coordinate
    end_point = Column(String, nullable = False) #JSONify coordinate
    current_point = Column(String, nullable = True) #JSONify coordinate
    waypoints = Column(String,nullable = True)
    route = Column(String,nullable = True) #JSONify route

    # Define relationships with driver (1:1)
    driver = relationship("Driver", backref="hitch_routes")

    @classmethod
    def create(session,**kw): #start point and end point is passed in
        current_point = kw[0]
        waypoints = [kw[0],kw[1]]
        route = tools.readable_route(waypoints)
        kw += [current_point,waypoints,route]
        obj = HitchRoute(**kw)
        session.add(obj)
        session.commit()
        

    @classmethod
    def update(id,dict): #start point and end point is passed in
        current_point = kw[0]
        waypoints = [kw[0],kw[1]]
        route = tools.readable_route(waypoints)
        kw += [current_point,waypoints,route]
        obj = cls(**kw)

class QRoute(Base):
    __tablename__ = 'q_routes'

    id = Column(Integer, primary_key=True)
    start_point = Column(String,nullable = False) #JSONify coordinate
    end_point = Column(String, nullable = False) #JSONify coordinate

    @classmethod
    def ()


