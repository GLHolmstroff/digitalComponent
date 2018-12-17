class Game():
    def __init__(self):
        self.colors = [color(255,0,0), color(0,255,255),color(0,255,0),color(0,0,255)]
        self.players = []
        self.amountActive = 0
        self._currentPlayer = None
        self._gameMode = 'LastManStanding'
        self._currentPlayerObservers = []
        self.currentPlayerIndex  = None
        self.board = None
        self.board = Board()
        self.setting = dict(lastManStanding = False, threeCastles = False, firstKnokOut = False)
        
        
    def setPlayer(self,value):
        self._currentPlayer = value
        for callback in self._currentPlayerObservers:
            callback(self._currentPlayer)
            
    def createPlayers(self,amount):
        self.players = []
        for i in range(amount):
            self.players.append(Player('player ' + str(i + 1), self.colors[i]))
        
    def setAmount(self, amount):
        self.amountActive = amount
        
    def bindTo(self,callback):
        self._currentPlayerObservers.append(callback)
    
    def setGameMode(self, mode):
        if mode == 0:
            self.setting['lastManStanding'] = True
            self.setting['threeCastles'] = False
            self.setting['firstKnokOut'] = False
            self.gameMode = 'LastManStanding'
        elif mode == 1:
            self.setting['lastManStanding'] = False
            self.setting['threeCastles'] = True
            self.setting['firstKnokOut'] = False
            self.gameMode = 'threeCastles'
        else:
            self.setting['lastManStanding'] = False
            self.setting['threeCastles'] = False
            self.setting['firstKnokOut'] = True
            self.gameMode = 'firstKnokOut'
        # for callback in self._currentPlayerObservers:
        #     callback(self._gameMode)
        
    def nextPlayer(self):
        if self.currentPlayerIndex < self.amountActive:
            self.currentPlayerIndex += 1
            self.setPlayer(self.players[self.currentPlayerIndex])
        else:
            self.currentPlayerIndex = 0
            self.setPlayer(self.players[self.currentPlayerIndex])
        
class Board():
    def __init__(self):
        self.board = []
        
class Player():
    def __init__(self, name, c):
        self.active = False
        self.name = name
        self.c = c
        self.coins = 500
        self.farms = 0
        self.castles = 0
        self.barracks = 0
        self.walls = 0
        self.palaces = 0
        self.villages = 0
        self.towers = 0
        self.mountain = 0
        self.forest = 0
        self.desert = 0
        self.swamp = 0
        self.highland = 0
        # self.vals = dict(coins = 0, farms=0,castles = 0, walls = 0, palaces = 0, villages = 0, towers = 0,barracks = 0, mountain = 0, highland = 0, forest = 0, desert = 0, swamp = 0)
        self._valsObservers = []
       
        
    def setcoins(self,value):
        self.coins += value
        for callback in self._valsObservers:
            callback(self)
            
    def setfarms(self,value):
        if self.coins >= 4:
            self.farms += value
            self.setcoins(-4)
            
        for callback in self._valsObservers:
            callback(self)
            
    def setcastles(self,value):
        if self.coins >= 20:
            self.castles += value
            self.setcoins(-20)
        for callback in self._valsObservers:
            callback(self)
            
    def setwalls(self,value):
        if self.coins >= 10:
            self.walls += value
            self.setcoins(-10)
        for callback in self._valsObservers:
            callback(self)
            print('added')
            
    def setpalaces(self,value):
        self.palaces += value
        for callback in self._valsObservers:
            callback(self)
            
    def setvillages(self,value):
        if self.coins >= 5:
            self.villages += value
            self.setcoins(-5)
        for callback in self._valsObservers:
            callback(self)
            
    def setbarracks(self,value):
        if self.coins >= 5:
            self.barracks += value
            self.setcoins(-5)
        for callback in self._valsObservers:
            callback(self)
            
    def settowers(self,value):
        if self.coins >= 15:
            self.towers += value
            self.setcoins(-15)
        for callback in self._valsObservers:
            callback(self)
            
    def setmountain(self,value):
        self.mountain += value
        for callback in self._valsObservers:
            callback(self)
            
    def sethighland(self,value):
        self.highland += value
        for callback in self._valsObservers:
            callback(self)
            
    def setswamp(self,value):
        self.swamp += value
        for callback in self._valsObservers:
            callback(self)
            
    def setforest(self,value):
        self.forest += value
        for callback in self._valsObservers:
            callback(self)
            
    def setdesert(self,value):
        self.desert += value
        for callback in self._valsObservers:
            callback(self)
            
    def setroad(self):
        if self.coins >= 1:
            self.setcoins(-1)
    
    def bindTo(self,callback):
        self._valsObservers.append(callback)

class Battle():
    def __init__(self):
        self.attacker = None
        self.defender = None
        self.troopsAttacker = 0
        self.troopsDefender = 0
        self.buildings = dict(wall = False, tower = False, castle = False, palace = False)
   
