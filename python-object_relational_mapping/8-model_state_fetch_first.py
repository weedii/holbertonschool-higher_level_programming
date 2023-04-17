#!/usr/bin/python3

"""script that prints the first State object from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    db_user = sys.argv[1]
    db_pass = sys.argv[2]
    db_name = sys.argv[3]
    db_host = "localhost"
    db_port = 3306

    engine = create_engine(
        f"mysql+mysqldb://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}")

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    session = Session()

    first_state = session.query(State).order_by(State.id).first()

    print(f"{first_state.id}: {first_state.name}")

    session.close()
