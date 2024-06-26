from global_imports import Enum

class event():
    
    class tag_type(Enum):
        medical_appointment  = 0,
        academic_appointment = 1,
        personal_appointment = 2
    
    def __init__(self, date, duration, title, description = None, tags = None, location = None):
        self.date        = date
        self.duration    = duration
        self.title       = title
        self.description = description
        self.tags        = tags if tags else []
        self.location    = location
