

from pymongo import MongoClient
from tkinter import Button, Tk, Label,Entry, Toplevel
import random


Client  = MongoClient()
db      = Client["miniProjects"]
collection = db ["DS"]   

class colorOrSwitch():
    Done =True
    def __init__(self):
        self.doubleTable()
    def doubleTable(self):
        label =  Label(root, text = "Click Mutliple Times ", justify ="center")
        label.pack()
        button1 = Button(root, text="Color Dice", width ="20", command = self.r)
        button1.pack()
        button2 = Button(root, text="Orginal Dice", width ="20", command = self.s)
        button2.pack()
   
    def s (self):
        try:
            import ColorandOrdinary.OrdinaryDice 
        except AttributeError as a:
            print("Restart and try again")
            
        
    def r(self):
        import  ColorandOrdinary.ColorDice    
    def random_generator(self):
        result = random.randint(1, 6)
        d = self.faceDie(result)
        strinG = ""
        strinG += str(result)
        return d
    def takingInuserUnput(self, input):
        return input
        


root = Tk()

c= colorOrSwitch()

root.mainloop()





