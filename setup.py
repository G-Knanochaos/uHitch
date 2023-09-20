import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from schema import Base, User, Driver, HitchRoute
import tools

# Check if the database file already exists
database_exists = os.path.isfile('user_database.db')

# Create Database Engine and Session
engine = create_engine('sqlite:///user_database.db')
if not database_exists:
    Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Create Users and Add to the Database (if needed)
if not database_exists:
    user1 = User(username='GKV', 
                 password='password', 
                 email='robotruleslego@gmail.com', 
                 country_of_residence='United States')
    driver1 = Driver(name = "Angad Batra", 
                    car_make_model="Ferrari",
                    rating = 0.0,
                    seats_available=5,
                    )
    hitch1 = HitchRoute(
        start_point = str(tools.geocode("13524 Village Dr Cerritos, CA 90703","US")),
        end_point = str(tools.geocode("Whitney High School, Shoemaker Avenue, Cerritos, CA","US"))
    )


    session.add(user1)
    session.add(driver1)
    session.add(hitch1)
    session.commit()


# Query Users
GKV = session.query(User).filter_by(username="GKV").all()[0]
ANGAD = session.query(Driver).filter_by(name="Angad Batra").all()[0]
HITCH = session.query(HitchRoute).all()[0]
print(GKV,ANGAD,HITCH.start_point,HITCH.end_point)
# Close the Session
session.close()