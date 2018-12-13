class Game():
    def __init__(self):
        self.players = []
        self._currentPlayer = None
        self._currentPlayerObservers = []
        self.currentPlayerIndex  = None
        self.board = None
        self.board = Board()
        self.setting = dict(lastManStanding = False, threeCastles = False, firstKnokOut = False)

        
    def setPlayer(self,value):
        self._currentPlayer = value
        for callback in self._currentPlayerObservers:
            callback(self._currentPlayer)
            
    def bindTo(self,callback):
        self._currentPlayerObservers.append(callback)
    
    def nextPlayer(self):
        if self.currentPlayerIndex < 3:
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
        self.coins = 0
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
        self.farms += value
        for callback in self._valsObservers:
            callback(self)
            
    def setcastles(self,value):
        self.castles += value
        for callback in self._valsObservers:
            callback(self)
            
    def setwalls(self,value):
        self.walls += value
        for callback in self._valsObservers:
            callback(self)
            
    def setpalaces(self,value):
        self.palaces += value
        for callback in self._valsObservers:
            callback(self)
            
    def setvillages(self,value):
        self.villages += value
        for callback in self._valsObservers:
            callback(self)
            
    def setbarracks(self,value):
        self.barracks += value
        for callback in self._valsObservers:
            callback(self)
            
    def settowers(self,value):
        self.towers += value
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
            
    def bindTo(self,callback):
        self._valsObservers.append(callback)

class Battle():
    def __init__(self):
        self.attacker = None
        self.defender = None
        self.troopsAttacker = 0
        self.troopsDefender = 0
        self.buildings = dict(wall = False, tower = False, castle = False, palace = False)
   
