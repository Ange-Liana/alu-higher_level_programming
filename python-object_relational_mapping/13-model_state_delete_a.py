#!/usr/bin/python3
"""Deletes states containing the letter 'a'."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}",
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # IMPORTANT: fetch ALL matching states first
    states = session.query(State)\
        .filter(State.name.like('%a%'))\
        .all()

    # delete all of them
    for state in states:
        session.delete(state)

    session.commit()
    session.close()
