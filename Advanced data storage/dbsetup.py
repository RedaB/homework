# dbsetup

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

Base = declarative_base()

class Measurement(Base):
    __tablename__ = 'measurement'
    id = Column(Integer, primary_key=True)
    station =  Column(String(255))
    date = Column(String(255))
    prcp = Column(Float)
    tobs = Column(Integer)

class Stations(Base):
    __tablename__ = 'stations'
    id = Column(Integer, primary_key=True)
    station =  Column(String(255))
    name = Column(String(255))
    latitude = Column(Float)
    longitude = Column(Float)
    elevation = Column(Float)

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
conn = engine.connect()
Base.metadata.create_all(conn)