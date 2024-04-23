import os
from test import test
    
def app_test():

    print("initializing..\n")
    
    test_handler = test()

    print("connected, testing..\n")

    test_handler.create_test()
    test_handler.show_test()
    test_handler.edit_test()
    test_handler.delete_test()
        
    input("\npress ENTER to exit\n")       

if __name__ == "__main__":
    app_test()