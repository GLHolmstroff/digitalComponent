class Game():
    def __init__(self):
        self.players = []
        self.currentPlayer = None
        self.board = None
        self.board = Board()
    
class Board():
    def __init__(self):
        self.board = []
        
class player():
    def __init__(self, name, c):
        self.active = False
        self.name = name
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
        game.players.append(self)
