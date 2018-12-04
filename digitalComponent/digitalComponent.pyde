from gameManagement import *
from screenManagement import *
from testScreen import *
from winScreen import *


def setup():
    fullScreen()
    frameRate(35)
    noStroke()
    # Caladea = loadFont('Caladea-Regular-48.vlw')
    # textFont(Caladea)
    global map1
    global typer
    map1 = clickableMap(1000,300,500,500,'Map1', 5)
    typer = textInput(300,100,1000,100,'textIn1')
    testScreen = Screen('testScreen')
    screenManager.addScreen(testScreen)
    testScreen.addItem(checkbox(200,200,40,20,'checkbox1',False,'kdfs'))
    testScreen.addItem(linkButton(10,10,100,100,'linkButton1','testScreen2',screenManager))
    testScreen.addItem(textBox(10,10,100,100,'buttonTextBox', ' Goto Screen 2', 20))
    testScreen.addItem(linkButton(10,120,100,60,'linkButton2','winScreen',screenManager))
    testScreen.addItem(textBox(10,120,100,100,'buttonTextBox','Goto win screen', 20))
    testScreen.addItem(textBox(300,300,1000,1000,'textBox1', 'Screen 1', 100))
    testScreen.addItem(textBox(300,100,1000,100,'textBox3',typer.intext.tString,20))
    testScreen.addItem(funButton(400,400,100,100,'val+',map1.incSize,1))
    testScreen.addItem(funButton(400,550,100,100,'val-',map1.decSize,1))
    map1.editTile(3,3,clickableDesert(0,0,0,0,''))
    map1.editTile(3,2,clickableSwamp(0,0,0,0,''))
    map1.editTile(1,1,clickableForest(0,0,0,0,''))
    map1.editTile(5,2,clickableMountain(0,0,0,0,''))
    map1.editTile(4,2,clickableHighland(0,0,0,0,''))
    testScreen.addItem(map1)
    screenManager.currentScreen = testScreen
    testScreen2 = Screen('testScreen2')
    screenManager.addScreen(testScreen2)
    testScreen2.addItem(linkButton(10,10,100,100,'linkButton2','testScreen',screenManager))
    testScreen2.addItem(textBox(10,10,100,100,'buttonTextBox', ' Goto Screen 1', 20))
    testScreen2.addItem(textBox(300,300,1000,1000,'textBox2', 'Screen 2', 100))
    testScreen2.addItem(typer)
    winScreen = Screen("winScreen")
    screenManager.addScreen(winScreen)
    winScreen.addItem(textBox(250,100,3000,1000,'textBox1', 'Choose one of the following winconditions', 50))
    winScreen.addItem(textBox(300,250,3000,1000,'textBox1', 'last one standing', 30))
    winScreen.addItem(textBox(750,250,3000,1000,'textBox1', '3 castles', 30))
    winScreen.addItem(textBox(1100,250,3000,1000,'textBox1', 'fist conqueror wins', 30))
    winScreen.addItem(checkbox(400,300,50,25,"last one standing",False,"default"))
    winScreen.addItem(checkbox(800,300,50,25,"3 castles",False,"3caslte"))
    winScreen.addItem(checkbox(1200,300,50,25,"first knocked out",False,"1st"))
    winScreen.addItem(linkButton(10,10,100,100,'linkButton1','winScreen',screenManager))
    winScreen.addItem(textBox(10,10,100,100,'buttonTextBox', ' Goto Screen 2', 20))
    winScreen.addItem(linkButton(10,120,100,60,'linkButton2','winScreen',screenManager))
    winScreen.addItem(textBox(10,120,100,100,'buttonTextBox','Goto win screen', 20))
    winScreen.addItem(textBox(250,400,3000,1000,'`textBox1', 'TEST', 30))
    winScreen.addItem(linkButton(250,400,120,50,'testWin','winScreen2',screenManager))
    winScreen2 = Screen('winScreen2')
    screenManager.addScreen(winScreen2)
    winScreen2.addItem(textBox(200,250,3000,3000,'winText','Winner Winner Chicken Dinner',100,tColor = '17325547'))
    winScreen2.addItem(textBox(1500,1000,3000,3000,'winText',player+' won',30,tColor = '17325547'))
    winScreen2.addItem(textBox(500,500,3000,3000,'winText','restart',100,tColor = '17325547'))
    
    
    

    

    
def draw():
    #reset the background
    background(51)
    # display all items from currentScreen
    screenManager.currentScreen.display()
    
    #check if the mouse hovers over a hoverable
    screenManager.currentScreen.action('hover')
    fill(80)
    
def mouseReleased():
    # check if an item was clicked
    screenManager.currentScreen.action('click')
    
def keyTyped():
     # text input
        screenManager.currentScreen.action('keyPress')
            
