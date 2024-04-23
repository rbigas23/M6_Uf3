from global_imports import pymongo

class peer():
    
    def __init__(self, collection_name):
        self.peer       = pymongo.MongoClient("mongodb+srv://tese:1234@cluster0.0xtd9rf.mongodb.net/?retryWrites=true&w=majority")
        self.db         = self.peer["agendas"]
        self.collection = self.db[collection_name]