from items import *
from collections import OrderedDict

global pickedColour
pickedColour = '#4A8EA5'

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
    def __init__(self,x,y,w,h,name, gold=0, colour=0, building=0, road=False, civ=False, mil=False,startup=True, **kwargs):
        super(clickableTile, self).__init__(x,y,w,h,name,gold,colour,building,road,civ,mil, **kwargs)
        self.startup = startup
    def onClick(self):
        if self.startup:
            self.colour = pickedColour
    
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
        for a in range(self.columns):
            self.tiles.append(list())
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
        
    def incSize(self):
        self.tiles.insert(0,list())
        for tile in range(self.columns):
            self.tiles[0].append(clickableWater(self.x,self.y,self.w/(self.columns),self.h/(self.rows),''))
        self.tiles.insert(len(self.tiles),list())
        for tile in range(self.columns):
            self.tiles[len(self.tiles)-1].append(clickableWater(self.x,self.y,self.w/(self.columns),self.h/(self.rows),''))
        for tilelist in self.tiles:
            tilelist.insert(0,clickableWater(self.x,self.y,self.w/(self.columns),self.h/(self.rows),''))
            tilelist.insert((len(self.tiles)-1),clickableWater(self.x,self.y,self.w/(self.columns),self.h/(self.rows),''))
        self.rows += 2
        self.columns += 2
        self.displayPrep()
    
    def decSize(self):
        if self.rows > 3 and self.tiles > 3:
            self.rows = self.rows - 2
            self.columns = self.columns - 2
            del(self.tiles[0])
            del(self.tiles[len(self.tiles)-1])
            for tilelist in self.tiles:
                del(tilelist[0])
                del(tilelist[len(tilelist)-1])
        self.displayPrep()
        
    
    
        
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
        
class colourPicker(button):
    def __init__(self,x,y,w,h,name,colour, **kwargs):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.name = name
        colours = ['#DAA33A','#8CA74D','#C02823','#F0E5B4','#3D342D','#4A8EA5']
        if colour in colours:
            self.colour = colour
        else:
            self.colour = '#4A8EA5'
        self.active = False
        
    def display(self):
        if pickedColour == self.colour:
            self.active = True
        else:
            self.active = False
        fill(self.colour)
        if self.active:
            h = createShape()
            h.beginShape()
            h.vertex(self.x,self.y)
            h.vertex(self.x + 0.6*self.w,self.y)
            h.vertex(self.x + 0.9*self.w,self.y+0.6*self.h)
            h.vertex(self.x + 0.6*self.w,self.y+1.1*self.h)
            h.vertex(self.x, self.y + 1.1 * self.h)
            h.vertex(self.x - 0.3*self.w,self.y+0.6*self.h)
            h.endShape(CLOSE)
            shape(h)
        if not self.active:
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
        
    def onClick(self):
        self.active = True
        global pickedColour
        pickedColour = self.colour
        
selected = Mountain(0,0,0,0,'')                   
