
from pymongo import MongoClient
from tkinter import Button, Toplevel,Entry,Label,Tk


import random
import tkinter

import ColorandOrdinary.diceNum as dN
import ColorandOrdinary.ColorChart as cfc
from ColorandOrdinary import Send_Sms


Client  = MongoClient()
db      = Client["miniProjects"]
collection = db ["DS"]

count  = 0
diceList = [0,0,0,0,0,0]

class colorDice(tkinter.Button):
    
    def __init__(self):
        
        self.button = None
        self.g()
        self.count=0
        self.diceNumbers=[]
        self.obj =[]
        
    def random_generatorForColor(self):
        result = random.randint(0, 478)
        f = cfc.c.COLORS[result]
        return str(f)   
    def random_generator(self):
        result = random.randint(1, 6)
        self.numberCounter(result)
        strinG = ""
        strinG += str(result)
        return strinG
    def diceNumbers(self, num):
        
        return num
    def g(self):
        global count
        if(self.button == None):
            
            result= self.random_generator()
            cResult = self.random_generatorForColor()
         
            dN.Num.diceNumbers.append(result)
            
            self.button =  Button(root, text = "" + result, bg =""+cResult, height = 3  , width = 10, command = self.g)
            self.button.pack()
            count+=1
          
           
        if(count%15==0 and count !=0 ):
            
            r=dN.Num.diceNumbers
            
            self.name()
           
            
            for i in r:
                print(i)
            

        else:
            
            result = self.random_generator()
            cResult = self.random_generatorForColor()
            r=dN.Num.diceNumbers.append(result)
            self.button.destroy()
            self.button =  Button(root, text = "" + result, bg =""+cResult , height = 3  , width = 10, command = self.g)
            self.button.pack()
            count+=1
            
            
        if(count%15==0 and count !=0 ):
            Done=True
            r=dN.Num.diceNumbers
            for i in r:
                print(i)
            
            self.name()
            
            
    def numberCounter(self, result):
            if result == 1:
                diceList[0]+=1
            elif result == 2:
                diceList [1]+=1
            elif result == 3:
                diceList[2]+=1
            elif result == 4:
                diceList[3]+=1
            elif result == 5:
                diceList[4]+=1
            else:
                diceList[5]+=1
    def takingInuserUnput(self,input):
        return input
    def name(self):
        r0 = Tk()
        label =  Label(r0, text = "First and Last Name", justify ="center")
        label.pack()
        e = Entry(r0)
        e.pack()
        b = Button(r0, text="Submit", width=10, command=lambda : self.OnButtonClick(1,e.get()))
        b.pack()
        
        
       
       
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
            ColorD ={'Type of Dice':'COLOR'}
            f.update(ColorD)
            f.update(nameDict)
            collection.insert(f)
            import ColorandOrdinary.Send_Sms as SS 
            
            client = SS.Client("ACcb07e49822bc4906cb515e45b66447d4","ca6aa57cfa027e322c8dd80aa5569e5a")
            client.messages.create(from_='+18562882993',
                       to='+12672304684',
                       body=' '.join('{0}{1}, '.format(key, val) for key, val in f.items()))
            self.callback()
            
            # self.button1 was clicked; do something
        
root = Toplevel()

cd = colorDice()


root.mainloop()
        
        
        
    
    
    
    