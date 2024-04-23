
from global_imports import pymongo, ObjectId, datetime, event, agenda, peer
from i_user_persistance import i_user_persistance

class user_persistance(i_user_persistance):
    
    def __init__(self):
        self.peer = peer("usuarios")

    def create_user(self, name):  # Crea un usuario en la colección con la id autoincremental y solo definendo el nombre
        result = self.collection.insert_one({'name': name})
        return result.acknowledged
    
    def show_user(self, name): # Muestra los datos de un usuario pasandole su nombre
        return self.collection.find_one({'name': name})
    
    def edit_user(self, name, new_name): # Edita un usario segun el nombre indicado y modifica sus datos con el diccionario indicado
        result = self.collection.update_one({'name': name}, {'$set': {'name': new_name}})
        return result.modified_count

user_col_handler = mongodb_persistance("usuarios")
agenda_col_handler = mongodb_persistance("agendas")

user_col_handler.create_user("Roc Bigas Ortuño")
user_col_handler.create_user("Pau Insa Delgado")
user_col_handler.create_user("Tese Orlando Araujo Sagardoy")
print(user_col_handler.show_user("Roc Bigas Ortuño"))
print(user_col_handler.edit_user("Roc Bigas Ortuño", "Rooooc Bigas Ortuño"))


e1 = event(datetime.date(2024, 6, 15).isoformat(), datetime.timedelta(hours = 3600).seconds, "Traumatólogo", "Visita con el trauma hehe.", 0, "41.390753, 2.173127")
e2 = event(datetime.date(2024, 5, 23).isoformat(), datetime.timedelta(hours = 3600).seconds, "Examen M06", "L'examen més difícil de la història", 1, "41.390753, 2.173127")
e3 = event(datetime.date(2025, 3, 11).isoformat(), datetime.timedelta(hours = 3600).seconds, "Cumple Roc", "Mi cumple!!", 2, "41.390753, 2.173127")

uid1 = ObjectId("6627f4b85a1a64b62936c5db")
uid2 = ObjectId("6627f4b95a1a64b62936c5dc")
uid3 = ObjectId("6627f4b95a1a64b62936c5dd")

a1 = agenda("Practica 1", [e1, e2, e3], [uid1, uid2, uid3])

agenda_col_handler.create_agenda(a1)
agenda_col_handler.show_agenda()
