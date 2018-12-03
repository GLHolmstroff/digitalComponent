from screenManagement import *

class item(object):
    def __init__(self, x,y,w,h,name, **kwargs):
        self.name = name
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
    #default displaying    
    def display(self):
        fill(80)
        rect(self.x,self.y,self.w,self.h)
        
class textBox(item):
    def __init__(self,x,y,w,h,name, tString = '', tSize = 24, tColor = '000000'):
        super(textBox, self).__init__(x,y,w,h,name)
        self.tString = tString
        self.tSize = tSize
        self.tColor = tColor
    
    def display(self):
        fill(self.tColor)
        textSize(self.tSize)
        text(self.tString,self.x,self.y,self.w,self.h)
    
    def addend(self,c):
        self.tString = self.tString + str(c)
    
    def remend(self):
        self.tString = self.tString[0:(len(self.tString)-1)]
     

class clickable(item):
    def __init__(self,x,y,w,h,name, **kwargs):
        super(clickable, self).__init__(x,y,w,h,name, **kwargs)
    
    def onClick(self, *args):
        pass
    
    def onHover(self):
        pass
        
class textInput(clickable):
    def __init__(self,x,y,w,h,name, **kwargs):
        super(textInput, self).__init__(x,y,w,h,name, **kwargs)
        textbox = textBox(self.x,self.y,self.w,self.h,self.name,)
        self.intext = textbox
        self.active = False
    
    def display(self):
        fill(200)
        if self.active:
            fill(255)
        rect(self.x,self.y,self.w,self.h)
        self.intext.display()
    
    def onClick(self):
        self.active = not(self.active)
            
    
    def onKeyPress(self):
        if self.active:
            if key == BACKSPACE:
                self.intext.remend()
            else:
                self.intext.addend(key)
        

class button(clickable):
    def __init__(self,x,y,w,h,name, **kwargs):
        super(button, self).__init__(x,y,w,h,name, **kwargs)
    
    def onClick(self, *args):
        pass
    
    def onHover(self):
        pass
    
class linkButton(button):
    
    def __init__(self,x,y,w,h,name, destination, manager, **kwargs):
        self.dest  = destination
        self.manager = manager
        super(linkButton, self).__init__(x,y,w,h,name, **kwargs)
    
    def onClick(self):
        self.manager.currentScreen = self.manager.screens.get(self.dest, self.manager.currentScreen)
        
class valButton(button):
    def __init__(self,x,y,w,h,name, value, targetVar, **kwargs):
        self.value = value
        self.targetVar = targetVar
        super(valButton, self).__init__(x,y,w,h,name, **kwargs)
    
    def onClick(self, *args):
        self.targetVar += self.value

        
class checkbox(clickable):
    def __init__(self,x,y,w,h,name, defaultValue, targetVar, **kwargs):
       
        self.value = defaultValue 
        super(checkbox, self).__init__(x,y,w,h,name, **kwargs)
    
    def onClick(self, *args):
        self.value = not(self.value)
        
        
    def display(self):

        if(self.value):
            fill(0,200,0)
        else:
            fill(120)
        rect(self.x,self.y,self.w,self.h,12,12,12,12)
        if(self.value):
            fill(0,90,0)
            ellipse(self.x + self.h/2 , self.y + self.h/2, self.w/2, self.h-2)
        else:
            fill(80)
            ellipse(self.x + self.w - self.h/2,self.y + self.h/2 ,self.w/2, self.h-2)

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
        

class Desert(Tile):
    def __init__(self,x,y,w,h,name):
        super(Desert, self).__init__(x,y,w,h,name,2,'#DAA33A',2,True,True,False)

class Forest(Tile):
    def __init__(self,x,y,w,h,name):
        super(Forest, self).__init__(x,y,w,h,name,2,'#8CA74D',1,True,True,True)

class Highland(Tile):
    def __init__(self,x,y,w,h,name):
        super(Highland, self).__init__(x,y,w,h,name,2,'#C02823',2,True,True,True)

class Mountain(Tile):
    def __init__(self,x,y,w,h,name):
        super(Mountain, self).__init__(x,y,w,h,name,3,'#F0E5B4',1,True,False,True)

class Swamp(Tile):
    def __init__(self,x,y,w,h,name):
        super(Swamp, self).__init__(x,y,w,h,name,1,'#3D342D',2,False,True,True)

class Water(Tile):
    def __init__(self,x,y,w,h,name):
        super(Water, self).__init__(x,y,w,h,name,0,'#4A8EA5',0,False,False,False)
        
class gameMap(item):
    def __init__(self, x,y,w,h,name,rows,columns, **kwargs):
        super(gameMap, self).__init__(x,y,w,h,name)
        self.tiles = list()
        self.rows = rows
        self.columns = columns
        for a in range(self.columns):
            self.tiles.append(list())
        for a in range (self.columns):
            for b in range (self.rows):
                self.tiles[b].append(Water(self.x,self.y,self.w/(self.rows*self.columns),self.h/(self.rows*self.columns),''))
        self.displayPrep()
    
    def displayPrep(self):
        for tilelist in self.tiles:
            for tile in tilelist:
                tile.x = self.x
                tile.y = self.y
                tile.w = self.w/(self.rows*self.columns)
                tile.h = self.h/(self.rows*self.columns)
                tile.x = tile.x + 0.75 * self.tiles.index(tilelist) * tile.w
                if self.tiles.index(tilelist) % 2 != 0:
                    tile.y = tile.y + 0.5*tile.h
                tile.y = tile.y + tilelist.index(tile) * tile.h     
                
    def display(self):
        for tilelist in self.tiles:
            for tile in tilelist:
                tile.display()
                   
