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
    def __init__(self,x,y,w,h,name, value, *targetVars, **kwargs):
        self.value = value
        self.targetVars = targetVars
        super(valButton, self).__init__(x,y,w,h,name, **kwargs)
    
    def onClick(self, *args):
        for x in self.targetVars:
            x = x + self.value
            
class funButton(button):
    def __init__(self,x,y,w,h,name,fun,*args,**kwargs):
        self.fun = fun
        self.args = args
        super(funButton, self).__init__(x,y,w,h,name, **kwargs)
    
    def onClick(self, *args):
        self.fun(*self.args)

        
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
