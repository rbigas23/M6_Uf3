import unittest
from event import event
from mongodb_persistance import mongodb_persistance
from global_imports import pymongo
import datetime

class test(unittest.TestCase):
    
    def __init__(self):
        self.db_handler = mongodb_persistance(pymongo.MongoClient("mongodb+srv://tese:1234@cluster0.0xtd9rf.mongodb.net/?retryWrites=true&w=majority"), "eventos")    
        self.e1 = event(datetime.date(2024, 6, 15).isoformat(), datetime.timedelta(hours = 3600).seconds, "Traumatólogo", "Visita con el trauma hehe.", 0, "41.390753, 2.173127")
        self.e2 = event(datetime.date(2024, 5, 23).isoformat(), datetime.timedelta(hours = 3600).seconds, "Examen M06", "L'examen més difícil de la història", 1, "41.390753, 2.173127")
        self.e3 = event(datetime.date(2025, 3, 11).isoformat(), datetime.timedelta(hours = 3600).seconds, "Cumple Roc", "Mi cumple!!", 2, "41.390753, 2.173127")
    
    def print_result(self, test_name):
        print(f"{test_name} completado correctamente.")
        
    def create_test(self):
        
        e1_inserted = self.db_handler.create_event(self.e1)
        e2_inserted = self.db_handler.create_event(self.e2)
        e3_inserted = self.db_handler.create_event(self.e3)
        
        self.assertTrue(e1_inserted and e2_inserted and e3_inserted)  # Si pasa el test, el codi continúa. Sino, dona error.
        
        self.print_result("Test de creación de eventos")

    def show_test(self):
        e1_show = self.db_handler.show_event("Cumple Roc")
        e2_show = self.db_handler.show_event("Traumatólogo")
        e3_show = self.db_handler.show_event("Examen M06")
        
        self.assertTrue(e1_show and e2_show and e3_show)  # Comproba si retorna un diccionari amb contingut (True) o si està buit (False)
        
        self.print_result("Test de mostrado de eventos")
        
    def edit_test(self):
        e1_edit = self.db_handler.edit_event("Cumple Roc", {"description": "Nueva descripción"})
        e2_edit = self.db_handler.edit_event("Traumatólogo", {"description": "Nueva descripción"})
        e3_edit = self.db_handler.edit_event("Examen M06", {"description": "Nueva descripción"})

        self.assertTrue(e1_edit == 1 and e2_edit == 1 and e3_edit == 1)  # Comproba que es modifiqui el registre comparant el modified_count amb un 1
        
        self.print_result("Test de edición de eventos")
        
    def delete_test(self):
        e1_delete = self.db_handler.delete_event("Cumple Roc")
        e2_delete = self.db_handler.delete_event("Traumatólogo")
        e3_delete = self.db_handler.delete_event("Examen M06")

        self.assertTrue(e1_delete == 1 and e2_delete == 1 and e3_delete == 1)  # Comproba que s'esborri el registre comparant el deleted_count amb un 1
        
        self.print_result("Test de eliminación de eventos") 

# t = test()

# t.create_test()
# t.show_test()
# t.edit_test()
# t.delete_test()
