#!/usr/bin/python3

"""script that changes the name of a State
            object from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    db_user = sys.argv[1]
    db_pass = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{db_user}:{db_pass}@localhost:{3306}/{db_name}")

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()

    state = session.query(State).filter(State.id == 2).one()
    state.name = "New Mexico"
    session.commit()

    session.close()
