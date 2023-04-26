import re
import db
from sqlalchemy.orm import sessionmaker
import random

Session = sessionmaker(bind=db.engine)
session = Session()

for i in range(10):

    pet_name = f"coco_{i}"
    steps = random.randint(10, 100)
    calories = random.randint(10, 1000)
    sleep = random.randint(0, 8)
    reps = random.randint(10, 100)

    player = db.player(i, pet_name, steps, calories, sleep, reps)
    session.add(player)

session.commit()
