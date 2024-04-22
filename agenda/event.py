from enum import Enum

class event():
    
    class tag_type(Enum):
        medical_appointment  = 0,
        academic_appointment = 1,
        personal_appointment = 2
    
    def __init__(self, date, duration, title, description, tags, location):
        self.date        = date
        self.duration    = duration
        self.title       = title
        self.description = description
        self.tags        = tags
        self.location    = location