#!/usr/bin/python3
""" script for task 9 """

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    host = 'localhost'
    port = 3306

    engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(
        username, passwd, host, port, db_name),
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    local_session = Session()
    states = local_session.query(State).order_by(State.id.asc()).all()
    local_session.close()

    for state in states:
        print(f"{state.id}: {state.name}")
