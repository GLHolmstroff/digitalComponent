from items import*
import random

class dice(clickable):
    def __init__(self,x,y,w,h,name, val,stopcount=20):
        super(dice, self).__init__(x,y,w,h,name)
        self.val=val
        self.clicked = False
        self.counter = 0
        self.stopcount = stopcount
        
    def display(self): 
        fill(255)
        if self.clicked:
            getattr(self,"dice{}".format(random.randint(1,6)))()
            self.counter += 1
        else:
            getattr(self,"dice{}".format(self.val))()
        if self.counter >= self.stopcount:
            self.counter = 0
            self.clicked = False
                         
    def onClick(self, *args):
        self.diceRoll()
        self.clicked = True
        
    def onHover(self):
        pass
                
    def diceRoll(self):
        self.val = random.randint(1,6) 
    
    def dice1(self):
        rect (self.x,self.y,self.w,self.h,10,10,10,10)
        fill(10)
        ellipse(self.x + 0.5*self.w,self.y+0.5*self.h,0.2*self.w,0.2*self.h)
        
    def dice2(self):
        rect(self.x,self.y,self.w,self.h,10,10,10,10)
        fill(10)
        ellipse(self.x + 0.25 * self.w, self.y + 0.75 * self.h, 0.2*self.w, 0.2*self.h)
        ellipse(self.x + 0.75 * self.w, self.y + 0.25 * self.h, 0.2*self.w, 0.2*self.h)
        
    def dice3(self):
        rect (self.x,self.y,self.w,self.h,10,10,10,10)
        fill(10)
        ellipse(self.x + 0.25 * self.w, self.y + 0.75 * self.h, 0.2*self.w, 0.2*self.h)
        ellipse(self.x + 0.5*self.w,self.y+0.5*self.h,0.2*self.w,0.2*self.h)
        ellipse(self.x + 0.75 * self.w, self.y + 0.25 * self.h, 0.2*self.w, 0.2*self.h)
    
    def dice4(self):
        rect (self.x,self.y,self.w,self.h,10,10,10,10)
        fill(10)
        ellipse(self.x + 0.25 * self.w, self.y + 0.25 * self.h, 0.2*self.w, 0.2*self.h)
        ellipse(self.x + 0.75 * self.w, self.y + 0.25 * self.h, 0.2*self.w, 0.2*self.h)
        ellipse(self.x + 0.25 * self.w, self.y + 0.75 * self.h, 0.2*self.w, 0.2*self.h)
        ellipse(self.x + 0.75 * self.w, self.y + 0.75 * self.h, 0.2*self.w, 0.2*self.h)
        
        
    def dice5(self):
        rect (self.x,self.y,self.w,self.h,10,10,10,10)
        fill(10)
        ellipse(self.x + 0.25 * self.w, self.y + 0.25 * self.h, 0.2*self.w, 0.2*self.h)
        ellipse(self.x + 0.75 * self.w, self.y + 0.25 * self.h, 0.2*self.w, 0.2*self.h)
        ellipse(self.x + 0.25 * self.w, self.y + 0.75 * self.h, 0.2*self.w, 0.2*self.h)
        ellipse(self.x + 0.75 * self.w, self.y + 0.75 * self.h, 0.2*self.w, 0.2*self.h)
        ellipse(self.x + 0.5*self.w,self.y+0.5*self.h,0.2*self.w,0.2*self.h)
        
        
    def dice6(self): 
        rect (self.x,self.y,self.w,self.h,10,10,10,10)
        fill(10)
        ellipse(self.x + 0.25 * self.w, self.y + 0.25 * self.h, 0.2*self.w, 0.2*self.h)
        ellipse(self.x + 0.75 * self.w, self.y + 0.25 * self.h, 0.2*self.w, 0.2*self.h)
        ellipse(self.x + 0.25 * self.w, self.y + 0.75 * self.h, 0.2*self.w, 0.2*self.h)
        ellipse(self.x + 0.75 * self.w, self.y + 0.75 * self.h, 0.2*self.w, 0.2*self.h)
        ellipse(self.x + 0.25 * self.w, self.y + 0.5 * self.h, 0.2*self.w, 0.2*self.h)
        ellipse(self.x + 0.75 * self.w, self.y + 0.5 * self.h, 0.2*self.w, 0.2*self.h)
        
class diceGroup(clickable): 
    def __init__(self,x,y,w,h,name, *dice):
        super(diceGroup, self).__init__(x,y,w,h,name)
        self.dice=list()
        for d in dice: 
            self.dice.append(d)
        self.out = 0
        self.outObservers = []
            
    def display(self):
        for d in self.dice:
            d.display()
    
    def onClick(self):
        self.out = 0
        for d in self.dice:
            d.onClick()
        for d in self.dice:
            self.out += d.val
        for callback in self.outObservers:
            callback(self)
        
    
    def addDice(self,d):
        if isinstance(dice,d):
            self.dice.append(d)
            
    def bindTo(self,callback):
        self.outObservers.append(callback)
        
        
