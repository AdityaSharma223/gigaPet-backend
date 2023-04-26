import db
from sqlalchemy.orm import Session, sessionmaker
Session = sessionmaker(bind=db.engine)
session = Session()

for i in session.query(db.player).all():
    print(i.player_id, i.pet_name, i.steps, i.calories, i.sleep, i.reps)
