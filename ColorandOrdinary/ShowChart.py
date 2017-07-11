import matplotlib.pyplot as plt
from pymongo import MongoClient


"""Client  = MongoClient()
db      = Client["miniProjects"]
collection = db ["DS"] 
diceNumbers={}
diceNumbers["1"]  = ""
diceNumbers["2"] = ""
diceNumbers["3"] = ""
diceNumbers["4"] = ""
diceNumbers["5"] = ""
diceNumbers["6"] = ""
diceNumbers["7"] = ""
diceNumbers["8"] = ""
diceNumbers["9"] = ""
diceNumbers["10"] = ""
diceNumbers["11"] = ""
diceNumbers["12"] = ""
diceNumbers["13"] = ""
diceNumbers["14"] = ""
diceNumbers["15"] = ""


diceNumbers["tags"] = ["mongodb", "python", "pymongo","","","","","","","","","","","",""]


collection.insert(diceNumbers)

h ="sdf"
 
cursor =collection.find()
"""


"""import datetime
post = {"author": "Mike",
         "text": "My first blog post!",
         "tags": ["mongodb", "python", "pymongo"],
         "date": datetime.datetime.utcnow()}
posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id )
"""
def takingInuserUnput(input):
    
    return input


def start(ok):
    # Data to plot
    labels = 'ONE', 'TWO','THREE','FOUR','FIVE','SIX'

    explode = (0.1, 0, 0, 0,0,0)  # explode 1st slice
    # Plot
    plt.pie(ok, explode=explode, labels=labels, colors=None,
                autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.show()
    






        

