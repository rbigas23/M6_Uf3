from agenda_test import agenda_test
from user_test import user_test
from event_test import event_test


def app_test(): 

    print("Initializing...\n")

    tests = [agenda_test(), user_test(), event_test()]

    print("Connected, testing...\n")
    
    for test in tests:
        test.execute_all_tests()
        print("\n")

    input("Press ENTER to exit\n")


if __name__ == "__main__":
    app_test()
