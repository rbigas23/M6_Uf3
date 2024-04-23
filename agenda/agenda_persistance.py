from global_imports import pymongo, ObjectId, datetime, event, agenda, peer
from i_agenda_persistance import i_agenda_persistance


class agenda_persistance(i_agenda_persistance):
    
    def __init__(self):
        self.peer = peer("agendas")

    def create_agenda(self, agenda):  # Crea una aguenda en la colección pasándole los datos por un diccionario
        result = self.collection.insert_one({agenda.__dict__})
        return result.acknowledged
    
    def show_agenda(self, name):  # Muestra los datos de un agenda pasándole su nombre
        return self.collection.find_one({'name': name}) 
    
    def edit_agenda(self, name , new_data):  # Edita un evento segun el título indicado y modifica sus datos con el diccionario indicado
        result = self.collection.update_one({'name': name}, {'$set': new_data})
        return result.modified_count

agenda_col_handler = peer("agendas")

e1 = event(datetime.date(2024, 6, 15).isoformat(), datetime.timedelta(hours = 3600).seconds, "Traumatólogo", "Visita con el trauma hehe.", 0, "41.390753, 2.173127")
e2 = event(datetime.date(2024, 5, 23).isoformat(), datetime.timedelta(hours = 3600).seconds, "Examen M06", "L'examen més difícil de la història", 1, "41.390753, 2.173127")
e3 = event(datetime.date(2025, 3, 11).isoformat(), datetime.timedelta(hours = 3600).seconds, "Cumple Roc", "Mi cumple!!", 2, "41.390753, 2.173127")

uid1 = ObjectId("6627f4b85a1a64b62936c5db")
uid2 = ObjectId("6627f4b95a1a64b62936c5dc")
uid3 = ObjectId("6627f4b95a1a64b62936c5dd")

a1 = agenda("Practica 1", [e1, e2, e3], [uid1, uid2, uid3])

agenda_col_handler.create_agenda(a1)
agenda_col_handler.show_agenda()