from items import*
import random

class dice(clickable):
    def __init__(self,x,y,w,h,name, val):
        super(dice, self).__init__(x,y,w,h,name)
        self.val=val
        
    def display(self): 
        fill(255)
        if self.val == 1:
            self.diceOne()
        if self.val == 2:
            self.diceTwo()
        if self.val == 3:
            self.diceThree()
        if self.val == 4:
            self.diceFour()
        if self.val == 5:
            self.diceFive()
        if self.val == 6:
            self.diceSix()
    
    def onClick(self, *args):
        self.diceRoll()
    
    def onHover(self):
        pass
                
    def diceRoll(self):
        self.val = random.randint(1,6) 
    
    def diceOne(self):
        rect (self.x,self.y,self.w,self.h,10,10,10,10)
        fill(10)
        ellipse(self.x + 0.5*self.w,self.y+0.5*self.h,0.2*self.w,0.2*self.h)
        
    def diceTwo(self):
        rect(self.x,self.y,self.w,self.h,10,10,10,10)
        fill(10)
        ellipse(self.x + 0.25 * self.w, self.y + 0.75 * self.h, 0.2*self.w, 0.2*self.h)
        ellipse(self.x + 0.75 * self.w, self.y + 0.25 * self.h, 0.2*self.w, 0.2*self.h)
        
    def diceThree(self):
        rect (self.x,self.y,self.w,self.h,10,10,10,10)
        fill(10)
        ellipse(self.x + 0.25 * self.w, self.y + 0.75 * self.h, 0.2*self.w, 0.2*self.h)
        ellipse(self.x + 0.5*self.w,self.y+0.5*self.h,0.2*self.w,0.2*self.h)
        ellipse(self.x + 0.75 * self.w, self.y + 0.25 * self.h, 0.2*self.w, 0.2*self.h)
    
    def diceFour(self):
        rect (self.x,self.y,self.w,self.h,10,10,10,10)
        fill(10)
        ellipse(self.x + 0.25 * self.w, self.y + 0.25 * self.h, 0.2*self.w, 0.2*self.h)
        ellipse(self.x + 0.75 * self.w, self.y + 0.25 * self.h, 0.2*self.w, 0.2*self.h)
        ellipse(self.x + 0.25 * self.w, self.y + 0.75 * self.h, 0.2*self.w, 0.2*self.h)
        ellipse(self.x + 0.75 * self.w, self.y + 0.75 * self.h, 0.2*self.w, 0.2*self.h)
        
        
    def diceFive(self):
        rect (self.x,self.y,self.w,self.h,10,10,10,10)
        fill(10)
        ellipse(self.x + 0.25 * self.w, self.y + 0.25 * self.h, 0.2*self.w, 0.2*self.h)
        ellipse(self.x + 0.75 * self.w, self.y + 0.25 * self.h, 0.2*self.w, 0.2*self.h)
        ellipse(self.x + 0.25 * self.w, self.y + 0.75 * self.h, 0.2*self.w, 0.2*self.h)
        ellipse(self.x + 0.75 * self.w, self.y + 0.75 * self.h, 0.2*self.w, 0.2*self.h)
        ellipse(self.x + 0.5*self.w,self.y+0.5*self.h,0.2*self.w,0.2*self.h)
        
        
    def diceSix(self): 
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
            
    def display(self):
        for d in self.dice:
            d.display()
    
    def onClick(self):
        for d in self.dice:
            d.onClick()
    
    def addDice(self,d):
        if isinstance(dice,d):
            self.dice.append(d)
            

        
        
