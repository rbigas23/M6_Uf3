from i_user_persistance import i_user_persistance
from peer import peer


class user_persistance(i_user_persistance):
    
    def __init__(self):
        self.peer = peer("usuarios")

    def create_user(self, name):  # Crea un usuario en la colección a partir del nombre indicado (su id es generada por MongoDB)
        result = self.peer.collection.insert_one({'name': name})
        return result.acknowledged
    
    def show_user(self, name): # Muestra los datos de un usuario pasándole su nombre
        return self.peer.collection.find_one({'name': name})
    
    def edit_user(self, name, new_name): # Edita un usario segun el nombre indicado y modifica sus datos con el diccionario indicado
        result = self.peer.collection.update_one({'name': name}, {'$set': {'name': new_name}})
        return result.modified_count
