from sqlalchemy import Column, Integer, String, ARRAY
from config import Base


class Pokedex(Base):
    __tablename__= 'pokedex'

    id = Column(Integer, primary_key=True, index=True)
    pokedex_num = Column(Integer, index=True)
    name = Column(String)
    description = Column(String)
    types = Column(ARRAY(String))
    abilities = Column(ARRAY(String))
    location = Column(String)
