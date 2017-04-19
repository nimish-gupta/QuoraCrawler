from config.database import db
class Interest:
    collection=db['interest']
    def __init__(self,type,name,data):
        self.type=type
        self.name=name
        self.data=data

    def insertData(self):
        Interest.collection.insert_one({

        })