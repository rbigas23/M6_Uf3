from global_imports import datetime, ObjectId


class agenda():
    
    def __init__(self, name, events, user_ids):
        self.name     = name
        self.events   = [e.__dict__ for e in events]
        self.user_ids = user_ids
