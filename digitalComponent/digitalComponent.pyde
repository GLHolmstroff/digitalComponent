from gameManagement import *
from screenManagement import *
from testScreen import *
from dice import *
from winScreen import *


def setup():
    fullScreen()
    print(width,height)
    frameRate(35)
    # noStroke()
    textAlign(CENTER,CENTER)
    game = Game()
    map1 = clickableMap(0.3*width,0.1*height,0.75 * min(width,height),0.75 * min(width,height),'Map1', 5)
    typer = textInput(300,100,1000,100,'textIn1')
    testScreen = Screen('testScreen')
    screenManager.addScreen(testScreen)
    testScreen.addItem(linkButton(10,10,100,100,'linkButton1','winScreen',screenManager, tString = 'Go to winScreen'))
    testScreen.addItem(linkButton(10,120,100,100,'mapToShop','shopScreen',screenManager, tString = 'Go to Shop'))
    testScreen.addItem(textBox(0,0,width,100,'textBox1', 'Map', 50))
    testScreen.addItem(funButton(0.2*width,0.4*height,100,100,'val+',map1.incSize,tString='+'))
    testScreen.addItem(funButton(0.2*width,0.6*height,100,100,'val-',map1.decSize,tString='-'))
    testScreen.addItem(map1)
    testScreen.addItem(colourPicker(1300,300,100,100,'desertPicker','#DAA33A'))
    testScreen.addItem(colourPicker(1600,300,100,100,'forestPicker','#8CA74D'))
    testScreen.addItem(colourPicker(1300,500,100,100,'highlandPicker','#C02823'))
    testScreen.addItem(colourPicker(1600,500,100,100,'mountainPicker','#F0E5B4'))
    testScreen.addItem(colourPicker(1300,700,100,100,'swampPicker','#3D342D'))
    testScreen.addItem(colourPicker(1600,700,100,100,'waterPicker','#4A8EA5'))

    testScreen2 = Screen('testScreen2')
    screenManager.addScreen(testScreen2)
    testScreen2.addItem(linkButton(10,10,100,100,'linkButton2','testScreen',screenManager, tString = 'Go to Screen 1'))
    testScreen2.addItem(textBox(300,300,1000,1000,'textBox2', 'Screen 2', 100))
    testScreen2.addItem(typer)
    testScreen2.addItem(dropDown(500,500,500,50,'dropdown1','This is a dropdown menu', 'this is option 1', 'this is option 2'))
    dice1 = dice(200,500,100,100,'dice1',1)
    dice2 = dice(300,500,100,100,'dice2',2)
    dice3 = dice(400,500,100,100,'dice3',3)
    dice4 = dice(500,500,100,100,'dice4',4)
    dice5 = dice(600,500,100,100,'dice5',5)
    dice6 = dice(700,500,100,100,'dice6',6)
    dice7 = dice(200,300,100,100,'dice7',1)
    dice8 = dice(300,300,100,100,'dice8',2)
    dice9 = dice(400,300,100,100,'dice9',3)
    dice10 = dice(500,300,100,100,'dice10',4)
    dice11 = dice(600,300,100,100,'dice11',5)
    dice12 = dice(700,300,100,100,'dice12',6)
    diceGroup1 = diceGroup(200,500,600,100,'diceGroup1',dice1,dice2,dice3,dice4,dice5,dice6)
    diceGroup2 = diceGroup(200,300,600,100,'diceGroup2',dice7,dice8,dice9,dice10,dice11,dice12)
    testScreen2.addItem(diceGroup1)
    testScreen2.addItem(diceGroup2)
    diceScreen = Screen('diceScreen')
    screenManager.addScreen(diceScreen)
    diceScreen.addItem(diceGroup1)
    diceScreen.addItem(diceGroup2)
    testScreen2.addItem(dropDown(500,500,500,50,'dropdown1','This is a dropdown menu', 'this is option 1', 'this is option 2'))

    winScreen = Screen("winScreen")
    screenManager.addScreen(winScreen)
    laststanding = False
    winScreen.addItem(textBox(250,100,900,100,'textBox1', 'Choose one of the following winconditions', 50))
    winScreen.addItem(textBox(350,250,500,100,'textBox1', 'last one standing', 30))
    winScreen.addItem(textBox(700,250,500,100,'textBox1', '3 castles', 30))
    winScreen.addItem(textBox(1200,250,500,100,'textBox1', 'fist conqueror wins', 30))
    winScreen.addItem(checkbox(400,300,50,25,"last one standing",False,laststanding))
    winScreen.addItem(checkbox(800,300,50,25,"3 castles",False,"3caslte"))
    winScreen.addItem(checkbox(1200,300,50,25,"first knocked out",False,"1st"))
    winScreen.addItem(linkButton(10,10,100,100,'linkButton1','testScreen',screenManager, tString='Go to Map'))
    winScreen.addItem(linkButton(10,120,100,100,'linkButton2','battleSim',screenManager, tString='Go to Battle'))
    winScreen.addItem(textBox(250,400,3000,1000,'`textBox1', 'TEST', 30))
    winScreen.addItem(linkButton(250,400,120,50,'testWin','winScreen2',screenManager))
    winScreen2 = Screen('winScreen2')
    screenManager.addScreen(winScreen2)
    winScreen2.addItem(textBox(200,250,1000,500,'winText','Winner Winner Chicken Dinner',100,tColor = '17325547'))
    winScreen2.addItem(textBox(200,450,1000,500,'winText',player+' won',30,tColor = '17325547'))
    # winScreen2.addItem(textBox(500,500,100,100,'winText','restart',100,tColor = '17325547'))


    startScreen = Screen('startScreen')
    screenManager.addScreen(startScreen)
    startScreen.addItem(img(width/2 - 250,height/2 - 400,500,600,'logo',imgUrl = 'data\Logo.png'))
    startScreen.addItem(linkButton(width/2-50,height - 140,100,50,'startToSetting','settingScreen',screenManager,tString = 'Start'))
    screenManager.currentScreen = startScreen


    settingScreen = Screen('settingScreen')
    screenManager.addScreen(settingScreen)

    settingScreen.addItem(textBox(width/2 - 150,height/2,200,50,'amountOfPlayersText','Amount of players:',20, tColor = '#ffffff'))
    settingScreen.addItem(dropDown(width/2+50,height/2,100,50,'dropdown1','1', '2','3','4'))
    settingScreen.addItem(linkButton(width/2-50,height - 140,100,50,'settingToTest','shopScreen',screenManager,tString = 'Start'))

    #I make 4 players just for testing
    for i in range(4):
        game.players.append(Player('player ' + str(i + 1), color(60)))
    game.currentPlayer = game.players[i]
    game.currentPlayerIndex = i

    #a lot of code for the shopScreen
    shopScreen = Screen('shopScreen')
    screenManager.addScreen(shopScreen)
    sideBar = item(width-400,0,400,height,'sideBar')
    sideBar.backgroundColor = color(30)
    shopScreen.addItem(sideBar)
    playersOverview = item(0,height - 500,width-400,500,'playersOverview')
    playersOverview.backgroundColor = color(81)
    shopScreen.addItem(playersOverview)
    currentplayerbox = varBox(30,20,600,100,'currentplayerTextbox', game.currentPlayer,'name' ,tSize = 40, tColor = color(0))
    print(game.currentPlayer.name)
    print(currentplayerbox.var)
    game.nextPlayer()
    print(game.currentPlayer.name)
    print(currentplayerbox.var)
    shopScreen.addItem(currentplayerbox)

    #adding all the add buttons
    t = textBox(width - 380, 30, 280, 40, 'swampTextbox', 'Swamp', 20)
    t.backgroundColor = color(30)
    t.tColor = '#ffffff'
    shopScreen.addItem(t)
    shopScreen.addItem(valButton(width - 90, 30, 80, 40, 'addSwampButton',1, game.currentPlayer.vals, 'swamp' ))
    shopScreen.addItem(textBox(width - 90, 30, 80, 40, 'addSwampButtonText', 'add', 20))

    t = textBox(width - 380, 130, 280, 40, 'desertTextbox', 'Desert', 20)
    t.backgroundColor = color(30)
    t.tColor = '#ffffff'
    shopScreen.addItem(t)
    shopScreen.addItem(valButton(width - 90, 130, 80, 40, 'addDeserButton',1, game.currentPlayer.vals, 'desert'))
    shopScreen.addItem(textBox(width - 90, 130, 80, 40, 'addDesertButtonText', 'add', 20))

    t = textBox(width - 380, 230, 280, 40, 'mountainsTextbox', 'Mountains', 20)
    t.backgroundColor = color(30)
    t.tColor = '#ffffff'
    shopScreen.addItem(t)
    shopScreen.addItem(valButton(width - 90, 230, 80, 40, 'addMountainsButton',1, game.currentPlayer.vals, 'mountain'))
    shopScreen.addItem(textBox(width - 90, 230, 80, 40, 'addMountainsButtonText', 'add', 20))

    t = textBox(width - 380, 330, 280, 40, 'forestTextbox', 'Forest', 20)
    t.backgroundColor = color(30)
    t.tColor = '#ffffff'
    shopScreen.addItem(t)
    shopScreen.addItem(valButton(width - 90, 330, 80, 40, 'addForestButton',1, game.currentPlayer.vals, 'forest'))
    shopScreen.addItem(textBox(width - 90, 330, 80, 40, 'addForestButtonText', 'add', 20))

    t = textBox(width - 380, 430, 280, 40, 'highlandsTextbox', 'Highlands', 20)
    t.backgroundColor = color(30)
    t.tColor = '#ffffff'
    shopScreen.addItem(t)
    shopScreen.addItem(valButton(width - 90, 430, 80, 40, 'addHighlandsButton',1, game.currentPlayer.vals, 'highland'))
    shopScreen.addItem(textBox(width - 90, 430, 80, 40, 'addHighlandsButtonText', 'add', 20))





    t = textBox(width - 380, 1030, 280, 40, 'castleTextbox', 'Castle', 20)
    t.backgroundColor = color(30)
    t.tColor = '#ffffff'
    shopScreen.addItem(t)
    shopScreen.addItem(valButton(width - 90, 1030, 80, 40, 'addCastleButton',1, game.currentPlayer.vals, 'castles'))
    shopScreen.addItem(textBox(width - 90, 1030, 80, 40, 'addCastleButtonText', 'add', 20))

    t = textBox(width - 380, 530, 280, 40, 'towerTextbox', 'Tower', 20)
    t.backgroundColor = color(30)
    t.tColor = '#ffffff'
    shopScreen.addItem(t)
    shopScreen.addItem(valButton(width - 90, 530, 80, 40, 'addTowerButton',1, game.currentPlayer.vals, 'towers'))
    shopScreen.addItem(textBox(width - 90, 530, 80, 40, 'addTowerButtonText', 'add', 20))

    t = textBox(width - 380, 630, 280, 40, 'farmTextbox', 'Farm', 20)
    t.backgroundColor = color(30)
    t.tColor = '#ffffff'
    shopScreen.addItem(t)
    shopScreen.addItem(valButton(width - 90, 630, 80, 40, 'addFarmButton',1, game.currentPlayer.vals, 'farms'))
    shopScreen.addItem(textBox(width - 90, 630, 80, 40, 'addFarmButtonText', 'add', 20))

    t = textBox(width - 380, 730, 280, 40, 'villageTextbox', 'Village', 20)
    t.backgroundColor = color(30)
    t.tColor = '#ffffff'
    shopScreen.addItem(t)
    shopScreen.addItem(valButton(width - 90, 730, 80, 40, 'addVillageButton',1, game.currentPlayer.vals, 'villages'))
    shopScreen.addItem(textBox(width - 90, 730, 80, 40, 'addVillageText', 'add', 20))

    t = textBox(width - 380, 830, 280, 40, 'barracksTextbox', 'Barracks', 20)
    t.backgroundColor = color(30)
    t.tColor = '#ffffff'
    shopScreen.addItem(t)
    shopScreen.addItem(valButton(width - 90, 830, 80, 40, 'addBarracksButton',1, game.currentPlayer.vals, 'barracks'))
    shopScreen.addItem(textBox(width - 90, 830, 80, 40, 'addBarracksButtonText', 'add', 20))

    t = textBox(width - 380, 930, 280, 40, 'wallsTextbox', 'Walls', 20)
    t.backgroundColor = color(30)
    t.tColor = '#ffffff'
    shopScreen.addItem(t)
    shopScreen.addItem(valButton(width - 90, 930, 80, 40, 'addWallsButton',1, game.currentPlayer.vals, 'walls'))
    shopScreen.addItem(textBox(width - 90, 930, 80, 40, 'addWallsButtonText', 'add', 20))

    shopScreen.addItem(textBox(40,100,200,30,'currentPlayerSwampText', 'Swamps:',20,color(255)))
    shopScreen.addItem(variableText(250,100,100,30,'varText1',game.currentPlayer.vals,'swamp',tSize = 20, tColor = color(255)))

    shopScreen.addItem(textBox(40,140,200,30,'currentPlayerDesertText', 'Deserts:',20,color(255)))
    shopScreen.addItem(variableText(250,140,100,30,'varText1',game.currentPlayer.vals, 'desert', tSize = 20, tColor = color(255)))

    shopScreen.addItem(textBox(40,180,200,30,'currentPlayerMountainText', 'Mountains:',20,color(255)))
    shopScreen.addItem(variableText(250,180,100,30,'varText1',game.currentPlayer.vals, 'mountain', tSize = 20, tColor = color(255)))

    shopScreen.addItem(textBox(40,220,200,30,'currentPlayerForestText', 'Forests:',20,color(255)))
    shopScreen.addItem(variableText(250,220,100,30,'varText1',game.currentPlayer.vals, 'forest', tSize = 20, tColor = color(255)))

    shopScreen.addItem(textBox(40,260,200,30,'currentPlayerHighlandText', 'Highlands:',20,color(255)))
    shopScreen.addItem(variableText(250,260,100,30,'varText1',game.currentPlayer.vals, 'highland', tSize = 20, tColor = color(255)))


    shopScreen.addItem(textBox(340,100,200,30,'currentPlayerPalacesText', 'Palaces:',20,color(255)))
    shopScreen.addItem(variableText(550,100,100,30,'varText1',game.currentPlayer.vals, 'palaces', tSize = 20, tColor = color(255)))

    shopScreen.addItem(textBox(340,140,200,30,'currentPlayerVillagesText', 'Villages:',20,color(255)))
    shopScreen.addItem(variableText(550,140,100,30,'varText1',game.currentPlayer.vals, 'villages', tSize = 20, tColor = color(255)))

    shopScreen.addItem(textBox(340,180,200,30,'currentPlayerFarmsText', 'Farms:',20,color(255)))
    shopScreen.addItem(variableText(550,180,100,30,'varText1',game.currentPlayer.vals, 'farms', tSize = 20, tColor = color(255)))

    shopScreen.addItem(textBox(340,220,200,30,'currentPlayerCastlesText', 'Castles:',20,color(255)))
    shopScreen.addItem(variableText(550,220,100,30,'varText1',game.currentPlayer.vals, 'castles', tSize = 20, tColor = color(255)))

    shopScreen.addItem(textBox(340,260,200,30,'currentPlayerBarracksText', 'Barracks:',20,color(255)))
    shopScreen.addItem(variableText(550,260,100,30,'varText1',game.currentPlayer.vals, 'barracks', tSize = 20, tColor = color(255)))

    shopScreen.addItem(textBox(340,300,200,30,'currentPlayerWallsText', 'Walls:',20,color(255)))
    shopScreen.addItem(variableText(550,300,100,30,'varText1',game.currentPlayer.vals, 'walls', tSize = 20, tColor = color(255)))

    shopScreen.addItem(textBox(340,340,200,30,'currentPlayerTowersText', 'Towers:',20,color(255)))
    shopScreen.addItem(variableText(550,340,100,30,'varText1',game.currentPlayer.vals, 'towers', tSize = 20, tColor = color(255)))

    shopScreen.addItem(funButton(400, height - 100, 200,50,'nextPlayerButton',game.nextPlayer, tString = 'next player',tColor = color(255), backgroundColor = color(51)))
    shopScreen.addItem(linkButton(400, height - 200, 200,50,'mapButton','testScreen',screenManager, tString = 'Go to Map',tColor = color(255), backgroundColor = color(51)))
    
    battleSimScreen = Screen('battleSim')
    screenManager.addScreen(battleSimScreen)
    testScreen.addItem(linkButton(10,230,100,100,'battleSimScreen','battleSim',screenManager,tString = 'Battle Simulator'))
    battleSimScreen.addItem(linkButton(10,10,100,100,'linkButton2','testScreen',screenManager, tString = 'Go to Map'))
    # battleSimScreen.addItem(linkButton(10,120,100,100,'diceScreen','diceScreen',screenManager, tString = 'Go to Dice'))
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
