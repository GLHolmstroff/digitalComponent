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
    testScreen2.addItem(linkButton(10,10,100,100,'linkButton2','testScreen',screenManager, tString = 'Go to Screen 1'))
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
    
    battleSimScreen = Screen('battleSim')
    screenManager.addScreen(battleSimScreen)
    testScreen.addItem(linkButton(10,230,100,100,'battleSimScreen','battleSim',screenManager,tString = 'Battle Simulator'))
    battleSimScreen.addItem(linkButton(10,10,100,100,'linkButton2','testScreen',screenManager, tString = 'Go to Screen 1'))
    battleSimScreen.addItem(linkButton(10,120,100,100,'diceScreen','diceScreen',screenManager, tString = 'Go to Dice'))
    battleSimScreen.addItem(textBox(760,10,400,200,'title', 'Battle Simulator', 60))
    battleSimScreen.addItem(textBox(150,300,100,100,'attacker', 'Attacker', 20))
    battleSimScreen.addItem(textInput(150,375,500,50,'attackerInput'))
    battleSimScreen.addItem(textBox(1670,300,100,100,'troops1', 'Troops', 20))
    battleSimScreen.addItem(textInput(1270,375,500,50,'troopsInput'))
    battleSimScreen.addItem(textBox(150,500,100,100,'defender', 'Defender', 20))
    battleSimScreen.addItem(textInput(150,575,500,50,'defenderInput'))
    battleSimScreen.addItem(textBox(1670,500,100,100,'troops2', 'Troops', 20))
    battleSimScreen.addItem(textInput(1270,575,500,50,'defenderInput'))
    battleSimScreen.addItem(checkbox(1670,650,20,20,'walls',0,'walls'))
    battleSimScreen.addItem(textBox(1680,645,100,24,'walls', 'Walls', 20))
    battleSimScreen.addItem(checkbox(1670,690,20,20,'tower',0,'tower'))
    battleSimScreen.addItem(textBox(1680,685,100,24,'tower', 'Tower', 20))
    battleSimScreen.addItem(checkbox(1670,730,20,20,'castle',0,'castle'))
    battleSimScreen.addItem(textBox(1680,725,100,24,'castle', 'Castle', 20))
    battleSimScreen.addItem(checkbox(1670,770,20,20,'palace',0,'palace'))
    battleSimScreen.addItem(textBox(1680,765,100,24,'palace', 'Palace', 20))
    battleSimScreen.addItem(linkButton(860,880,200,100,'rollButton','diceScreen',screenManager, tString = 'Roll'))
    
    

    
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
            
