import os
from datetime import datetime
from sqlalchemy import create_engine, Table, Column, Integer, String, DateTime, Date, Time, ForeignKey, event, ARRAY, TupleType
from sqlalchemy.orm import scoped_session, sessionmaker, backref, relation, relationship
from sqlalchemy.ext.declarative import declarative_base

base_dir = os.path.join(os.path.abspath(os.curdir), 'instance')
engine = create_engine(f'sqlite:///{base_dir}/development.db', echo=True)

if os.getenv('environment') in 'development':
    engine = create_engine('mysql://<username>:<password>@<host>:<port>/<databasename>[?<options>]', echo=True)
elif os.getenv('environment') in 'production':
    engine = create_engine('mysql://<username>:<password>@<host>:<port>/<databasename>[?<options>]')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine
                                         )
                            )


def init_db():
    Model.metadata.create_all(bind=engine)


Model = declarative_base(name='Model')
Model.query = db_session.query_property()
