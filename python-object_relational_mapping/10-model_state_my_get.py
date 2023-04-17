#!/usr/bin/python3

"""script that prints the State object with the
            name passed as argument from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    db_user = sys.argv[1]
    db_pass = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine(
        f"mysql+mysqldb://{db_user}:{db_pass}@localhost:{3306}/{db_name}")

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()

    state = session.query(State).filter(State.name == state_name).first()

    if state:
        print(f"{state.id}")
    else:
        print("Not found")

    session.close()
