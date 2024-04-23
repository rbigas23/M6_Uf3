from abc import ABC, abstractmethod
from global_imports import peer

class i_user_persistance(ABC):
    
    @abstractmethod
    def create_user():
        pass
    
    @abstractmethod
    def show_user():
        pass

    @abstractmethod
    def edit_user():
        pass

    #@abstractmethod
    #def delete_user():
    #    pass
    
    