from gameManagement import *
from screenManagement import *
from mapScreen import *
from dice import *
from winScreen import *



def setUpGame():
    game = Game(screenManager)
    battle = Battle(game)
    
    # I make 4 players just for testing
    # player1 = Player('player 1',color(255,255,255))
    # player2 = Player('player 2',color(255,0,0))
    # player3 = Player('player 3',color(0,255,0))
    # player4 = Player('player 4',color(0,0,255))
    # game.players.append(player1)
    # game.players.append(player2)
    # game.players.append(player3)
    # game.players.append(player4)
    # game._currentPlayer = player1
    # game._currentPlayerIndex = 0

    shopFarm = Farm(0,0,0,0,'farm',game._currentPlayer)
    shopVillage = Village(0,0,0,0,'village',game._currentPlayer)
    shopBarracks = Barracks(0,0,0,0,'barracks',game._currentPlayer)
    shopWalls = Walls(0,0,0,0,'wall',game._currentPlayer)
    shopTower = Tower(0,0,0,0,'tower',game._currentPlayer)
    shopCastle = Castle(0,0,0,0,'castle',game._currentPlayer)
    shopRoad = Road(0,0,0,0,'road')
    palace = Palace(0,0,0,0,'palace',game._currentPlayer)
    
    setupmap = setupMap(0.3*width,0.3*height,0.60 * min(width,height),0.60 * min(width,height),'setupMap', 5)
    palaceMap = shopMap(0.3*width,0.3*height,0.60 * min(width,height),0.60 * min(width,height),'Map',(setupmap,),palace,(game,),'shopScreen',screenManager)
    farmMap = shopMap(0.3*width,0.22*height,0.7 * min(width,height),0.7 * min(width,height),'shopFarmMap',(palaceMap,),shopFarm,(game,),'shopScreen',screenManager)
    villageMap = shopMap(0.3*width,0.22*height,0.7 * min(width,height),0.7 * min(width,height),'shopVillageMap',(palaceMap,),shopVillage,(game,),'shopScreen',screenManager)
    barracksMap = shopMap(0.3*width,0.22*height,0.7 * min(width,height),0.7 * min(width,height),'shopBarracksMap',(palaceMap,),shopBarracks,(game,),'shopScreen',screenManager)
    wallsMap = shopMap(0.3*width,0.22*height,0.7 * min(width,height),0.7 * min(width,height),'shopWallsMap',(palaceMap,),shopWalls,(game,),'shopScreen',screenManager)
    towerMap = shopMap(0.3*width,0.22*height,0.7 * min(width,height),0.7 * min(width,height),'shopTowerMap',(palaceMap,),shopTower,(game,),'shopScreen',screenManager)
    castleMap = shopMap(0.3*width,0.22*height,0.7 * min(width,height),0.7 * min(width,height),'shopCastleMap',(palaceMap,),shopCastle,(game,),'shopScreen',screenManager)
    roadMap = shopMap(0.3*width,0.22*height,0.7 * min(width,height),0.7 * min(width,height),'shopRoadMap',(palaceMap,),shopRoad,(game,),'shopScreen',screenManager)
    batMap = battleMap(0.3*width,0.22*height,0.7 * min(width,height),0.7 * min(width,height),'battleMap',(palaceMap,),battle)
    map2 = displayMap(0.3*width,0.22*height,0.7 * min(width,height),0.7 * min(width,height),'displayMap',(palaceMap,farmMap,villageMap,barracksMap,wallsMap,towerMap,castleMap,batMap))
    
    testScreen = Screen('testScreen')
    screenManager.addScreen(testScreen)
    testScreen.addItem(item(0,0,width,200,'titleBarBackground', backgroundColor ="#2C3531"))
    testScreen.addItem(textBox(0,0,width,200,'titleBar', 'Create your map', 50))
    testScreen.addItem(funButton(0.2*width,0.4*height,80,50,'val+',setupmap.incSize,tString='+',tSize = 30))
    testScreen.addItem(funButton(0.2*width,0.6*height,80,50,'val-',setupmap.decSize,tString='-',tSize = 30))
    testScreen.addItem(setupmap)
    testScreen.addItem(colourPicker(1300,300,100,100,'desertPicker','#DAA33A'))
    testScreen.addItem(colourPicker(1600,300,100,100,'forestPicker','#8CA74D'))
    testScreen.addItem(colourPicker(1300,500,100,100,'highlandPicker','#C02823'))
    testScreen.addItem(colourPicker(1600,500,100,100,'mountainPicker','#F0E5B4'))
    testScreen.addItem(colourPicker(1300,700,100,100,'swampPicker','#3D342D'))
    testScreen.addItem(colourPicker(1600,700,100,100,'waterPicker','#4A8EA5'))
    testScreen.addItem(linkButton(50, height - 140,100,50,'testToStartDice', 'startDiceScreen',screenManager,tString = 'Back'))
    testScreen.addItem(linkButton(width - 150, height - 140,100,50,'testToPalace','palaceScreen',screenManager,tString = 'Next'))
    
    palaceScreen = Screen('palaceScreen')
    screenManager.addScreen(palaceScreen)
    palaceScreen.addItem(item(0,0,width,200,'titleBarBackground', backgroundColor ="#2C3531"))
    palaceScreen.addItem(textBox(0,0,width,200,'titleBar', 'Pick your starting tile', 50))
    palaceScreen.addItem(linkButton(width - 150, height - 190,100,100,'Begin game button','shopScreen',screenManager, tString = 'Begin game'))
    palaceScreen.addItem(palaceMap)
    palaceScreen.addItem(funButton(1300, 0.5*height, 200,50,'nextPlayerButton',game.nextPlayer, tString = 'next player',tColor = color(255), backgroundColor = color(51)))
    palaceScreen.addItem(funButton(1300,0.6*height,200,50,'defMapButton',palaceMap.toDefaultMap,arg = game.players,tString='Set default',tColor = color(255),backgroundColor = color(51)))
    
    mapScreen = Screen('mapScreen')
    screenManager.addScreen(mapScreen)
    mapScreen.addItem(item(0,0,width,200,'titleBarBackground', backgroundColor ="#2C3531"))
    mapScreen.addItem(textBox(0,0,width,200,'titleBar', 'MAP', 50))
    mapScreen.addItem(map2)
    mapScreen.addItem(linkButton(30,height-100,100,50,'linkButton1','shopScreen',screenManager, tString = 'Shop'))
    mapScreen.addItem(linkButton(width-130,height-100,100,50,'linkButton1','battleSim',screenManager, tString = 'Battle'))
    
    shopFarmMapScreen = Screen('shopFarmMapScreen')
    screenManager.addScreen(shopFarmMapScreen)
    
    shopFarmMapScreen.addItem(item(0,0,width,200,'titleBarBackground', backgroundColor ="#2C3531"))
    shopFarmMapScreen.addItem(textBox(0,0,width,200,"titleBar", "Place your farm",50))
    shopFarmMapScreen.addItem(farmMap)
    shopFarmMapScreen.addItem(mapUpdateButton(30,height-100,100,50,'farmMapUpdate',(farmMap,),'shopScreen',screenManager,villageMap,barracksMap,wallsMap,towerMap,castleMap,batMap,roadMap, tString = 'Back'))
    
    shopVillageMapScreen = Screen('shopVillageMapScreen')
    screenManager.addScreen(shopVillageMapScreen)
    shopVillageMapScreen.addItem(item(0,0,width,200,'titleBarBackground', backgroundColor ="#2C3531"))
    shopVillageMapScreen.addItem(textBox(0,0,width,200,"titleBar", "Place your village",50))
    shopVillageMapScreen.addItem(villageMap)
    shopVillageMapScreen.addItem(mapUpdateButton(30,height-100,100,50,'villageMapUpdate',(villageMap,),'shopScreen',screenManager,farmMap,barracksMap,wallsMap,towerMap,castleMap,batMap,roadMap, tString = 'Back'))
    
    shopBarracksMapScreen = Screen('shopBarracksMapScreen')
    screenManager.addScreen(shopBarracksMapScreen)
    shopBarracksMapScreen.addItem(item(0,0,width,200,'titleBarBackground', backgroundColor ="#2C3531"))
    shopBarracksMapScreen.addItem(textBox(0,0,width,200,"titleBar", "Place your barrack",50))
    shopBarracksMapScreen.addItem(barracksMap)
    shopBarracksMapScreen.addItem(mapUpdateButton(30,height-100,100,50,'barracksMapUpdate',(barracksMap,),'shopScreen',screenManager,farmMap,villageMap,wallsMap,towerMap,castleMap,batMap,roadMap, tString = 'Back'))
    
    shopWallsMapScreen = Screen('shopWallsMapScreen')
    screenManager.addScreen(shopWallsMapScreen)
    shopWallsMapScreen.addItem(item(0,0,width,200,'titleBarBackground', backgroundColor ="#2C3531"))
    shopWallsMapScreen.addItem(textBox(0,0,width,200,"titleBar", "Place your wall",50))
    shopWallsMapScreen.addItem(wallsMap)
    shopWallsMapScreen.addItem(mapUpdateButton(30,height-100,100,50,'wallsMapUpdate',(wallsMap,),'shopScreen',screenManager,farmMap,villageMap,barracksMap,towerMap,castleMap,batMap,roadMap, tString = 'Back'))
    
    shopTowerMapScreen = Screen('shopTowerMapScreen')
    screenManager.addScreen(shopTowerMapScreen)
    shopTowerMapScreen.addItem(item(0,0,width,200,'titleBarBackground', backgroundColor ="#2C3531"))
    shopTowerMapScreen.addItem(textBox(0,0,width,200,"titleBar", "Place your tower",50))
    shopTowerMapScreen.addItem(towerMap)
    shopTowerMapScreen.addItem(mapUpdateButton(30,height-100,100,50,'towerMapUpdate',(towerMap,),'shopScreen',screenManager,farmMap,villageMap,barracksMap,wallsMap,castleMap,batMap,roadMap, tString = 'Back'))
    
    shopCastleMapScreen = Screen('shopCastleMapScreen')
    screenManager.addScreen(shopCastleMapScreen)
    shopCastleMapScreen.addItem(item(0,0,width,200,'titleBarBackground', backgroundColor ="#2C3531"))
    shopCastleMapScreen.addItem(textBox(0,0,width,200,"titleBar", "Place your castle",50))
    shopCastleMapScreen.addItem(castleMap)
    shopCastleMapScreen.addItem(mapUpdateButton(30,height-100,100,50,'castleMapUpdate',(castleMap,),'shopScreen',screenManager,farmMap,villageMap,barracksMap,wallsMap,towerMap,batMap,roadMap, tString = 'Back'))
    
    shopRoadMapScreen = Screen('shopRoadMapScreen')
    screenManager.addScreen(shopRoadMapScreen)
    shopRoadMapScreen.addItem(item(0,0,width,200,'titleBarBackground', backgroundColor ="#2C3531"))
    shopRoadMapScreen.addItem(textBox(0,0,width,200,"titleBar", "Place your Road",50))
    shopRoadMapScreen.addItem(roadMap)
    shopRoadMapScreen.addItem(mapUpdateButton(30,height-100,100,50,'roadMapUpdate',(roadMap,),'shopScreen',screenManager,farmMap,villageMap,barracksMap,wallsMap,towerMap,castleMap,batMap, tString = 'Back'))
    
    battleMapScreen = Screen('battleMapScreen')
    screenManager.addScreen(battleMapScreen)
    battleMapScreen.addItem(item(0,0,width,200,'titleBarBackground', backgroundColor ="#2C3531"))
    battleMapScreen.addItem(textBox(0,0,width,200,'titleBar', 'Pick the tile you are going to attack', 50))
    battleMapScreen.addItem(batMap)
    battleMapScreen.addItem(mapUpdateButton(30,height-100,100,50,'battleMapUpdate',(castleMap,),'battleSim',screenManager,farmMap,villageMap,barracksMap,wallsMap,towerMap,castleMap,roadMap,map2, tString = 'Back'))
    battle.setDamToDef(30)
    battleMapScreen.addItem(linkButton(1200,height/2 - 100,100,50,'toDiceButton','diceScreen',screenManager,tString = 'Fight!'))
    
    
    winScreen = Screen("winScreen")
    screenManager.addScreen(winScreen)
    winScreen.addItem(textBox(200,250,1000,500,'winText','Winner Winner Chicken Dinner',100,tColor = '#FFCB9A'))
    winScreen.addItem(winBox(200,450,1000,500,'winText',(game,),'name',tSize = 30, tColor = '#FFCB9A'))
    winScreen.addItem(linkButton(width-230, height - 140,200,50,'winToStart', 'startScreen',screenManager,tString = 'Play again'))
    
    
    winScreen2 = Screen('winScreen2')
    screenManager.addScreen(winScreen2)
    winScreen2.addItem(textBox(200,250,1000,500,'winText','Winner Winner Chicken Dinner',100,tColor = '#FFCB9A'))
    winScreen2.addItem(winBox(200,450,1000,500,'winText',(game,),'name',tSize = 30, tColor = '#FFCB9A'))
    winScreen2.addItem(linkButton(width-230, height - 140,200,50,'winToStart', 'startScreen',screenManager,tString = 'Play again'))
    
    winScreen3 = Screen('winScreen3')
    screenManager.addScreen(winScreen3)
    winScreen3.addItem(textBox(200,250,1000,500,'winText','Winner Winner Chicken Dinner',100,tColor = '#FFCB9A'))
    winScreen3.addItem(winBox(200,450,1000,500,'winText',(game,),'name',tSize = 30, tColor = '#FFCB9A'))
    winScreen3.addItem(linkButton(width-230, height - 140,200,50,'winToStart', 'startScreen',screenManager,tString = 'Play again'))
    # winScreen2.addItem(textBox(500,500,100,100,'winText','restart',100,tColor = '17325547'))


    startScreen = Screen('startScreen')
    screenManager.addScreen(startScreen)
    startScreen.addItem(img(width/2 - 250,height/2 - 400,500,600,'logo',imgUrl = 'data\Logo.png'))
    startScreen.addItem(linkButton(width/2-50,height - 140,100,50,'startToSetting','gameModeScreen',screenManager,tString = 'Start'))
    screenManager.currentScreen = startScreen
    
    #screens for setting up the game
    #gameMode screen
    gameModeScreen = Screen('gameModeScreen')
    screenManager.addScreen(gameModeScreen)
    gameModeScreen.addItem(item(0,0,width,300,'titleBarBackground', backgroundColor ="#2C3531"))
    gameModeScreen.addItem(textBox(0,0,width,300,"titleBar", "GAMEMODE",50))
    gameModeScreen.addItem(textBox(0,300,width,280,'explanation', "Select the gamemode you want to play"))
    settingFunDrop = funDropDown(width/2 -200,580,400,40,'GameModeDropDown','Last one standing',game.setGameMode,'Last one standing', 'Three castles', 'firstKnockOut')
    gameModeScreen.addItem(settingFunDrop)
    gameModeScreen.addItem(linkButton(width/2 - 50, height - 140,100,50,'GameModeToPlayerSetup', 'playerSetupScreen',screenManager,tString = 'Next'))
    
    setupDice1 = setupDice(750,height/2 + 50, 100,100,'setupDice1',1,backgroundColor = color(255,0,0))
    setupDice2 = setupDice(950,height/2 + 50, 100,100,'setupDice2',1,backgroundColor = color(255,255,0))
    setupDice3 = setupDice(1150,height/2 + 50, 100,100,'setupDice3',1,backgroundColor = color(0,255,0))
    setupDice4 = setupDice(1350,height/2 + 50, 100,100,'setupDice4',1,backgroundColor = color(0,0,255))
    settingScreenDices = [setupDice1,setupDice2,setupDice3,setupDice4]
    setupDiceGroup1 = setupDiceGroup(100,height/2 + 50, width,100,'setupDiceGroup1',game, *settingScreenDices)
    
    #playerSetupSCreen
    playerSetupScreen = Screen('playerSetupScreen')
    playerSetupScreen.addItem(linkButton(50, height - 140,100,50,'PlayerSetupToGameMode', 'gameModeScreen',screenManager,tString = 'Back'))
    playerSetupScreen.addItem(linkButton(width - 150, height - 140,100,50,'PlayerSetupToStartDice', 'startDiceScreen',screenManager,tString = 'Next'))
    playerSetupScreen.addItem(item(0,0,width,300,'titleBarBackground', backgroundColor ="#2C3531"))
    playerSetupScreen.addItem(textBox(0,0,width,300,'TitleBar','PLAYER SETUP',50))
    playerSetupScreen.addItem(textBox(0,300,width,280,'explanation','Select the amount of players'))
    playerSetupScreen.addItem(setupDropDown(width/2 -200 ,580,400,40,'dropdown1','2',game, setupDiceGroup1, '2','3','4'))
    screenManager.addScreen(playerSetupScreen)
    
    startDiceScreen = Screen('startDiceScreen')
    screenManager.addScreen(startDiceScreen)
    startDiceScreen.addItem(item(0,0,width,300,'titleBarBackground', backgroundColor ="#2C3531"))
    startDiceScreen.addItem(textBox(0,0,width,300,'TitleBar','START PLAYER',50))
    startDiceScreen.addItem(textBox(0,300,width,280,'explanation', 'Click the dice to roll. The color with the highest dice is the start player'))
    startDiceScreen.addItem(setupDiceGroup1)
    startDiceScreen.addItem(linkButton(50, height - 140,100,50,'startDiceToPlayerSetup', 'playerSetupScreen',screenManager,tString = 'Back'))
    startDiceScreen.addItem(linkButton(width - 150, height - 140,100,50,'startDiceToTestScreen','testScreen',screenManager,tString = 'Next'))

    #a lot of code for the shopScreen
    shopScreen = Screen('shopScreen')
    screenManager.addScreen(shopScreen)
    shopScreen.addItem(item(0,0,width,200,'titleBarBackground', backgroundColor ="#2C3531"))
    shopScreen.addItem(textBox(0,0,width,200,"titleBar", "SHOP",50))
    # Temp links to shopmapscreens
    # shopScreen.addItem(linkButton(10,10,100,100,'linkButton1','shopFarmMapScreen',screenManager, tString = 'Go to farmMap'))
    # shopScreen.addItem(linkButton(10,120,100,100,'linkButton1','shopVillageMapScreen',screenManager, tString = 'Go to villageMap'))
    # shopScreen.addItem(linkButton(10,230,100,100,'linkButton1','shopBarracksMapScreen',screenManager, tString = 'Go to BarracksMap'))
    # shopScreen.addItem(linkButton(10,340,100,100,'linkButton1','shopWallsMapScreen',screenManager, tString = 'Go to WallsMap'))
    # shopScreen.addItem(linkButton(10,450,100,100,'linkButton1','shopTowerMapScreen',screenManager, tString = 'Go to TowerMap'))
    # shopScreen.addItem(linkButton(10,450,100,100,'linkButton1','shopTowerMapScreen',screenManager, tString = 'Go to TowerMap'))
    # shopScreen.addItem(linkButton(10,560,100,100,'linkButton1','shopCastleMapScreen',screenManager, tString = 'Go to CastleMap'))
    # shopScreen.addItem(linkButton(10,560,100,100,'linkButton1','shopRoadMapScreen',screenManager, tString = 'Go to RoadMap'))
    
    sideBar = item(width-400,200,400,height,'sideBar')
    sideBar.backgroundColor = "#253031"
    shopScreen.addItem(sideBar)

    
    currentplayerbox = varBox(0,220,width-200,100,'currentplayerTextbox', (game,),game._currentPlayer.name ,'name')
    currentplayerbox.tSize = 50
    shopScreen.addItem(currentplayerbox)

    #adding all the add buttons
    troopsInput = textInput(width - 275, 220, 60, 60,'attackerInput')

    shopScreen.addItem(troopsInput)
    shopScreen.addItem(textBox(width - 90, 220, 280, 40, 'troopsTextbox', 'Troops', 20))
    shopScreen.addItem(varArgFunButton(width - 90, 220, 80, 40, 'addTroopButton',game._currentPlayer.settroops,1,(game,),'settroops',(troopsInput,)))
    shopScreen.addItem(textBox(width - 90, 220, 80, 40, 'addTroopButtonText', 'Buy', 20))
    shopScreen.addItem(textBox(width - 170, 220, 80, 40, 'addTroopButtonText', '2', 20))

    shopScreen.addItem(textBox(width - 380, 310, 280, 40, 'desertTextbox', 'Villager', 20))
    shopScreen.addItem(varFunButton(width - 90, 310, 80, 40, 'addVillagerButton',game._currentPlayer.setvillagers,1,(game._currentPlayer,game),'setvillagers'))
    shopScreen.addItem(textBox(width - 90, 310, 80, 40, 'addVillagerButtonText', 'Buy', 20))
    shopScreen.addItem(textBox(width - 170, 310, 80, 40, 'addVillagerButtonText', '2', 20))
    
    shopScreen.addItem(textBox(width - 380, 400, 280, 40, 'RoadTextbox', 'Road', 20))
    shopScreen.addItem(shopMapLinkButton(width - 90, 400, 80, 40, 'addRoadButton', game._currentPlayer.coins,1,(game._currentPlayer,game), 'coins','shopRoadMapScreen',screenManager))
    shopScreen.addItem(textBox(width - 90, 400, 80, 40, 'addRoadButtonText', 'Buy', 20))
    shopScreen.addItem(textBox(width - 170, 400, 80, 40, 'addRoadButtonText', '1', 20))


    shopScreen.addItem(textBox(width - 380, 490, 280, 40, 'towerTextbox', 'Tower', 20))
    shopScreen.addItem(shopMapLinkButton(width - 90, 490, 80, 40, 'addTowerButton', game._currentPlayer.coins,15,(game._currentPlayer,game), 'coins','shopTowerMapScreen',screenManager))
    shopScreen.addItem(textBox(width - 90, 490, 80, 40, 'addTowerButtonText', 'Buy', 20))
    shopScreen.addItem(textBox(width - 170, 490, 80, 40, 'addTowerButtonText', '15', 20))

    shopScreen.addItem(textBox(width - 380, 580, 280, 40, 'farmTextbox', 'Farm', 20))
    shopScreen.addItem(shopMapLinkButton(width - 90, 580, 80, 40, 'addFarmButton',game._currentPlayer.coins,4,(game._currentPlayer,game), 'coins','shopFarmMapScreen',screenManager))
    shopScreen.addItem(textBox(width - 90, 580, 80, 40, 'addFarmButtonText', 'Buy', 20))
    shopScreen.addItem(textBox(width - 170, 580, 80, 40, 'addFarmButtonText', '4', 20))

    shopScreen.addItem(textBox(width - 380, 670, 280, 40, 'villageTextbox', 'Village', 20))
    shopScreen.addItem(shopMapLinkButton(width - 90, 670, 80, 40, 'addVillageButton', game._currentPlayer.coins,5,(game._currentPlayer,game), 'coins','shopVillageMapScreen',screenManager))
    shopScreen.addItem(textBox(width - 90, 670, 80, 40, 'addVillageText', 'Buy', 20))
    shopScreen.addItem(textBox(width - 170, 670, 80, 40, 'addVillageText', '5', 20))

    shopScreen.addItem(textBox(width - 380, 760, 280, 40, 'barracksTextbox', 'Barracks', 20))
    shopScreen.addItem(shopMapLinkButton(width - 90, 760, 80, 40, 'addBarracksButton', game._currentPlayer.coins,5,(game._currentPlayer,game), 'coins','shopBarracksMapScreen',screenManager))
    shopScreen.addItem(textBox(width - 90, 760, 80, 40, 'addBarracksButtonText', 'Buy', 20))
    shopScreen.addItem(textBox(width - 170, 760, 80, 40, 'addBarracksButtonText', '5', 20))
    
    shopScreen.addItem(textBox(width - 380, 850, 280, 40, 'wallsTextbox', 'Walls', 20))
    shopScreen.addItem(shopMapLinkButton(width - 90, 850, 80, 40, 'addWallsButton', game._currentPlayer.coins,10,(game._currentPlayer,game), 'coins','shopWallsMapScreen',screenManager))
    shopScreen.addItem(textBox(width - 90, 850, 80, 40, 'addWallsButtonText', 'Buy', 20))
    shopScreen.addItem(textBox(width - 170, 850, 80, 40, 'addWallsButtonText', '10', 20))
    
    shopScreen.addItem(textBox(width - 380, 940, 280, 40, 'castleTextbox', 'Castle', 20))
    shopScreen.addItem(shopMapLinkButton(width - 90, 940, 80, 40, 'addCastleButton', game._currentPlayer.coins,20,(game._currentPlayer,game),'coins','shopCastleMapScreen',screenManager))
    shopScreen.addItem(textBox(width - 90, 940, 80, 40, 'addCastleButtonText', 'Buy', 20))
    shopScreen.addItem(textBox(width - 170, 940, 80, 40, 'addCastleButtonText', '20', 20))


    shopScreen.addItem(textBox(1000,330,200,40,'currentPlayerCoinsText', 'Coins:',30))
    shopScreen.addItem(shopVarBox(1000,380,200,40,'currentPlayerCoins',game, [game,game._currentPlayer],game._currentPlayer.coins,'coins',tSize = 30))
    
    shopScreen.addItem(textBox(90,330,200,40,'currentPlayerSwampText', 'Swamps:',30))
    shopScreen.addItem(shopVarBox(300,330,100,40,'varText1',game,[game,game._currentPlayer],game._currentPlayer.swamp,'swamp',tSize = 30))

    shopScreen.addItem(textBox(90,370,200,40,'currentPlayerDesertText', 'Deserts:',30))
    shopScreen.addItem(shopVarBox(300,370,100,40,'varText1',game,[game,game._currentPlayer],game._currentPlayer.desert, 'desert', tSize = 30))

    shopScreen.addItem(textBox(90,410,200,40,'currentPlayerMountainText', 'Mountains:',30))
    shopScreen.addItem(shopVarBox(300,410,100,40,'varText1',game,[game,game._currentPlayer],game._currentPlayer.mountain, 'mountain', tSize = 30))

    shopScreen.addItem(textBox(90,450,200,40,'currentPlayerForestText', 'Forests:',30))
    shopScreen.addItem(shopVarBox(300,450,100,40,'varText1',game,[game,game._currentPlayer],game._currentPlayer.forest, 'forest', tSize = 30))

    shopScreen.addItem(textBox(90,490,200,40,'currentPlayerHighlandText', 'Highlands:',30))
    shopScreen.addItem(shopVarBox(300,490,100,40,'varText1',game,[game,game._currentPlayer],game._currentPlayer.highland, 'highland', tSize = 30))

    shopScreen.addItem(textBox(610,330,200,40,'currentPlayerPalacesText', 'Palaces:',30))
    shopScreen.addItem(shopVarBox(830,330,100,40,'varText1',game,[game,game._currentPlayer],game._currentPlayer.palaces, 'palaces', tSize = 30))

    shopScreen.addItem(textBox(610,370,200,40,'currentPlayerVillagesText', 'Villages:',30))
    shopScreen.addItem(shopVarBox(830,370,100,40,'varText1',game,[game,game._currentPlayer],game._currentPlayer.villages, 'villages', tSize = 30))

    shopScreen.addItem(textBox(610,410,200,40,'currentPlayerFarmsText', 'Farms:',30))
    shopScreen.addItem(shopVarBox(830,410,100,40,'varText1',game,[game,game._currentPlayer],game._currentPlayer.farms, 'farms', tSize = 30))

    shopScreen.addItem(textBox(610,450,200,40,'currentPlayerCastlesText', 'Castles:',30))
    shopScreen.addItem(shopVarBox(830,450,100,40,'varText1',game,[game,game._currentPlayer],game._currentPlayer.castles, 'castles', tSize = 30))

    shopScreen.addItem(textBox(610,490,200,40,'currentPlayerBarracksText', 'Barracks:',30))
    shopScreen.addItem(shopVarBox(830,490,100,40,'varText1',game,[game,game._currentPlayer],game._currentPlayer.barracks, 'barracks', tSize = 30))

    shopScreen.addItem(textBox(610,530,200,40,'currentPlayerWallsText', 'Walls:',30))
    shopScreen.addItem(shopVarBox(830,530,100,40,'varText1',game,[game,game._currentPlayer],game._currentPlayer.walls, 'walls', tSize = 30))

    shopScreen.addItem(textBox(610,570,200,40,'currentPlayerTowersText', 'Towers:',30))
    shopScreen.addItem(shopVarBox(830,570,100,40,'varText1',game,[game,game._currentPlayer],game._currentPlayer.towers, 'towers', tSize = 30))
    
    shopScreen.addItem(textBox(610,650,200,40,'currentPlayerTroopsText', 'Troops:',30))
    shopScreen.addItem(shopVarBox(830,650,100,40,'varText1',game,[game,game._currentPlayer],game._currentPlayer.towers, 'troops', tSize = 30))
    
    shopScreen.addItem(textBox(610,730,200,40,'currentPlayerVillagersText', 'Villagers:',30))
    shopScreen.addItem(shopVarBox(830,730,100,40,'varText1',game,[game,game._currentPlayer],game._currentPlayer.villagers, 'villagers', tSize = 30))

    # shopScreen.addItem(funButton(width - 630, height - 100, 200,50,'nextPlayerButton',game.nextPlayer, tString = 'next player',tColor = color(255), backgroundColor = color(51)))
    shopScreen.addItem(linkButton(width-630 , height - 100, 200,50,'nextButton','battleStartScreen',screenManager, tString = 'Next',tColor = color(255), backgroundColor = color(51)))
    shopScreen.addItem(linkButton(width-880 , height - 100, 200,50,'mapButton','mapScreen',screenManager, tString = 'View Map',tColor = color(255), backgroundColor = color(51)))
    
    battleStartScreen = Screen('battleStartScreen')
    screenManager.addScreen(battleStartScreen)
    battleStartScreen.addItem(item(0,0,width,200,'titleBarBackground', backgroundColor ="#2C3531"))
    battleStartScreen.addItem(textBox(0,0,width,200,'title', 'BATTLE', 50))
    battleStartScreen.addItem(textBox(0,300,width,280,'explanation','Do you want to fight against someone?'))
    battleStartScreen.addItem(linkButton(width/2 - 150,height/2-50,300,50,'linkButton2','battleSim',screenManager, tString = 'Yes, lets fight!'))
    battleStartScreen.addItem(linkButton(width/2 - 150,height/2 + 50,300,50,'linkButton2','shopScreen',screenManager, tString = 'No, end turn'))
    battleStartScreen.addItem(funButton(width/2 - 150, height/2 + 50,300,50,'nextPlayerButton',game.nextPlayer, tColor = color(255), backgroundColor = color(51)))
    battleStartScreen.addItem(linkButton(30,height-100,100,50,'linkButton2','shopScreen',screenManager, tString = 'Back'))
    
    
    battleSimScreen = Screen('battleSim')
    screenManager.addScreen(battleSimScreen)
    battleSimScreen.addItem(item(0,0,width,200,'titleBarBackground', backgroundColor ="#2C3531"))
    battleSimScreen.addItem(textBox(0,0,width,200,'title', 'BATTLE SIMULATOR', 50))
    battleSimScreen.addItem(textBox(0,200,width,250,'explanation','Select the defender and the amount of troops'))
    battleSimScreen.addItem(textBox(400,400,100,100,'attacker', 'Attacker', 20))
    battleSimScreen.addItem(varBox(400,475,500,50,'currentplayerTextbox', (game,),game._currentPlayer.name ,'name',tSize = 40))
    battleSimScreen.addItem(textBox(1270,400,100,100,'troops1', 'Troops', 20))
    attTroops = funDropDown(1270,475,150,30,'attTroopDropDown','2',battle.setTroopsAttacker,2,3,4,5)
 
    battleSimScreen.addItem(attTroops)
    
    battleSimScreen.addItem(textBox(400,600,100,100,'defender', 'Defender', 20))
    battleSimScreen.addItem(varFunDropDown(400,675,500,30,'defenderInput',game,'Defender',battle.setDefender,*game.players))
    battleSimScreen.addItem(textBox(1270,600,100,100,'troops2', 'Troops', 20))
    defTroops = funDropDown(1270,675,150,30,'defTroopDropDown','0',battle.setTroopsDefender,0,1,2,3,4,5)
    battleSimScreen.addItem(defTroops)
    # battleSimScreen.addItem(linkButton(860,880,200,100,'rollButton','diceScreen',screenManager, tString = 'Roll'))
    battleSimScreen.addItem(linkButton(width - 130,height - 100,100,50,'battleMapButton','battleMapScreen',screenManager, tString = 'Next'))
    battleSimScreen.addItem(linkButton(30,height-100,100,50,'linkButton2','mapScreen',screenManager, tString = 'Back'))
    # dice1 = dice(200,500,100,100,'dice1',1)
    # dice2 = dice(300,500,100,100,'dice2',2)
    # dice3 = dice(400,500,100,100,'dice3',3)
    # dice4 = dice(500,500,100,100,'dice4',4)
    # dice5 = dice(600,500,100,100,'dice5',5)
    # dice6 = dice(700,500,100,100,'dice6',6)
    # dice7 = dice(200,300,100,100,'dice7',1)
    # dice8 = dice(300,300,100,100,'dice8',2)
    # dice9 = dice(400,300,100,100,'dice9',3)
    # dice10 = dice(500,300,100,100,'dice10',4)
    # dice11 = dice(600,300,100,100,'dice11',5)
    # dice12 = dice(700,300,100,100,'dice12',6)
    # diceGroup1 = diceGroup(200,500,600,100,'diceGroup1',dice1,dice2,dice3,dice4,dice5,dice6)
    # diceGroup2 = diceGroup(200,300,600,100,'diceGroup2',dice7,dice8,dice9,dice10,dice11,dice12)
    diceGroup1 = varDiceGroup(200,300,600,100,'diceGroup1',(attTroops,),'actoutput',battle.setDamToDef)
    diceGroup2 = varDiceGroup(200,500,600,100,'diceGroup2',(defTroops,),'actoutput',battle.setDamToAtt)
    diceScreen = Screen('diceScreen')
    screenManager.addScreen(diceScreen)
    diceScreen.addItem(diceGroup1)
    diceScreen.addItem(diceGroup2)
    diceScreen.addItem(linkButton(10,110,100,100,'linkButton1','battleSim',screenManager, tString = 'Back'))
    diceScreen.addItem(linkFunButton(width/2-100,800,200,100,'linkButton1',battle.fight,'battleResultScreen',screenManager, tString = 'Go to results'))
    diceScreen.addItem(varBox(800,300,100,100,'diceGroup1val', (diceGroup1,),0,'sum',tSize = 40, tColor = color(0)))
    diceScreen.addItem(varBox(800,500,100,100,'diceGroup1val', (diceGroup2,),0,'sum',tSize = 40, tColor = color(0)))
    
    battleResultScreen = Screen('battleResultScreen')
    screenManager.addScreen(battleResultScreen)
    battleResultScreen.addItem(linkButton(10,10,100,100,'linkButton1','shopScreen',screenManager, tString = 'Go to Shop'))
    battleResultScreen.addItem(linkButton(10,120,100,100,'linkButton1','mapScreen',screenManager, tString = 'Go to Map'))
    battleResultScreen.addItem(resultVarBox(width/3-300,height/3,600,400,'attackerResult',(battle,),True))
    battleResultScreen.addItem(resultVarBox(2*width/3-300,height/3,600,400,'defenderResult',(battle,),False))
