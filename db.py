from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///sqlalchemy.sqlite', echo=True)

base = declarative_base()

class player(base):

    __tablename__ = 'player'

    player_id = Column(Integer, primary_key=True) 
    pet_name = Column(String)
    steps = Column(Integer)
    calories = Column(Integer)
    sleep = Column(Integer)
    reps = Column(Integer)

    def __init__(self, player_id, pet_name, steps, calories, sleep, reps):
        self.player_id = player_id
        self.pet_name = pet_name
        self.steps = steps
        self.calories = calories
        self.sleep = sleep
        self.reps = reps


base.metadata.create_all(engine)
