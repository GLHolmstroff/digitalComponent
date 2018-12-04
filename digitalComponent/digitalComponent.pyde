from gameManagement import *
from screenManagement import *
from testScreen import *


def setup():
    fullScreen()
    print(width,height)
    frameRate(35)
    noStroke()
    textAlign(CENTER,CENTER)
    game = Game()
    map1 = clickableMap(0.4*width,0.25*height,0.5 * min(width,height),0.5 * min(width,height),'Map1', 5)
    typer = textInput(300,100,1000,100,'textIn1')
    testScreen = Screen('testScreen')
    screenManager.addScreen(testScreen)
    testScreen.addItem(linkButton(10,10,100,100,'linkButton1','testScreen2',screenManager, tString = 'Go to screen 2'))
    testScreen.addItem(textBox(0,0,width,100,'textBox1', 'Map', 50))
    testScreen.addItem(funButton(0.2*width,0.4*height,100,100,'val+',map1.incSize,1))
    testScreen.addItem(funButton(0.2*width,0.6*height,100,100,'val-',map1.decSize,1))
    testScreen.addItem(map1)
    testScreen.addItem(colourPicker(1300,300,100,100,'desertPicker','#DAA33A'))
    testScreen.addItem(colourPicker(1600,300,100,100,'forestPicker','#8CA74D'))
    testScreen.addItem(colourPicker(1300,500,100,100,'highlandPicker','#C02823'))
    testScreen.addItem(colourPicker(1600,500,100,100,'mountainPicker','#F0E5B4'))
    testScreen.addItem(colourPicker(1300,700,100,100,'swampPicker','#3D342D'))
    testScreen.addItem(colourPicker(1600,700,100,100,'waterPicker','#4A8EA5'))
    
    testScreen2 = Screen('testScreen2')
    screenManager.addScreen(testScreen2)
    testScreen2.addItem(linkButton(10,10,100,100,'linkButton2','testScreen',screenManager))
    testScreen2.addItem(textBox(10,10,100,100,'buttonTextBox', ' Goto Screen 1', 20))
    testScreen2.addItem(textBox(300,300,1000,1000,'textBox2', 'Screen 2', 100))
    testScreen2.addItem(typer)
    testScreen2.addItem(dropDown(500,500,500,50,'dropdown1','This is a dropdown menu', 'this is option 1', 'this is option 2'))

    
    startScreen = Screen('startScreen')
    screenManager.addScreen(startScreen)
    startScreen.addItem(img(width/2 - 250,height/2 - 400,500,600,'logo',imgUrl = 'data\Logo.png'))
    startScreen.addItem(linkButton(width/2-50,height - 140,100,50,'startToSetting','settingScreen',screenManager,tString = 'Start'))
    screenManager.currentScreen = startScreen
    
    
    settingScreen = Screen('settingScreen')
    screenManager.addScreen(settingScreen)
    settingScreen.addItem(textBox(500,500,300,30,'AmountOfPlayersText', 'Amount of Players:',20))
    settingScreen.addItem(amountInput(850,500,30,30,'AmountOfplayersInput'))
    settingScreen.addItem(linkButton(width/2-50,height - 140,100,50,'settingToTest','testScreen',screenManager,tString = 'Start'))
    # settingScreen.additem(funButton())

    
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
            
