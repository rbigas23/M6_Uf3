from abc import ABC, abstractmethod
from global_imports import peer

class i_agenda_persistance(ABC):

    @abstractmethod
    def create_agenda():
        pass

    @abstractmethod
    def show_agenda():
        pass

    @abstractmethod
    def edit_agenda():
        pass

    #@abstractmethod
    #def delete_agenda():
    #    pass
    
    