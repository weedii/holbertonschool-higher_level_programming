#!/usr/bin/python3

"""script that prints all City objects from the database hbtn_0e_14_usa"""

import sys
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
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

    states_cities_names = session.query(State, City).filter(
        City.state_id == State.id).order_by(City.id)

    for x in states_cities_names:
        print(f"{x.State.name}: ({x.City.id}) {x.City.name}")

    session.close()
