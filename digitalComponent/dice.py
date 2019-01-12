from items import*
import random

class dice(clickable):
    def __init__(self,x,y,w,h,name, val ,backgroundColor = color(255)):
        super(dice, self).__init__(x,y,w,h,name,backgroundColor = backgroundColor)
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
        fill(self.backgroundColor)
        rect (self.x,self.y,self.w,self.h,10,10,10,10)
        fill(10)
        ellipse(self.x + 0.5*self.w,self.y+0.5*self.h,0.2*self.w,0.2*self.h)
        
    def diceTwo(self):
        fill(self.backgroundColor)
        rect(self.x,self.y,self.w,self.h,10,10,10,10)
        fill(10)
        ellipse(self.x + 0.25 * self.w, self.y + 0.75 * self.h, 0.2*self.w, 0.2*self.h)
        ellipse(self.x + 0.75 * self.w, self.y + 0.25 * self.h, 0.2*self.w, 0.2*self.h)
        
    def diceThree(self):
        fill(self.backgroundColor)
        rect (self.x,self.y,self.w,self.h,10,10,10,10)
        fill(10)
        ellipse(self.x + 0.25 * self.w, self.y + 0.75 * self.h, 0.2*self.w, 0.2*self.h)
        ellipse(self.x + 0.5*self.w,self.y+0.5*self.h,0.2*self.w,0.2*self.h)
        ellipse(self.x + 0.75 * self.w, self.y + 0.25 * self.h, 0.2*self.w, 0.2*self.h)
    
    def diceFour(self):
        fill(self.backgroundColor)
        rect (self.x,self.y,self.w,self.h,10,10,10,10)
        fill(10)
        ellipse(self.x + 0.25 * self.w, self.y + 0.25 * self.h, 0.2*self.w, 0.2*self.h)
        ellipse(self.x + 0.75 * self.w, self.y + 0.25 * self.h, 0.2*self.w, 0.2*self.h)
        ellipse(self.x + 0.25 * self.w, self.y + 0.75 * self.h, 0.2*self.w, 0.2*self.h)
        ellipse(self.x + 0.75 * self.w, self.y + 0.75 * self.h, 0.2*self.w, 0.2*self.h)
        
        
    def diceFive(self):
        fill(self.backgroundColor)
        rect (self.x,self.y,self.w,self.h,10,10,10,10)
        fill(10)
        ellipse(self.x + 0.25 * self.w, self.y + 0.25 * self.h, 0.2*self.w, 0.2*self.h)
        ellipse(self.x + 0.75 * self.w, self.y + 0.25 * self.h, 0.2*self.w, 0.2*self.h)
        ellipse(self.x + 0.25 * self.w, self.y + 0.75 * self.h, 0.2*self.w, 0.2*self.h)
        ellipse(self.x + 0.75 * self.w, self.y + 0.75 * self.h, 0.2*self.w, 0.2*self.h)
        ellipse(self.x + 0.5*self.w,self.y+0.5*self.h,0.2*self.w,0.2*self.h)
        
        
    def diceSix(self): 
        fill(self.backgroundColor)
        rect (self.x,self.y,self.w,self.h,10,10,10,10)
        fill(10)
        ellipse(self.x + 0.25 * self.w, self.y + 0.25 * self.h, 0.2*self.w, 0.2*self.h)
        ellipse(self.x + 0.75 * self.w, self.y + 0.25 * self.h, 0.2*self.w, 0.2*self.h)
        ellipse(self.x + 0.25 * self.w, self.y + 0.75 * self.h, 0.2*self.w, 0.2*self.h)
        ellipse(self.x + 0.75 * self.w, self.y + 0.75 * self.h, 0.2*self.w, 0.2*self.h)
        ellipse(self.x + 0.25 * self.w, self.y + 0.5 * self.h, 0.2*self.w, 0.2*self.h)
        ellipse(self.x + 0.75 * self.w, self.y + 0.5 * self.h, 0.2*self.w, 0.2*self.h)
        
    def copy(self):
        return dice(self.x,self.y,self.w,self.h,self.name,self.val,self.backgroundColor)
        
class diceGroup(clickable): 
    def __init__(self,x,y,w,h,name, *dice):
        super(diceGroup, self).__init__(x,y,w,h,name)
        self.dice=list()
        self._observers = []
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
        
    def bindTo(self,callback):
        self._observers.append(callback)
            

#some secific items I made for the setup screen
class setupDice(dice):
    def __init__(self, x,y,w,h,name, val, backgroundColor = color(255)):
        super(setupDice, self).__init__(x,y,w,h,name, val,backgroundColor = backgroundColor)
        self.active = None
        
class setupDiceGroup(diceGroup):
    def __init__(self,x,y,w,h,name,game,*dice):
         super(setupDiceGroup,self).__init__(x,y,w,h,name,*dice)
         self.results = []
         self.amountActive = 2
         self.winningDice = 0
         self.game = game
         self.changeAmount(2)
    def onClick(self):
        self.winningDice = 0
        self.results = []
        for d in self.dice:
            if d.active:
                d.onClick()
                self.results.append(d.val)
        try:    
            self.winningDice = self.results.index(max(self.results))
        except:
            self.winningDice = 0
        self.game.currentPlayer = self.game.setPlayer(self.game.players[self.winningDice])
        self.game.currentPlayerIndex = self.winningDice
    
    def changeAmount(self, amount):
        if amount  == 2:
            self.amountActive = 2
            self.dice[0].active = True
            self.dice[1].active = True
            self.dice[2].active = False
            self.dice[3].active = False
        elif amount == 3:
            self.amountActive = 3
            self.dice[0].active = True
            self.dice[1].active = True
            self.dice[2].active = True
            self.dice[3].active = False
        else:
            self.amountActive = 4
            self.dice[0].active = True
            self.dice[1].active = True
            self.dice[2].active = True
            self.dice[3].active = True
    
    def display(self):
        for d in self.dice:
            if d.active:
                d.display()
                
class varDiceGroup(diceGroup):
    def __init__(self,x,y,w,h,name,parents,attrname,function,*dice):
        super(varDiceGroup,self).__init__(x,y,w,h,name,*dice)
        self.amount = 0
        self.parents = parents
        self.attrname = attrname
        for x in self.parents:
            x.bindTo(self.update)
        self.function = function
        self.sum = 0
            
    def update(self, value):
        self.amount = getattr(value,self.attrname)
        self.resetDice()
        
    def resetDice(self):
        self.dice = list()
        for x in range(self.amount):
            d = dice(self.x + 100*x,self.y,100,100,'',1)
            self.dice.append(d.copy())
            
    def onClick(self):
        self.sum = 0
        for d in self.dice:
            d.onClick()
            self.sum += d.val
        for callback in self._observers:
            callback(self)    
        self.function(self.sum)
            
        
        
        

        
                    
            
