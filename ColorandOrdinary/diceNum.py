

class Num():
    
    from pymongo import MongoClient
    Client  = MongoClient()
    db      = Client["miniProjects"]
    collection = db ["DS"] 
    def __init__(self):
        self.hello ="hello world"
    
    def go(self,col ):
        col.insert(col)
   
    diceNumbers=[]  
N = Num()
#N.collection.insert()


