from global_imports import ABC, abstractmethod

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
