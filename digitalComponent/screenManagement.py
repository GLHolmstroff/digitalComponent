from items import *
class Screen():
    
    def __init__(self, name = ''):
        #maybe give option to add objects to screen at the creation of the screen
        self.name = name
        self.items = []
        
    #add a item to the screen itemList
    #maybe let objects themselve add them to a screen at the creation of the object?
    
    def addItem(self, item):
        self.items.append(item)
            
    #remove item from the screen itemlist
    def removeItem(self, item):
        if item in self.items:
            self.items.remove(item)
    
    #display all items inside the screen            
    def display(self):
        for i in self.items:
            i.display()

    #manage actions from user
    def action(self, action, *args):
        #could only think of clicking now
        if action == 'click':
            for item in self.items:
                if isinstance(item, clickable):
                    if mouseX > item.x and mouseX < item.x + item.w and mouseY > item.y and mouseY < item.y + item.h:
                        item.onClick() 
        if action =='hover':
            for item in self.items:
                if isinstance(item, clickable):
                    if mouseX > item.x and mouseX < item.x + item.w and mouseY > item.y and mouseY < item.y + item.h:
                        item.onHover()
        if action =='keyPress':
            for i in self.items:
                if isinstance(i, textInput):
                    i.onKeyPress()  
        
        
class screenManager():
    def __init__(self):
        self.screens = dict()
        self.currentScreen = Screen()

    def addScreen(self,screen):
        if isinstance(screen, Screen):
            self.screens[screen.name] = screen
            
    @property
    def currentScreen(self):
        return(self.currentScreen)
    
    @currentScreen.setter
    def currentScreen(self,screen):
        self.currentScreen = screen
        
# Instantiate screenManager into global variable
screenManager = screenManager()       
    #For some reason this only works here.
    #DO NOT TOUCH UNDER ANY CONDITION
    #DO NOT ANGER THE PROCESSING GODS
    #THEY WILL RAIN DOOM UPON OUR DRAWINGS
    #YOU WILL OPEN THE BOX OF PANDORAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH


    
            
