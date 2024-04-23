import datetime
from user import user
from global_imports import json, ObjectId
from event import event

class agenda():
    
    def __init__(self, name, events, user_ids):
        self.name     = name
        self.events   = events
        self.user_ids = user_ids

    def __repr__(self):
        return f"agenda(events=[{", ".join(repr(event) for event in self.events)}], users=[{", ".join(repr(user) for user in self.user_ids)}])"

e1 = event(datetime.date(2024, 6, 15).isoformat(), datetime.timedelta(hours = 3600).seconds, "Traumatólogo", "Visita con el trauma hehe.", 0, "41.390753, 2.173127")
e2 = event(datetime.date(2024, 5, 23).isoformat(), datetime.timedelta(hours = 3600).seconds, "Examen M06", "L'examen més difícil de la història", 1, "41.390753, 2.173127")
e3 = event(datetime.date(2025, 3, 11).isoformat(), datetime.timedelta(hours = 3600).seconds, "Cumple Roc", "Mi cumple!!", 2, "41.390753, 2.173127")

uid1 = ObjectId("6627f4b85a1a64b62936c5db")
uid2 = ObjectId("6627f4b95a1a64b62936c5dc")
uid3 = ObjectId("6627f4b95a1a64b62936c5dd")

a1 = agenda([e1, e2, e3], [uid1, uid2, uid3])

print(a1)