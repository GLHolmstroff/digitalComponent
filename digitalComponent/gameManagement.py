class Game():
    def __init__(self):
        self.players = []
        self.currentPlayer = None
        self.currentPlayerIndex  = None
        self.board = None
        self.board = Board()
        self.setting = dict(lastManStanding = False, threeCastles = False, firstKnokOut = False)
    
    def nextPlayer(self):
        print('next')
        if self.currentPlayerIndex < 4:
            self.currentPlayerIndex += 1
            self.currentPlayer = self.players[self.currentPlayerIndex]
        else:
            self.currentPlayerIndex = 0
            self.currentPlayer = self.players[self.currentPlayerIndex]
        
class Board():
    def __init__(self):
        self.board = []
        
class Player():
    def __init__(self, name, c):
        self.active = False
        self.name = name
        self.vals = dict(coins = 0, farms=0,castles = 0, walls = 0, palaces = 0, villages = 0, towers = 0,barracks = 0, mountain = 0, highland = 0, forest = 0, desert = 0, swamp = 0)
        self.c = c
        self.coins = 0
        self.farms = 0
        self.castles = 0
        self.walls = 0
        self.palaces = 0
        self.villages = 0
        self.towers = 0
        self.mountain = 0
        self.forest = 0
        self.desert = 0
        self.swamp = 0
        # game.players.append(self)

class Battle():
    def __init__(self,attacker,defender,troopsAttacker,troopsDefender,wall,tower,castle,palace):
        self.attacker = attacker
        self.defender = defender
        self.troopsAttacker = troopsAttacker
        self.troopsDefender = troopsDefender
        self.buildings = dict(wall = wall, tower = tower, castle = castle, palace = palace)
    
        
