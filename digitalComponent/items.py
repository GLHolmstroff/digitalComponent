from screenManagement import *


class item(object):
    def __init__(self, x,y,w,h,name,backgroundColor = color(80), **kwargs):
        self.name = name
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.backgroundColor = backgroundColor
        
    #default displaying    
    def display(self):
        fill(self.backgroundColor)
        rect(self.x,self.y,self.w,self.h)

class img(item):
    def __init__(self,x,y,w,h,name,**kwargs):
        super(img, self).__init__(x,y,w,h,name, **kwargs)
        self.img = loadImage(kwargs.get('imgUrl'))
        
    def display(self):
        image(self.img,self.x,self.y,self.w,self.h)
        
class textBox(item):
    def __init__(self,x,y,w,h,name, tString, tSize = 24, tColor = '000000'):
        super(textBox, self).__init__(x,y,w,h,name)    
        self.tString = tString
        self.tSize = tSize
        self.tColor = tColor
    
    def display(self):
        fill(self.tColor)
        textSize(self.tSize)
        text(str(self.tString),self.x,self.y,self.w,self.h)
    
    def addend(self,c):
        self._tString = self._tString + str(c)
    
    def remend(self):
        self._tString = self._tString[0:(len(self._tString)-1)]
     

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
        textbox = textBox(self.x,self.y,self.w,self.h,self.name,'')
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
    def __init__(self,x,y,w,h,name,tString='', tSize = 20, tColor = '000', **kwargs):
        self.tString = tString
        self.tSize = tSize
        self.tColor = tColor
        super(button, self).__init__(x,y,w,h,name, **kwargs)
    
    def onClick(self, *args):
        pass
    
    def onHover(self):
        pass
    
    def display(self):
        fill(self.backgroundColor)
        rect(self.x,self.y,self.w,self.h,10,10,10,10)
        fill(self.tColor)
        textSize(self.tSize)
        text(self.tString,self.x,self.y,self.w,self.h)
    
class linkButton(button):
    
    def __init__(self,x,y,w,h,name, destination, manager, **kwargs):
        self.dest  = destination
        self.manager = manager
        super(linkButton, self).__init__(x,y,w,h,name, **kwargs)
    
    def onClick(self):
        self.manager.currentScreen = self.manager.screens.get(self.dest, self.manager.currentScreen)
        
class valButton(button):
    def __init__(self,x,y,w,h,name, value, location, item, *targetVars, **kwargs):
        self.value = value
        self.location = location
        self.item = item
        self.targetVars = targetVars
        super(valButton, self).__init__(x,y,w,h,name, **kwargs)
    
    def onClick(self, *args):
        # for x in self.targetVars:
        #     x = x + self.value
        self.location[self.item] += self.value
            
class funButton(button):
    def __init__(self,x,y,w,h,name,fun,arg = None,**kwargs):
        self.fun = fun
        self.arg = arg
        super(funButton, self).__init__(x,y,w,h,name, **kwargs)
    
    def onClick(self):
        if self.arg is not None:
            self.fun(self.arg)
        else:
            self.fun()
        
class varFunButton(funButton):
    def __init__(self,x,y,w,h,name,fun,arg,parents,attrname,**kwargs):
        super(varFunButton, self).__init__(x,y,w,h,name,fun,arg)
        self.parents = parents
        self.attrname = attrname
        for x in range(len(self.parents)):
            self.parents[x].bindTo(self.update)
            
    def update(self,value):
        self.fun = getattr(value, self.attrname)
        
        
class dropDown(clickable):
    def __init__(self,x,y,w,h,name,title,*options,**kwargs):
        super(dropDown, self).__init__(x,y,w,h,name)
        self.title = title
        self.basetitle = title
        self.options = options
        self.active = False
        self.output = 0
        self.baseh = h
        
    def display(self):
        fill(200)
        rect(self.x,self.y,self.w,self.baseh,10,10,10,10)
        fill(0)
        triangle(self.x + 0.85 * self.w, self.y + 0.1 * self.h, self.x + 0.95 * self.w, self.y + 0.1 * self.h, self.x + 0.9* self.w, self.y + 0.8 * self.h )
        text(self.title,self.x,self.y,self.w,self.h)
        if self.active:
            fill(255)
            rect(self.x,self.y,self.w,self.baseh,10,10,10,10)
            fill(0)
            text(self.title,self.x,self.y,self.w,self.h)
            fill(255)
            for option in range(len(self.options)):
                rect(self.x ,self.y + (option+1) * self.baseh,self.w,self.baseh,10,10,10,10)
                fill(0)
                text(str(self.options[option]),self.x,self.y + (option+1) * self.baseh,self.w,self.baseh)
                fill(255)
            
    def onClick(self):
        if mouseX > self.x and mouseX < self.x + self.w and mouseY > self.y and mouseY < self.y + self.h:
            if  not self.active:
                self.active = True
                self.h = (len(self.options) + 1) * self.baseh
            else:
                self.active = False
                self.h = self.baseh
        if mouseX > self.x and mouseX < self.x + self.w and mouseY > self.y + self.baseh and mouseY < self.y + (len(self.options)+1) * self.baseh:
            self.output = (mouseY - self.y)//self.baseh-1
            self.title = str(self.options[self.output])

        
    def onHover(self):
        pass
    
        
class checkbox(clickable):
    def __init__(self,x,y,w,h,name, defaultValue, targetVar, **kwargs):
       
        self.value = defaultValue
        self.targetVar = targetVar 
        super(checkbox, self).__init__(x,y,w,h,name, **kwargs)
    
    def onClick(self, *args):
        self.value = not(self.value)
        self.targetVar = not(self.targetVar)
        
        
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

class variableText(textBox):
    def __init__(self,x,y,w,h,name,location,item, tColor = 'fff', tSize = 20):
        super(variableText,self).__init__(x,y,w,h,name,'')
        self.tColor = tColor
        self.tSize = tSize
        self.location = location
        self.item = item
        self.value = self.location.get(self.item)
        
    def update(self):
        self.value = self.location.get(self.item)
    
    def display(self):
        self.value = self.location.get(self.item)
        fill(self.tColor)
        textSize(self.tSize)
        text(str(self.value), self.x,self.y,self.w,self.h)
        
        
class varBox(textBox):
    def __init__(self,x,y,w,h,name,parents,var,attrname,tColor = 'fff', tSize = 20):
        super(varBox,self).__init__(x,y,w,h,name,'')
        self.tColor = tColor
        self.tSize = tSize
        self.parents = parents
        self.var = var
        self.tString = var
        self.attrname = attrname
        for x in range(len(self.parents)):
            self.parents[x].bindTo(self.update)
        
    def update(self,value):
        self.tString = getattr(value, self.attrname)
        print (self.tString)
    
        
