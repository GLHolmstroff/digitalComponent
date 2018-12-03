from items import *

class Tile(item):
    def __init__(self,x,y,w,h,name, gold=0, colour=0, building=0, road=False, civ=False, mil=False, **kwargs):
        super(Tile, self).__init__(x,y,w,h,name, **kwargs)
        self.gold = gold        
        self.colour = colour
        self.building = building
        self.road = road
        self.civ = civ
        self.mil = mil
        
    def display(self):
        fill(self.colour)
        h = createShape()
        h.beginShape()
        h.vertex(self.x,self.y)
        h.vertex(self.x + 0.5*self.w,self.y)
        h.vertex(self.x + 0.75*self.w,self.y+0.5*self.h)
        h.vertex(self.x + 0.5*self.w,self.y+self.h)
        h.vertex(self.x, self.y+self.h)
        h.vertex(self.x - 0.25*self.w,self.y+0.5*self.h)
        h.endShape(CLOSE)
        shape(h)

class clickableTile(Tile, clickable):
    def __init__(self,x,y,w,h,name, gold=0, colour=0, building=0, road=False, civ=False, mil=False, **kwargs):
        super(clickableTile, self).__init__(x,y,w,h,name,gold,colour,building,road,civ,mil, **kwargs)
    
    def onClick(self):
        self.colour = 255
    
    def onHover(self):
        pass

class Desert(Tile):
    def __init__(self,x,y,w,h,name):
        super(Desert, self).__init__(x,y,w,h,name,2,'#DAA33A',2,True,True,False)
        
class clickableDesert(clickableTile):
    def __init__(self,x,y,w,h,name):
        super(clickableDesert, self).__init__(x,y,w,h,name,2,'#DAA33A',2,True,True,False)

class Forest(Tile):
    def __init__(self,x,y,w,h,name):
        super(Forest, self).__init__(x,y,w,h,name,2,'#8CA74D',1,True,True,True)

class clickableForest(clickableTile):
    def __init__(self,x,y,w,h,name):
        super(clickableForest, self).__init__(x,y,w,h,name,2,'#8CA74D',1,True,True,True)

class Highland(Tile):
    def __init__(self,x,y,w,h,name):
        super(Highland, self).__init__(x,y,w,h,name,2,'#C02823',2,True,True,True)

class clickableHighland(clickableTile):
    def __init__(self,x,y,w,h,name):
        super(clickableHighland, self).__init__(x,y,w,h,name,2,'#C02823',2,True,True,True)

class Mountain(Tile):
    def __init__(self,x,y,w,h,name):
        super(Mountain, self).__init__(x,y,w,h,name,3,'#F0E5B4',1,True,False,True)

class clickableMountain(clickableTile):
    def __init__(self,x,y,w,h,name):
        super(clickableMountain, self).__init__(x,y,w,h,name,3,'#F0E5B4',1,True,False,True)

class Swamp(Tile):
    def __init__(self,x,y,w,h,name):
        super(Swamp, self).__init__(x,y,w,h,name,1,'#3D342D',2,False,True,True)

class clickableSwamp(clickableTile):
    def __init__(self,x,y,w,h,name):
        super(clickableSwamp, self).__init__(x,y,w,h,name,1,'#3D342D',2,False,True,True)

class Water(Tile):
    def __init__(self,x,y,w,h,name):
        super(Water, self).__init__(x,y,w,h,name,0,'#4A8EA5',0,False,False,False)

class clickableWater(clickableTile):
    def __init__(self,x,y,w,h,name):
        super(clickableWater, self).__init__(x,y,w,h,name,0,'#4A8EA5',0,False,False,False)
        
class gameMap(item):
    def __init__(self, x,y,w,h,name,rows, **kwargs):
        super(gameMap, self).__init__(x,y,w,h,name)
        self.tiles = list()
        self.rows = rows
        self.columns = rows
        self.waterFill()
        
        
    def waterFill(self):
        self.tiles = list()
        for a in range(self.columns):
            self.tiles.append(list())
        for a in range (self.columns):
            for b in range (self.rows):
                self.tiles[a].append(clickableWater(self.x,self.y,self.w/(self.columns),self.h/(self.rows),''))
        self.displayPrep()
        
    # Moves hexagons into place to display as grid
    def displayPrep(self):
        for tilelist in self.tiles:
            for tile in tilelist:
                tile.x = self.x
                tile.y = self.y
                tile.w = self.w/(self.columns)
                tile.h = self.h/(self.rows)
                tile.x = tile.x + 0.75 * self.tiles.index(tilelist) * tile.w
                if self.tiles.index(tilelist) % 2 != 0:
                    tile.y = tile.y + 0.5*tile.h
                tile.y = tile.y + tilelist.index(tile) * tile.h     
                
    def display(self):
        for tilelist in self.tiles:
            for tile in tilelist:
                tile.display()
                
    def editTile(self,x,y,tile):
        if isinstance(tile,Tile):
            self.tiles[x-1][y-1] = tile
        self.displayPrep()
        
    def incSize(self, x):
        self.rows += x
        self.columns += x
        self.waterFill()
    
    def decSize(self, x):
        self.rows = self.rows - x
        if self.rows < 1:
            self.rows = 1
        self.columns = self.columns - x
        if self.columns < 1:
            self.columns = 1
        self.waterFill()
        
    
    
        
class clickableMap(gameMap,clickable):
    def __init__(self,x,y,w,h,name,rows, **kwargs):
        super(clickableMap, self).__init__(x,y,w,h,name,rows)
    
    def onClick(self):
        for tilelist in self.tiles:
            for tile in tilelist:
                if (mouseX > tile.x and mouseX < tile.x + 0.5 * tile.w and mouseY > tile.y and mouseY < tile.y + tile.h) or \
                (mouseX > tile.x + 0.5*tile.w and mouseY - tile.y > 2 * (mouseX - tile.x) - tile.h and mouseY - tile.y < -2 * (mouseX - tile.x) + 2 * tile.h) or \
                (mouseX < tile.x and mouseY - tile.y > -2 * (mouseX - tile.x) and mouseY - tile.y < 2 * (mouseX - tile.x) + tile.h):
                        tile.onClick()
    
    def onHover(self):
        pass
        
selected = Mountain(0,0,0,0,'')                   
