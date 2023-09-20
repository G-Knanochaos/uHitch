import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from schema import Base, User

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
    user1 = User(username='GKV', password='password', email='robotruleslego@gmail.com', country_of_residence='United States')

    session.add(user1)
    session.commit()

# Query Users
users = session.query(User).all()
for user in users:
    print(f"User ID: {user.id}, Username: {user.username}, Email: {user.email}, Country: {user.country_of_residence}")

# Close the Session
session.close()