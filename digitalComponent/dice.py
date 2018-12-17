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
            

#some secific items I made for the setup screen
class setupDice(dice):
    def __init__(self, x,y,w,h,name, val, backgroundColor = color(255)):
        super(setupDice, self).__init__(x,y,w,h,name, val,backgroundColor = backgroundColor)
        self.active = None
        
class setupDiceGroup(diceGroup):
    def __init__(self,x,y,w,h,name,game,*dice):
         super(setupDiceGroup,self).__init__(x,y,w,h,name,*dice)
         self.results = []
         self.amountActive = 0
         self.winningDice = 0
         self.game = game
    
    def onClick(self):
        print('onClick')
        self.winningDice = 0
        rollAgain = True
        while rollAgain and self.amountActive > 0:
            # print('rolling..')
            self.results = []
            for d in self.dice:
                d.onClick()
                self.results.append(d.val)    
            
            for i in range(len(self.results)):
                if self.results[i] == self.results[self.winningDice] and i != 0:
                    rollAgain = True
                elif self.results[i] > self.results[self.winningDice]:
                    rollAgain =  False
                    self.winningDice = i - 1
            print(self.winningDice)
            print(len(self.game.players))
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
        
        

        
                    
            
