import unittest

from global_imports import ObjectId, event, agenda, datetime, peer

class test(unittest.TestCase):
    
    def __init__(self):
        self.agenda_coll_handler = peer("agendas")  
        
    def print_result(self, test_name):
        print(f"{test_name} completado correctamente.")
    
    def create_user_test(self):
        u1 = user(1,Roc)
        u1_inserted = self.db_handler.create_user("Pau")
        u2_inserted = self.db_handler.create_user("Roc")
        u3_inserted = self.db_handler.create_user("Tese")
        
        self.assertTrue(u1_inserted and u2_inserted and u3_inserted)  
        self.print_result("Test de creación de usuario")
    
    def show_user_test(self):
        u1_show = self.db_handler.show_user("Pau")
        u2_show = self.db_handler.show_user("Roc")
        u3_show = self.db_handler.show_user("Tese")

    def edit_user_test(self): 
        pass

    def create_agenda_test(self):
        e1 = event(datetime.date(2024, 6, 15).isoformat(), datetime.timedelta(hours = 3600).seconds, "Traumatólogo", "Visita con el trauma hehe.", 0, "41.390753, 2.173127")
        e2 = event(datetime.date(2024, 5, 23).isoformat(), datetime.timedelta(hours = 3600).seconds, "Examen M06", "L'examen més difícil de la història", 1, "41.390753, 2.173127")
        e3 = event(datetime.date(2025, 3, 11).isoformat(), datetime.timedelta(hours = 3600).seconds, "Cumple Roc", "Mi cumple!!", 2, "41.390753, 2.173127")

        uid1 = ObjectId("6627f4b85a1a64b62936c5db")
        uid2 = ObjectId("6627f4b95a1a64b62936c5dc")
        uid3 = ObjectId("6627f4b95a1a64b62936c5dd")

        a1 = agenda("agenda_test", [e1, e2, e3], [uid1, uid2, uid3])

        return 

    def show_agenda_test(self):pass
        
    def edit_agenda_test(self):pass
    
    # def create_event_test(self):
        
    #     e1_inserted = self.db_handler.create_event(self.e1)
    #     e2_inserted = self.db_handler.create_event(self.e2)
    #     e3_inserted = self.db_handler.create_event(self.e3)
        
    #     self.assertTrue(e1_inserted and e2_inserted and e3_inserted)  # Si pasa el test, el codi continúa. Sino, dona error.
        
    #     self.print_result("Test de creación de eventos")

    # def show_event_test(self):
    #     e1_show = self.db_handler.show_event("Cumple Roc")
    #     e2_show = self.db_handler.show_event("Traumatólogo")
    #     e3_show = self.db_handler.show_event("Examen M06")
        
    #     self.assertTrue(e1_show and e2_show and e3_show)  # Comproba si retorna un diccionari amb contingut (True) o si està buit (False)
        
    #     self.print_result("Test de mostrado de eventos")
        
    # def edit_event_test(self):
    #     e1_edit = self.db_handler.edit_event("Cumple Roc", {"description": "Nueva descripción"})
    #     e2_edit = self.db_handler.edit_event("Traumatólogo", {"description": "Nueva descripción"})
    #     e3_edit = self.db_handler.edit_event("Examen M06", {"description": "Nueva descripción"})

    #     self.assertTrue(e1_edit == 1 and e2_edit == 1 and e3_edit == 1)  # Comproba que es modifiqui el registre comparant el modified_count amb un 1
        
    #     self.print_result("Test de edición de eventos")
        
    # def delete_event_test(self):
    #     e1_delete = self.db_handler.delete_event("Cumple Roc")
    #     e2_delete = self.db_handler.delete_event("Traumatólogo")
    #     e3_delete = self.db_handler.delete_event("Examen M06")

    #     self.assertTrue(e1_delete == 1 and e2_delete == 1 and e3_delete == 1)  # Comproba que s'esborri el registre comparant el deleted_count amb un 1
        
    #     self.print_result("Test de eliminación de eventos") 
