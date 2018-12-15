from items import *
from collections import OrderedDict

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
    def __init__(self,x,y,w,h,name, gold=0, colour=0, building=0, road=False, civ=False, mil=False, **kwargs):
        super(clickableTile, self).__init__(x,y,w,h,name,gold,colour,building,road,civ,mil, **kwargs)
        
    def onClick(self):
        pass    
            
    def onHover(self):
        pass

class setupTile(clickableTile):
    def __init__(self,x,y,w,h,name, gold=0, colour=0, building=0, road=False, civ=False, mil=False, **kwargs):
        super(setupTile, self).__init__(x,y,w,h,name,gold,colour,building,road,civ,mil,**kwargs)
    
    def onClick(self):
        if pickedColour == '#DAA33A':
            self.colour = pickedColour
            self.gold = 2
            self.building = 2
            self.road = True
            self.civ = True
            self.mil = False
        elif pickedColour == '#8CA74D':
            self.colour = pickedColour
            self.gold = 2
            self.building = 1
            self.road = True
            self.civ = True
            self.mil = True
        elif pickedColour == '#C02823':
            self.colour = pickedColour
            self.gold = 2
            self.building = 2
            self.road = True
            self.civ = True
            self.mil = True
        elif pickedColour == '#F0E5B4':
            self.colour = pickedColour
            self.gold = 3
            self.building = 1
            self.road = True
            self.civ = False
            self.mil = True
        elif pickedColour == '#3D342D':
            self.colour = pickedColour
            self.gold = 1
            self.building = 2
            self.road = False
            self.civ = True
            self.mil = True
        elif pickedColour == '#4A8EA5':
            self.colour = pickedColour
            self.gold = 0
            self.building = 0
            self.road = False
            self.civ = False
            self.mil = False
    

            
class Desert(Tile):
    def __init__(self,x,y,w,h,name):
        super(Desert, self).__init__(x,y,w,h,name,2,'#DAA33A',2,True,True,False)
        
class clickableDesert(clickableTile):
    def __init__(self,x,y,w,h,name):
        super(clickableDesert, self).__init__(x,y,w,h,name,2,'#DAA33A',2,True,True,False)
        
class setupDesert(setupTile):
    def __init__(self,x,y,w,h,name):
        super(setupDesert, self).__init__(x,y,w,h,name,2,'#DAA33A',2,True,True,False)

class Forest(Tile):
    def __init__(self,x,y,w,h,name):
        super(Forest, self).__init__(x,y,w,h,name,2,'#8CA74D',1,True,True,True)

class clickableForest(clickableTile):
    def __init__(self,x,y,w,h,name):
        super(clickableForest, self).__init__(x,y,w,h,name,2,'#8CA74D',1,True,True,True)

class setupForest(setupTile):
    def __init__(self,x,y,w,h,name):
        super(setupForest, self).__init__(x,y,w,h,name,2,'#8CA74D',1,True,True,True)

class Highland(Tile):
    def __init__(self,x,y,w,h,name):
        super(Highland, self).__init__(x,y,w,h,name,2,'#C02823',2,True,True,True)

class clickableHighland(clickableTile):
    def __init__(self,x,y,w,h,name):
        super(clickableHighland, self).__init__(x,y,w,h,name,2,'#C02823',2,True,True,True)
        
class setupHighland(setupTile):
    def __init__(self,x,y,w,h,name):
        super(setupHighland, self).__init__(x,y,w,h,name,2,'#DAA33A',2,True,True,True)

class Mountain(Tile):
    def __init__(self,x,y,w,h,name):
        super(Mountain, self).__init__(x,y,w,h,name,3,'#F0E5B4',1,True,False,True)

class clickableMountain(clickableTile):
    def __init__(self,x,y,w,h,name):
        super(clickableMountain, self).__init__(x,y,w,h,name,3,'#F0E5B4',1,True,False,True)

class setupMountain(setupTile):
    def __init__(self,x,y,w,h,name):
        super(setupMountain, self).__init__(x,y,w,h,name,3,'#DAA33A',1,True,False,True)

class Swamp(Tile):
    def __init__(self,x,y,w,h,name):
        super(Swamp, self).__init__(x,y,w,h,name,1,'#3D342D',2,False,True,True)

class clickableSwamp(clickableTile):
    def __init__(self,x,y,w,h,name):
        super(clickableSwamp, self).__init__(x,y,w,h,name,1,'#3D342D',2,False,True,True)
        
class setupSwamp(setupTile):
    def __init__(self,x,y,w,h,name):
        super(setupSwamp, self).__init__(x,y,w,h,name,1,'#3D342D',2,False,True,True)

class Water(Tile):
    def __init__(self,x,y,w,h,name):
        super(Water, self).__init__(x,y,w,h,name,0,'#4A8EA5',0,False,False,False)

class clickableWater(clickableTile):
    def __init__(self,x,y,w,h,name):
        super(clickableWater, self).__init__(x,y,w,h,name,0,'#4A8EA5',0,False,False,False)
        
class setupWater(setupTile):
    def __init__(self,x,y,w,h,name):
        super(setupWater, self).__init__(x,y,w,h,name,0,'#4A8EA5',0,False,False,False)
        
class gameMap(item):
    def __init__(self, x,y,w,h,name,rows, **kwargs):
        super(gameMap, self).__init__(x,y,w,h,name)
        self.tiles = list()
        self.rows = rows
        self.columns = rows
        for a in range(self.columns):
            self.tiles.append(list())
            for b in range (self.rows):
                self.tiles[a].append(Water(self.x,self.y,self.w/(self.columns),self.h/(self.rows),''))
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
                
class clickableMap(gameMap,clickable):
    def __init__(self,x,y,w,h,name,rows, **kwargs):
        super(clickableMap, self).__init__(x,y,w,h,name,rows)
        self._observers = list()
        self.tiles = list()
        for a in range(self.columns):
            self.tiles.append(list())
            for b in range (self.rows):
                self.tiles[a].append(clickableWater(self.x,self.y,self.w/(self.columns),self.h/(self.rows),''))
        self.displayPrep()
    
    def onClick(self):
        for tilelist in self.tiles:
            for tile in tilelist:
                if (mouseX > tile.x and mouseX < tile.x + 0.5 * tile.w and mouseY > tile.y and mouseY < tile.y + tile.h) or \
                (mouseX > tile.x + 0.5*tile.w and mouseY - tile.y > 2 * (mouseX - tile.x) - tile.h and mouseY - tile.y < -2 * (mouseX - tile.x) + 2 * tile.h) or \
                (mouseX < tile.x and mouseY - tile.y > -2 * (mouseX - tile.x) and mouseY - tile.y < 2 * (mouseX - tile.x) + tile.h):
                        tile.onClick()
                        for callback in self._observers:
                            callback(self)
    
    def onHover(self):
        pass
        
    def toDisplayMap(self):
        out = list(self.tiles)
        # for x in range(len(self.tiles)):
            # for y in range(len(self.tiles[x])):
            #     if self.tiles[x][y].colour == '#DAA33A':
            #         out[x][y] = (Desert(self.x,self.y,self.w,self.h,''))
            #     elif self.tiles[x][y].colour == '#8CA74D':
            #         out[x][y] = (Forest(self.x,self.y,self.w,self.h,''))
            #     elif self.tiles[x][y].colour == '#C02823':
            #         out[x][y] = (Highland(self.x,self.y,self.w,self.h,''))
            #     elif self.tiles[x][y].colour == '#F0E5B4':
            #         out[x][y] = (Mountain(self.x,self.y,self.w,self.h,''))
            #     elif self.tiles[x][y].colour == '#3D342D':
            #         out[x][y] = (Swamp(self.x,self.y,self.w,self.h,''))
            #     else:
            #         out[x][y] = (Water(self.x,self.y,self.w,self.h,''))
        return out
    
    def bindTo(self,callback):
        self._observers.append(callback)

class setupMap(clickableMap):
    def __init__(self,x,y,w,h,name,rows):
        super(setupMap, self).__init__(x,y,w,h,name,rows)
        #Boolean which decides if next added/removed row should be top or bottom
        self.alt = False
        self.tiles = list()
        for a in range(self.columns):
            self.tiles.append(list())
            for b in range (self.rows):
                self.tiles[a].append(setupWater(self.x,self.y,self.w/(self.columns),self.h/(self.rows),''))
        self.displayPrep()
    
    def incSize(self):
        if self.rows < 7 and self.columns < 7:
            self.alt = not self.alt
            if self.alt:
                self.tiles.insert(0,list())
                for tile in range(self.columns):
                    self.tiles[0].append(setupWater(self.x,self.y,self.w/(self.columns),self.h/(self.rows),''))
                for tilelist in self.tiles:
                    tilelist.insert(0,setupWater(self.x,self.y,self.w/(self.columns),self.h/(self.rows),''))
            else:    
                self.tiles.insert(len(self.tiles),list())
                for tile in range(self.columns):
                    self.tiles[len(self.tiles)-1].append(setupWater(self.x,self.y,self.w/(self.columns),self.h/(self.rows),''))
                for tilelist in self.tiles:
                    tilelist.insert((len(self.tiles)-1),setupWater(self.x,self.y,self.w/(self.columns),self.h/(self.rows),''))
            self.rows += 1
            self.columns += 1
            self.displayPrep()
    
    def decSize(self):
        if self.rows > 3 and self.tiles > 3:
            self.alt = not self.alt
            if self.alt:
                del(self.tiles[0])
                for tilelist in self.tiles:
                    del(tilelist[0])
            else:
                del(self.tiles[len(self.tiles)-1])
                for tilelist in self.tiles:
                    del(tilelist[len(tilelist)-1])
            self.rows -=1
            self.columns -= 1
            self.displayPrep()
        
        
class displayMap(gameMap):
    def __init__(self,x,y,w,h,name,parents,**kwargs):
        super(displayMap, self).__init__(x,y,w,h,name,7)
        self.parents = parents
        for x in self.parents:
            x.bindTo(self.update)
        
    def update(self, value):
        self.rows = value.rows
        self.columns = value.columns
        self.tiles = value.toDisplayMap()
        self.displayPrep()
                
        
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
