from global_imports import unittest

from user_persistance import user_persistance


class user_test(unittest.TestCase):
    
    def __init__(self):
        self.user_handler = user_persistance()

    def create_user_test(self):
        u1_inserted = self.user_handler.create_user("Pau")
        u2_inserted = self.user_handler.create_user("Tese")
        u3_inserted = self.user_handler.create_user("Roc")
        
        self.assertTrue(u1_inserted and u2_inserted and u3_inserted)
        
        print("Test de creación de usuario completado correctamente.")
    
    def show_user_test(self):
        u1_show = self.user_handler.show_user("Pau")
        u2_show = self.user_handler.show_user("Tese")
        u3_show = self.user_handler.show_user("Roc")
        
        self.assertTrue(u1_show and u2_show and u3_show)
        
        print("Test de mostrado de usuario completado correctamente.")

    def edit_user_test(self): 

        self.assertTrue(self.user_handler.edit_user("Pau", {"name":"PAU_NUEVO_NOMBRE"}) == 1)
        
        print("Test de modificación de agenda completado correctamente.")
    
    def execute_all_tests(self):
        self.create_user_test()
        self.show_user_test()
        self.edit_user_test()
