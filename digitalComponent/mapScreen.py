from items import *
from screenManagement import *
from collections import OrderedDict
import copy

pickedColour = '#4A8EA5'
pickedBuilding = None



class Tile(item):
    def __init__(self,x,y,w,h,name, gold=0, colour=0, building=0, road=False, civ=False, mil=False,hasRoad=False,building1=None,building2=None,currentBuildings=0, **kwargs):
        super(Tile, self).__init__(x,y,w,h,name, **kwargs)
        self.gold = gold        
        self.colour = colour
        self.building = building
        self.road = road
        self.civ = civ
        self.mil = mil
        self._hasRoad = hasRoad
        self._building1 = building1
        self._building2 = building2
        self.currentBuildings = currentBuildings
        
    def display(self):
        #Draw hexagon
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
        #Draw gold indicator
        ellipse(self.x + 0.05*self.w,self.y + 0.2*self.h,0.2*self.w,0.2*self.h)
        fill(0)
        textSize(0.1*self.w)
        text(str(self.gold),self.x -0.05*self.w,self.y+0.1*self.h,0.2*self.w,0.2*self.h)
        #Draw road slot if present
        if self.road:
            if self._hasRoad:
                fill(50)    
            rect(self.x + 0.1*self.w,self.y + 0.55*self.h,0.2*self.w,0.2*self.h)
            fill(0)
        #Draw building slots if present
        if self.building > 0:
                if self._building1 is not None:
                    # Insert code to load image here
                    stroke(self._building1.owner.colour)
                    rect(self.x + 0.34*self.w,self.y + 0.54*self.h,0.22*self.w,0.22*self.h)
                    stroke(30)
                else:
                    rect(self.x + 0.35*self.w,self.y + 0.55*self.h,0.2*self.w,0.2*self.h)
        if self.building > 1:
                if self._building2 is not None:
                    #insert code to load image here
                    stroke(self._building2.owner.colour)
                    rect(self.x + 0.34*self.w,self.y + 0.19*self.h,0.22*self.w,0.22*self.h)
                    stroke(30)
                else:
                    rect(self.x + 0.35*self.w,self.y + 0.2*self.h,0.2*self.w,0.2*self.h)

    def addRoad(self):
        if self.road:
            self._hasRoad = True
    
    def remRoad(self):
        self._hasRoad = False
        
    def addBuilding(self,building):
        if self.currentBuildings < self.building:
            if self.currentBuildings == 1 and building.owner == self._building1.owner:
                self._building2 = building
                self.currentBuildings +=1
            elif self._building1 is None:
                self._building1 = building
                self.currentBuildings +=1
            
            

class clickableTile(Tile, clickable):
    def __init__(self,x,y,w,h,name, gold=0, colour=0, building=0, road=False, civ=False, mil=False,hasRoad=False,building1=None,building2=None, **kwargs):
        super(clickableTile, self).__init__(x,y,w,h,name,gold,colour,building,road,civ,mil,hasRoad,building1,building2, **kwargs)
        
    def onClick(self):
        pass    
            
    def onHover(self):
        pass
    
    #Conversion methods for internal updating of maps
    def toTile(self):
        return(Tile(self.x,self.y,self.w,self.h,self.name,self.gold,self.colour,self.building,self.road,self.civ,self.mil,self._hasRoad,self._building1,self._building2,self.currentBuildings))
    
    def toShopTile(self,targetBuilding,dest,manager):
        return(shopTile(self.x,self.y,self.w,self.h,self.name,self.gold,self.colour,self.building,self.road,self.civ,self.mil,self._hasRoad,self._building1,self._building2,targetBuilding,dest,manager,self.currentBuildings))
    
    def toBattleTile(self,battle):
        return(battleTile(self.x,self.y,self.w,self.h,self.name,self.gold,self.colour,self.building,self.road,self.civ,self.mil,self._hasRoad,self._building1,self._building2,battle,self.currentBuildings))
    
class setupTile(clickableTile):
    def __init__(self,x,y,w,h,name, gold=0, colour=0, building=0, road=False, civ=False, mil=False,hasRoad=False,building1=None,building2=None, **kwargs):
        super(setupTile, self).__init__(x,y,w,h,name,gold,colour,building,road,civ,mil,hasRoad,building1,building2,**kwargs)
    
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
    
class shopTile(clickableTile):
    def __init__(self,x,y,w,h,name, gold=0, colour=0, building=0, road=False, civ=False, mil=False,hasRoad=False,building1=None,building2=None,targetBuilding=None,dest=None,manager=None,cB=0, **kwargs):
        super(shopTile, self).__init__(x,y,w,h,name,gold,colour,building,road,civ,mil,hasRoad,building1,building2,**kwargs)
        self.targetBuilding = targetBuilding
        self.dest = dest
        self.manager = manager
        self.currentBuildings=cB
        
    def onClick(self):
        if self.targetBuilding is not None:
            if (self.targetBuilding.mil and self.mil) or (self.targetBuilding.civ and self.civ):
                if self.currentBuildings < self.building:
                    if self.currentBuildings == 1 and self.targetBuilding.owner.name == self._building1.owner.name and self.targetBuilding.name != self._building1.name:
                            self._building2 = self.targetBuilding.copy()
                            self.currentBuildings +=1
                    elif self._building1 is None:
                        self._building1 = self.targetBuilding.copy()
                        self.currentBuildings +=1
                        #Determine which tileatrribute to increase in owner, only when building first building on tile
                        out = ''
                        if self.colour == '#DAA33A':
                            out = 'setdesert'
                        elif self.colour == '#8CA74D':
                            out = 'setforest'
                        elif self.colour == '#C02823':
                            out = 'sethighland'
                        elif self.colour == '#F0E5B4':
                            out = 'setmountain'
                        elif self.colour == '#3D342D':
                            out = 'setswamp'
                        #call appropriate setter of the new building owner to increase by one            
                        getattr(self.targetBuilding.owner,out)(1)
                    # self.manager.currentScreen = self.manager.screens.get(self.dest, self.manager.currentScreen)
                    
        
class battleTile(clickableTile):
    def __init__(self,x,y,w,h,name, gold=0, colour=0, building=0, road=False, civ=False, mil=False,hasRoad=False,building1=None,building2=None,battle=None,cB=0, **kwargs):
        super(battleTile, self).__init__(x,y,w,h,name,gold,colour,building,road,civ,mil,hasRoad,building1,building2,**kwargs)
        self.battle = battle
        self.currentBuildings=cB
            
    def onClick(self):
        self.battle.setLocation(self)
        print(self.battle.location)
        
    def remove(self,string):
        if string == 'civ':
            for x in ['farm','village','barracks']:
                if self._building2 is not None:
                    if self._building2.name == x:
                        getattr(self._building2.owner,'set' + x + 's')(-1)
                        self._building2 = None
                        self.currentBuildings -= 1
                    if self._building1 is not None:
                        if self._building1.name == x:
                            getattr(self._building1.owner,'set' + x + 's')(-1)
                            self._building1 = self._building2.copy()
                            self._building2 = None
                            self.currentBuildings -= 1
                elif self._building1 is not None:
                    if self._building1.name == x:
                        getattr(self._building1.owner,'set' + x + 's')(-1)
                        self._building1 = None
                        self.currentBuildings -= 1
                    
        else:
            if self._building2 is not None:
                if self._building2.name == string:
                    getattr(self._building2.owner,'set' + string + 's')(-1)
                    self._building2 = None
                    self.currentBuildings -= 1
                if self._building1 is not None:
                    if self._building1.name == string:
                        getattr(self._building1.owner,'set' + string + 's')(-1)
                        self._building1 = self._building2.copy()
                        self._building2 = None
                        self.currentBuildings -= 1
            elif self._building1 is not None:
                if self._building1.name == string:
                    getattr(self._building1.owner,'set' + string + 's')(-1)
                    self._building1 = None
                    self.currentBuildings -= 1
                
            
                
        
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
        
class shopWater(shopTile):
    def __init__(self,x,y,w,h,name):
        super(shopWater, self).__init__(x,y,w,h,name,0,'#4A8EA5',0,False,False,False)
        
class battleWater(battleTile):
    def __init__(self,x,y,w,h,name):
        super(battleWater, self).__init__(x,y,w,h,name,0,'#4A8EA5',0,False,False,False)
        
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
        
    # Conversion methods for internal updating   
    def toDisplayMap(self):
        out = list()
        for a in range(self.columns):
            out.append(list())
            for b in range (self.rows):
                out[a].append(clickableWater(self.x,self.y,self.w/(self.columns),self.h/(self.rows),''))
        for x in range(len(self.tiles)):
            for y in range(len(self.tiles[x])):
                out[x][y] = self.tiles[x][y].toTile()
        return out
    
    def toShopMap(self,targetBuilding,dest,manager):
        out = list()
        for a in range(self.columns):
            out.append(list())
            for b in range (self.rows):
                out[a].append(clickableWater(self.x,self.y,self.w/(self.columns),self.h/(self.rows),''))
        for x in range(len(self.tiles)):
            for y in range(len(self.tiles[x])):
                out[x][y] = self.tiles[x][y].toShopTile(targetBuilding,dest,manager)
        return out
    
    def toBattleMap(self,battle):
        out = list()
        for a in range(self.columns):
            out.append(list())
            for b in range (self.rows):
                out[a].append(clickableWater(self.x,self.y,self.w/(self.columns),self.h/(self.rows),''))
        for x in range(len(self.tiles)):
            for y in range(len(self.tiles[x])):
                out[x][y] = self.tiles[x][y].toBattleTile(battle)
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
            for callback in self._observers:
                            callback(self)
    
    def decSize(self):
        if self.rows > 3 and self.tiles > 3:
            if self.alt:
                del(self.tiles[0])
                for tilelist in self.tiles:
                    del(tilelist[0])
            else:
                del(self.tiles[len(self.tiles)-1])
                for tilelist in self.tiles:
                    del(tilelist[len(tilelist)-1])
            self.alt = not self.alt
            self.rows -=1
            self.columns -= 1
            self.displayPrep()
            for callback in self._observers:
                            callback(self)
        
        
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
                
class shopMap(clickableMap):
    def __init__(self,x,y,w,h,name,mapParents,targetBuilding,tbParents,dest,manager,**kwargs):
        super(shopMap, self).__init__(x,y,w,h,name,7)
        self.tiles = list()
        self.targetBuilding = targetBuilding
        for a in range(self.columns):
            self.tiles.append(list())
            for b in range (self.rows):
                self.tiles[a].append(shopWater(self.x,self.y,self.w/(self.columns),self.h/(self.rows),''))
        self.displayPrep()
        self.mapParents = mapParents
        for x in self.mapParents:
            x.bindTo(self.update)
        #Updating targetbuidling owner whenver currentplayer changes allows for one shopMap to be used for all players
        self.tbParents = tbParents
        for x in self.tbParents:
            x.bindTo(self.tbUpdate)
        self.dest = dest
        self.manager = manager
            
    def update(self, value):
        self.rows = value.rows
        self.columns = value.columns
        self.tiles = value.toShopMap(self.targetBuilding,self.dest,self.manager)
        self.displayPrep()
        
    def tbUpdate(self,value):
        self.targetBuilding.setOwner(value)
        
    def __str__(self):
        return(self.name)
    
class battleMap(clickableMap):
    def __init__(self,x,y,w,h,name,mapParents,battle,**kwargs):
        super(battleMap, self).__init__(x,y,w,h,name,7)
        self.tiles = list()
        self.battle = battle
        for a in range(self.columns):
            self.tiles.append(list())
            for b in range (self.rows):
                self.tiles[a].append(shopWater(self.x,self.y,self.w/(self.columns),self.h/(self.rows),''))
        self.displayPrep()
        self.mapParents = mapParents
        for x in self.mapParents:
            x.bindTo(self.update)

    def update(self,value):
        self.rows = value.rows
        self.columns = value.columns
        self.tiles = value.toBattleMap(self.battle)
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
