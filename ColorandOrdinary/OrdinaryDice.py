

from tkinter import  Button as But , PhotoImage, Toplevel,Tk,Entry,Label
import ColorandOrdinary.diceNum as dN
import tkinter
import random
from pymongo import MongoClient
from ColorandOrdinary import Send_Sms
Client  = MongoClient()
db      = Client["miniProjects"]
collection = db ["DS"]

diceList = [0,0,0,0,0,0]

count  = 0
class diceListe(tkinter.Toplevel):
    
    def __init__(self):
        self.greatButton = But()
        self.random_generator()
        self.go()
        self.photo = PhotoImage()
        self.count = 0
    def random_generator(self):
        result = random.randint(1, 6)
        dN.Num.diceNumbers.append(result)
        d = self.faceDie(result)
        strinG = ""
        strinG += str(result)
        return d
    def random_generatorForColor(self):
        result = random.randint(0, 478)
        return result
    def faceDie(self, face):
        if(face==1):
            self.photo = PhotoImage(file="C:\\Users\\moni\\Downloads\\dice1150x150.png")
            diceList[0] +=1
            return self.photo
        elif(face==2):
            self.photo = PhotoImage(file="C:\\Users\\moni\\Downloads\\dice2150x150.png")
            diceList[1] +=1
            return self.photo
        elif(face==3):
            self.photo = PhotoImage(file="C:\\Users\\moni\\Downloads\\dice3150x150.png")
            diceList[2] +=1
            return self.photo
        elif(face==4):
            self.photo = PhotoImage(file="C:\\Users\\moni\\Downloads\\dice4150x150.png")
            diceList[3] +=1
            return self.photo
        elif(face==5):
            self.photo = PhotoImage(file="C:\\Users\\moni\\Downloads\\dice5150x150.png")
            diceList[4] +=1
            return self.photo
        else:
            self.photo = PhotoImage(file="C:\\Users\\moni\\Downloads\\dice6150x150.png")
            diceList[5] +=1
            return self.photo
        
    def go(self):
        global count
        """check this out  http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter"""
        
        count+=1
        self.greatButton.pack_forget() 
        self.greatButton = But(root, image=self.random_generator(),command=self.go
                ,height = 150   , width = 150 )
        self.greatButton.pack()
        
        if(count%15==0 and count !=0 ):
            r=dN.Num.diceNumbers
            for i in r:
                print(i)
            self.name()    
            
            """"f = dict(zip(('oneRoll', 'twoRoll','thereRoll','fourthRoll','fifthRoll','sixthRoll','seventhRoll',
                      'eightRoll','ninthRoll','tenthRoll','eleventhRoll','twelveRoll','thirtteenthRoll','fourthteenthRoll','fithRoll'), (r)))
            f.update(g)
            collection.insert(f)"""
    def callback(self):
            import ColorandOrdinary.ShowChart as M
            M.start(diceList)  
    def OnButtonClick(self, button_id,e):
        if button_id == 1:
            st =""
            r=dN.Num.diceNumbers
            f=dict(zip(('Roll One is: ', 'Roll Two is: ','Roll Three is: ','Roll Four is: ','Roll Five is: ','Roll Six is: ','Roll Seven is: ',
                      'Roll Eight is: ','Roll Nine is: ','Roll Ten is: ','Roll Eleven is: ','RollTwelve is: ','Roll Thirthteenth is: ','Roll Fourthteenth is: ','Roll Fifthteenth is: '), (r)))
            nameDict= {'Name: ':e}
            OrdinayD ={'Type of Dice':'Orginal'}
            f.update(OrdinayD)
            f.update(nameDict)
            collection.insert(f)
            import ColorandOrdinary.Send_Sms as SS 
            
            client = SS.Client("ACcb07e49822bc4906cb515e45b66447d4","ca6aa57cfa027e322c8dd80aa5569e5a")
            client.messages.create(from_='+18562882993',
                       to='+12672304684',
                       body=' '.join('{0}{1}, '.format(key, val) for key, val in f.items()))
            self.callback()
            
            # self.button1 was clicked; do something
               
    def name(self):
        r0 = Tk()
        label =  Label(r0, text = "First and Last Name", justify ="center")
        label.pack()
        
        e = Entry(r0)
        e.pack()
   
            
            
        b = But(r0, text="Submit", width=10, command=lambda : self.OnButtonClick(1,e.get()))
        b.pack()
         
        
 
 
            
"""print(help(diceListe))"""

root  = Toplevel() 
c = diceListe()
print(id(c.go()))
root.mainloop() 



            