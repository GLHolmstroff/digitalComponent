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
    testScreen2.addItem(dropDown(500,500,500,50,'dropdown1','This is a dropdown menu', 'this is option 1', 'this is option 2'))

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
    for i in range(5):
        game.players.append(Player('player' + str(i), color(60)))
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
    shopScreen.addItem(textBox(30,20,600,100,'currentplayerTextbox',game.currentPlayer.name,40))
    
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
    shopScreen.addItem(variableText(250,100,100,30,'varText1',game.currentPlayer.vals, 'swamp', tSize = 20, tColor = color(255)))
    
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
            
