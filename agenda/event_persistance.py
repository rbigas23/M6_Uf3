from i_event_persistance import i_event_persistance
from peer import peer
class event_persistance(i_event_persistance):
    
    def __init__(self):
        self.peer = peer("eventos")
    
    def create_event(self, event):  # Crea un evento en la colección pasándole los datos por un diccionario
        result = self.peer.collection.insert_one(event.__dict__)
        return result.acknowledged
    
    def show_event(self, event_title):  # Muestra los datos de un evento pasándole su título
        return self.peer.collection.find({'title': event_title})
    
    def edit_event(self, event_title , new_data):  # Edita un evento segun el título indicado y modifica sus datos con el diccionario indicado
        result = self.peer.collection.update_one({'title': event_title}, {'$set': new_data})
        return result.modified_count
    
    def delete_event(self, event_title):  # Elimina un evento segun el titulo indicado
        result = self.peer.collection.delete_one({'title': event_title})
        return result.deleted_count


# e1 = event(datetime.date(2024, 6, 15).isoformat(), datetime.timedelta(hours = 3600).seconds, "Traumatólogo", "Visita con el trauma hehe.", 0, "41.390753, 2.173127")
# print(mongodb_persistance(pymongo.MongoClient("mongodb+srv://tese:1234@cluster0.0xtd9rf.mongodb.net/?retryWrites=true&w=majority"), "eventos").edit_event("Traumatólogo", {"description":"CAMBIO CAMBIO CAMBIO"}))
# docs = mongodb_persistance(pymongo.MongoClient("mongodb+srv://tese:1234@cluster0.0xtd9rf.mongodb.net/?retryWrites=true&w=majority"), "eventos").show_event("FOLLADITA RICA")
# for doc in docs:
#     print(doc)
