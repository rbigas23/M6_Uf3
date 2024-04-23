
class user():

    def __init__(self, id, name):
        self.id   = id
        self.name = name
        
    def __repr__(self):
        return f"user(id={repr(self.id)}, name={repr(self.name)})"