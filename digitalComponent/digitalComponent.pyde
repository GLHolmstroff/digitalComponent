from gameManagement import *
from screenManagement import *
from testScreen import *


def setup():
    fullScreen()
    frameRate(35)
    noStroke()
    textAlign(CENTER,CENTER)
    # Caladea = loadFont('Caladea-Regular-48.vlw')
    # textFont(Caladea)
    global map1
    global typer
    global game
    game = Game()
    map1 = clickableMap(1000,300,500,500,'Map1', 5)
    typer = textInput(300,100,1000,100,'textIn1')
    testScreen = Screen('testScreen')
    screenManager.addScreen(testScreen)
    testScreen.addItem(checkbox(200,200,40,20,'checkbox1',False,'kdfs'))
    testScreen.addItem(linkButton(10,10,100,100,'linkButton1','testScreen2',screenManager))
    testScreen.addItem(textBox(10,10,100,100,'buttonTextBox', ' Goto Screen 2', 20))
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
    
    startScreen = Screen('startScreen')
    # screenManager.addScreen(startScreen)
    startScreen.addItem(img(width/2 - 250,height/2 - 400,500,600,'logo',imgUrl = 'data\Logo.png'))
    startScreen.addItem(linkButton(width/2-50,height - 140,100,50,'startToTest','testScreen',screenManager,tString = 'Start'))
    screenManager.currentScreen = startScreen
    

    

    
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
            
