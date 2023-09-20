#we're going to do a text interface for now with some extensive documentation
from database import session
from schema import Base, User, Driver, HitchRoute

#used to manipulate database, add new Users   
while True:
    inp = input(" uHitch Interface:")
    try:
        if inp == "close":
            session.close()
            quit()
        eval(inp)
    except Exception as e:
        print(e)


