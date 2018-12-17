
class Game:
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
    def __init__(self, name, colour):
        self.active = False
        self.name = name
        self.colour = colour
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

class Battle(object):
    def __init__(self):
        self.attacker = None
        self.defender = None
        self.troopsAttacker = 0
        self.troopsDefender = 0
        self.location = None
        self.buildings = {'wall' : False, 'tower' : False, 'castle' : False, 'palace' : False}
        self.damToAtt = 0
        self.damToDef = 0
        self.troopsLostAtt = 0
        self.troopsLostDef = 0
        self.defLost = {'troops' : self.troopsLostDef,'wall':False, 'tower':False, 'castle':False, 'palace':False, 'civ':False}
        self.attLost = 0
        
    def setAttacker(self,att):
        self.attacker = att
        
    def setDefender(self,defen):
        self.defender = defen
   
    def setTroopsAttacker(self,x):
        self.TroopsAttacker = x
        
    def setTroopsDefender(self,x):
        self.TroopsDefender = x
    
    def setLocation(self,loc):
        self.location = loc
        locBuildings = []
        if loc._building1 is not None:
            locBuildings.append(loc._building1.name)
        if loc._building2 is not None:
            locBuildings.append(loc._building2.name)
        for battleBuilding in self.buildings:
            for tileBuilding in locBuildings:
                if battleBuilding == tileBuilding:
                    self.buildings[battleBuilding] = True
            
            
        
    def setDamtoDef(self,x):
        self.damToDef = x
    
    def setBuildings(wall=False,tower=False,castle=False,palace=False):
        if wall:
            self.buildings['wall']=True
        if tower:
            self.buildings['tower']=True
        if castle:
            self.buildings['castle']=True
        if palace:
            self.buildings['palace']=True
    
    def setDamToAtt(self,x):
        self.damToAtt = x
    
    def setDamToDef(self,x):
        self.damToDef = x
        
    def defDamage(self):
        self.troopsLostDef = 0
        restDamage = int(self.damToDef)
        if self.buildings['wall']:
            if restDamage >= 10:
                self.location.remove('wall')
                self.defLost[wall] = True
                restDamage -= 10
        if self.buildings['tower' ]:
            if restDamage >= 15:
                self.location.remove('tower')
                self.defLost['tower'] = True
                restDamage -=15
        if self.buildings['castle']:
            if restDamage >= 20:
                self.location.remove('castle')
                self.defLost['castle'] = True
                restDamage -=20
        for x in range(self.troopsDefender):
            if restDamage >=4:
                restDamage -=4
                self.troopsLostDef +=1
        if self.troopsLostDef == self.troopsDefender:
            if self.buildings['palace']:
                if restDamage >= 20:
                    self.location.remove('palace')
                    self.defLost['palace'] = True
                    self.location.remove('civ')
                    self.defLost['civ'] = True
                    # function to get knocked out
                restDamage -=20
        else:
            self.location.remove(civ)
            self.defLost['civ'] = True
            
    def reset(self):
        self.attacker = None
        self.defender = None
        self.troopsAttacker = 0
        self.troopsDefender = 0
        self.location = None
        self.buildings = {'wall' : False, 'tower' : False, 'castle' : False, 'palace' : False}
        self.damtoAtt = 0
        self.damtoDef = 0
        self.troopsLostAtt = 0
        self.troopsLostDef = 0
        self.defLost = {'troops' : self.troopsLostDef,'wall':False, 'tower':False, 'castle':False, 'palace':False, 'civ':False}
        self.attLost = 0
