import datetime
from user import user
from global_imports import json
from event import event

class agenda():
    
    def __init__(self, events, users):
        self.events = events
        self.users  = users


    def to_json(self):
        return json.dumps(self.__dict__, indent=4)

e1 = event(datetime.date(2024, 6, 15).isoformat(), datetime.timedelta(hours = 3600).seconds, "Traumatólogo", "Visita con el trauma hehe.", 0, "41.390753, 2.173127")
e2 = event(datetime.date(2024, 5, 23).isoformat(), datetime.timedelta(hours = 3600).seconds, "Examen M06", "L'examen més difícil de la història", 1, "41.390753, 2.173127")
e3 = event(datetime.date(2025, 3, 11).isoformat(), datetime.timedelta(hours = 3600).seconds, "Cumple Roc", "Mi cumple!!", 2, "41.390753, 2.173127")
edging = agenda([e1, e2, e3], [["Roc Bigas Ortuño", "POLLA GORDA"],["Tese Orlando"]])

print(edging.to_json())