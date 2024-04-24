from global_imports import datetime, ObjectId, unittest

from agenda import agenda
from agenda_persistance import agenda_persistance
from event import event


class agenda_test(unittest.TestCase):
    
    def __init__(self):
        
        self.agenda_pers_handler = agenda_persistance()
        
    def create_agenda_test(self):
        
        e1 = event(datetime.date(2024, 6, 15).isoformat(), datetime.timedelta(hours = 3600).seconds, "Traumatólogo", "Visita con el trauma hehe.", 0, "41.390753, 2.173127")
        e2 = event(datetime.date(2024, 5, 23).isoformat(), datetime.timedelta(hours = 3600).seconds, "Examen M06", "L'examen més difícil de la història", 1, "41.390753, 2.173127")
        e3 = event(datetime.date(2025, 3, 11).isoformat(), datetime.timedelta(hours = 3600).seconds, "Cumple Roc", "Mi cumple!!", 2, "41.390753, 2.173127")

        uids = [ObjectId("6627f4b85a1a64b62936c5db"), ObjectId("6627f4b95a1a64b62936c5dc"), ObjectId("6627f4b95a1a64b62936c5dd")]

        a1 = agenda("agenda_test", [e1, e2, e3], uids)
        
        self.assertTrue(self.agenda_pers_handler.create_agenda(a1))
        
        print("Test de creación de agenda completado correctamente.")

    def show_agenda_test(self):
        
        self.assertTrue(self.agenda_pers_handler.show_agenda("agenda_test"))
        
        print("Test de mostrado de agenda completado correctamente.")
        
    def edit_agenda_test(self):
        
        self.assertTrue(self.agenda_pers_handler.edit_agenda("agenda_test", {"name":"NUEVO NOMBRE"}) == 1)
        
        print("Test de modificación de agenda completado correctamente.")
        
    def execute_all_tests(self):
        self.create_agenda_test()
        self.show_agenda_test()
        self.edit_agenda_test()
