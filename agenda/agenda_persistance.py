from i_agenda_persistance import i_agenda_persistance
from peer import peer


class agenda_persistance(i_agenda_persistance):
    
    def __init__(self):
        self.peer = peer("agendas")

    def create_agenda(self, agenda):  # Crea una agenda en la colección pasándole un objeto agenda
        result = self.peer.collection.insert_one(agenda.__dict__)
        return result.acknowledged
    
    def show_agenda(self, name):  # Muestra los datos de un agenda pasándole su nombre
        return self.peer.collection.find_one({'name': name})
    
    def edit_agenda(self, name , new_data):  # Edita una agenda segun el nombre indicado y modifica sus datos con el diccionario indicado
        result = self.peer.collection.update_one({'name': name}, {'$set': new_data})
        return result.modified_count
