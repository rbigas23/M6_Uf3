from abc import ABC, abstractmethod

class agenda_persistance(ABC):

    @abstractmethod
    def create_event():
        pass

    @abstractmethod
    def show_event():
        pass

    @abstractmethod
    def edit_event():
        pass

    @abstractmethod
    def delete_event():
        pass
    