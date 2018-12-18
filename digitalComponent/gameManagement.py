
class Game:
    def __init__(self,manager):
        self.colors = [color(255,0,0), color(0,255,255),color(0,255,0),color(0,0,255)]
        self.players = []
        self.amountActive = 0
        self._currentPlayer = None
        self._gameMode = 'LastManStanding'
        self._currentPlayerObservers = []
        self._winnerObservers = []
        self._allPlayerObservers = []
        self.currentPlayerIndex  = None
        self.board = None
        self.board = Board()
        self.setting = dict(lastManStanding = False, threeCastles = False, firstKnokOut = False)
        self.winner = None
        self.manager = manager

    def setPlayer(self,value):
        self._currentPlayer = value
        for callback in self._currentPlayerObservers:
            callback(self._currentPlayer)

    def createPlayers(self,amount):
        self.players = []
        for i in range(amount + 1):
            self.players.append(Player('methodplayer ' + str(i + 1), self.colors[i]))
        for callback in self._allPlayerObservers:
            callback(self.players)
    
    # amount of active players playing the game
    def setAmount(self, amount):
        self.amountActive = amount

    def bindTo(self,callback):
        self._currentPlayerObservers.append(callback)
        
    def bindToWin(self,callback):
        self._winnerObservers.append(callback)
        
    def bindToAll(self,callback):
        self._allPlayerObservers.append(callback)

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
        self.winCheck()
            
    def winCheck(self):
        if self.setting['lastManStanding']:
            if len(self.players) == 1:
                self.winner = self.players[0]
                for callback in self._winnerObservers:
                    callback(self.winner)
                self.manager.currentScreen = self.manager.screens.get('winScreen')
        if self.setting['threeCastles']:
            for player in self.players:
                if player.castles >= 3:
                    self.winner = player
                    for callback in self._winnerObservers:
                        callback(self.winner)
                    self.manager.currentScreen = self.manager.screens.get('winScreen2')
                    break;
    
    def knockoutWin(self, player):
        if self.setting['firstKnokOut']:
            self.winner = player
            for callback in self._winnerObservers:
                    callback(self.winner)
            self.manager.currentScreen = self.manager.screens.get('winScreen3')
            

class Board():
    def __init__(self):
        self.board = []

class Player():
    def __init__(self, name, colour):
        self.active = False
        self.name = name
        self.colour = colour
        self.coins = 500
        self.farms = 0
        self.castles = 0
        self.barracks = 0
        self.walls = 0
        self.palaces = 1
        self.villages = 0
        self.towers = 0
        self.mountain = 0
        self.forest = 0
        self.desert = 0
        self.swamp = 0
        self.highland = 0
        self.villagers = 2
        self.troops = 0
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
            
    def settroops(self,value):
        if value > 0:
            if self.coins >=2*value:
                self.setcoins(-2*value)
                self.troops += value
            for callback in self._valsObservers:
                callback(self)
            
    def setvillagers(self,value):
        if self.villagers < 2:
            self.setcoins(-2)
            self.villagers += value
        for callback in self._valsObservers:
            callback(self)
        
            
            

    def bindTo(self,callback):
        self._valsObservers.append(callback)

class Battle(object):
    def __init__(self,game):
        self.game = game
        self.attacker = self.game._currentPlayer
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
        self._observers = []
        
    def bindTo(self, callback):
        self._observers.append(callback)

    def setAttacker(self,att):
        self.attacker = att
        for callback in self._observers:
            callback(self)

    def setDefender(self,defen):
        self.defender = defen
        for callback in self._observers:
            callback(self)

    def setTroopsAttacker(self,x):
        self.TroopsAttacker = x
        for callback in self._observers:
            callback(self)

    def setTroopsDefender(self,x):
        self.TroopsDefender = x
        for callback in self._observers:
            callback(self)

    def setLocation(self,loc):
        self.location = loc
        locBuildings = []
        if loc._building1 is not None:
            locBuildings.append(loc._building1.name)
            self.defender = loc._building1.owner
        if loc._building2 is not None:
            locBuildings.append(loc._building2.name)
        for battleBuilding in self.buildings:
            for tileBuilding in locBuildings:
                if battleBuilding == tileBuilding:
                    self.buildings[battleBuilding] = True
                    
        for callback in self._observers:
            callback(self)

    def setBuildings(wall=False,tower=False,castle=False,palace=False):
        if wall:
            self.buildings['wall']=True
        if tower:
            self.buildings['tower']=True
        if castle:
            self.buildings['castle']=True
        if palace:
            self.buildings['palace']=True
        
        for callback in self._observers:
            callback(self)

    def setDamToAtt(self,x):
        self.damToAtt = x
        for callback in self._observers:
                callback(self)

    def setDamToDef(self,x):
        self.damToDef = x
        for callback in self._observers:
            callback(self)
        
    def fight():
        self.attDamage()
        self.defDamage()

    def attDamage():
        pass
        
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
                    self.game.knockoutWin(self.attacker)
                    self.game.players.remove(self.defender)
                    self.game.amountActive -= 1
                    print('knocked out, leftover: ' + str(self.game.players))
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
