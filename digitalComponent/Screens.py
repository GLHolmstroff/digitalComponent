from gameManagement import *
from screenManagement import *
from mapScreen import *
from dice import *
from winScreen import *



def setUpGame():
    game = Game(screenManager)
    battle = Battle(game)
    
    # I make 4 players just for testing
    player1 = Player('player 1',color(255,255,255))
    player2 = Player('player 2',color(255,0,0))
    player3 = Player('player 3',color(0,255,0))
    player4 = Player('player 4',color(0,0,255))
    game.players.append(player1)
    game.players.append(player2)
    game.players.append(player3)
    game.players.append(player4)
    game.currentPlayer = player1
    game.currentPlayerIndex = 0

    shopFarm = Farm(0,0,0,0,'farm',game._currentPlayer)
    shopVillage = Village(0,0,0,0,'village',game._currentPlayer)
    shopBarracks = Barracks(0,0,0,0,'barracks',game._currentPlayer)
    shopWalls = Walls(0,0,0,0,'walls',game._currentPlayer)
    shopTower = Tower(0,0,0,0,'tower',game._currentPlayer)
    shopCastle = Castle(0,0,0,0,'castle',game._currentPlayer)
    palace = Palace(0,0,0,0,'palace',game._currentPlayer)
    
    setupmap = setupMap(0.3*width,0.1*height,0.75 * min(width,height),0.75 * min(width,height),'setupMap', 5)
    palaceMap = shopMap(0.3*width,0.1*height,0.75 * min(width,height),0.75 * min(width,height),'Map',(setupmap,),palace,(game,),'shopScreen',screenManager)
    farmMap = shopMap(0.3*width,0.1*height,0.75 * min(width,height),0.75 * min(width,height),'shopFarmMap',(palaceMap,),shopFarm,(game,),'shopScreen',screenManager)
    villageMap = shopMap(0.3*width,0.1*height,0.75 * min(width,height),0.75 * min(width,height),'shopVillageMap',(palaceMap,),shopVillage,(game,),'shopScreen',screenManager)
    barracksMap = shopMap(0.3*width,0.1*height,0.75 * min(width,height),0.75 * min(width,height),'shopBarracksMap',(palaceMap,),shopBarracks,(game,),'shopScreen',screenManager)
    wallsMap = shopMap(0.3*width,0.1*height,0.75 * min(width,height),0.75 * min(width,height),'shopWallsMap',(palaceMap,),shopWalls,(game,),'shopScreen',screenManager)
    towerMap = shopMap(0.3*width,0.1*height,0.75 * min(width,height),0.75 * min(width,height),'shopTowerMap',(palaceMap,),shopTower,(game,),'shopScreen',screenManager)
    castleMap = shopMap(0.3*width,0.1*height,0.75 * min(width,height),0.75 * min(width,height),'shopCastleMap',(palaceMap,),shopCastle,(game,),'shopScreen',screenManager)
    batMap = battleMap(0.3*width,0.1*height,0.75 * min(width,height),0.75 * min(width,height),'battleMap',(palaceMap,),battle)
    map2 = displayMap(0.3*width,0.1*height,0.75 * min(width,height),0.75 * min(width,height),'displayMap',(palaceMap,farmMap,villageMap,barracksMap,wallsMap,towerMap,castleMap,batMap))
    
    testScreen = Screen('testScreen')
    screenManager.addScreen(testScreen)
    
    testScreen.addItem(linkButton(10,500,100,100,'palaceButton','palaceScreen',screenManager, tString = 'Continue to Palaces'))
    testScreen.addItem(textBox(0,0,width,100,'textBox1', 'Create your map', 50))
    testScreen.addItem(funButton(0.2*width,0.4*height,100,100,'val+',setupmap.incSize,tString='+'))
    testScreen.addItem(funButton(0.2*width,0.6*height,100,100,'val-',setupmap.decSize,tString='-'))
    testScreen.addItem(setupmap)
    testScreen.addItem(colourPicker(1300,300,100,100,'desertPicker','#DAA33A'))
    testScreen.addItem(colourPicker(1600,300,100,100,'forestPicker','#8CA74D'))
    testScreen.addItem(colourPicker(1300,500,100,100,'highlandPicker','#C02823'))
    testScreen.addItem(colourPicker(1600,500,100,100,'mountainPicker','#F0E5B4'))
    testScreen.addItem(colourPicker(1300,700,100,100,'swampPicker','#3D342D'))
    testScreen.addItem(colourPicker(1600,700,100,100,'waterPicker','#4A8EA5'))
    
    palaceScreen = Screen('palaceScreen')
    screenManager.addScreen(palaceScreen)
    
    palaceScreen.addItem(textBox(0,0,width,100,'textBox1', 'Pick your starting tile', 50))
    palaceScreen.addItem(linkButton(10,500,100,100,'Begin game button','shopScreen',screenManager, tString = 'Begin game'))
    palaceScreen.addItem(palaceMap)
    palaceScreen.addItem(funButton(1300, 0.5*height, 200,50,'nextPlayerButton',game.nextPlayer, tString = 'next player',tColor = color(255), backgroundColor = color(51)))
    
    mapScreen = Screen('mapScreen')
    screenManager.addScreen(mapScreen)
    
    mapScreen.addItem(map2)
    mapScreen.addItem(linkButton(10,10,100,100,'linkButton1','winScreen',screenManager, tString = 'Go to winScreen'))
    mapScreen.addItem(linkButton(10,120,100,100,'linkButton1','shopScreen',screenManager, tString = 'Go to Shop'))
    mapScreen.addItem(linkButton(10,230,100,100,'linkButton1','battleSim',screenManager, tString = 'Go to battle'))
    
    shopFarmMapScreen = Screen('shopFarmMapScreen')
    screenManager.addScreen(shopFarmMapScreen)
    
    shopFarmMapScreen.addItem(farmMap)
    shopFarmMapScreen.addItem(mapUpdateButton(10,10,100,100,'farmMapUpdate',(farmMap,),'shopScreen',screenManager,villageMap,barracksMap,wallsMap,towerMap,castleMap,batMap, tString = 'Go to Shop'))
    
    shopVillageMapScreen = Screen('shopVillageMapScreen')
    screenManager.addScreen(shopVillageMapScreen)
    
    shopVillageMapScreen.addItem(villageMap)
    shopVillageMapScreen.addItem(mapUpdateButton(10,10,100,100,'villageMapUpdate',(villageMap,),'shopScreen',screenManager,farmMap,barracksMap,wallsMap,towerMap,castleMap,batMap, tString = 'Go to Shop'))
    
    shopBarracksMapScreen = Screen('shopBarracksMapScreen')
    screenManager.addScreen(shopBarracksMapScreen)
    
    shopBarracksMapScreen.addItem(barracksMap)
    shopBarracksMapScreen.addItem(mapUpdateButton(10,10,100,100,'barracksMapUpdate',(barracksMap,),'shopScreen',screenManager,farmMap,villageMap,wallsMap,towerMap,castleMap,batMap, tString = 'Go to Shop'))
    
    shopWallsMapScreen = Screen('shopWallsMapScreen')
    screenManager.addScreen(shopWallsMapScreen)
    
    shopWallsMapScreen.addItem(wallsMap)
    shopWallsMapScreen.addItem(mapUpdateButton(10,10,100,100,'wallsMapUpdate',(wallsMap,),'shopScreen',screenManager,farmMap,villageMap,barracksMap,towerMap,castleMap,batMap, tString = 'Go to Shop'))
    
    shopTowerMapScreen = Screen('shopTowerMapScreen')
    screenManager.addScreen(shopTowerMapScreen)
    
    shopTowerMapScreen.addItem(towerMap)
    shopTowerMapScreen.addItem(mapUpdateButton(10,10,100,100,'towerMapUpdate',(towerMap,),'shopScreen',screenManager,farmMap,villageMap,barracksMap,wallsMap,castleMap,batMap, tString = 'Go to Shop'))
    
    shopCastleMapScreen = Screen('shopCastleMapScreen')
    screenManager.addScreen(shopCastleMapScreen)
    
    shopCastleMapScreen.addItem(castleMap)
    shopCastleMapScreen.addItem(mapUpdateButton(10,10,100,100,'castleMapUpdate',(castleMap,),'shopScreen',screenManager,farmMap,villageMap,barracksMap,wallsMap,towerMap,batMap, tString = 'Go to Shop'))
    
    battleMapScreen = Screen('battleMapScreen')
    screenManager.addScreen(battleMapScreen)
    
    battleMapScreen.addItem(batMap)
    battleMapScreen.addItem(mapUpdateButton(10,10,100,100,'battleMapUpdate',(castleMap,),'battleSim',screenManager,farmMap,villageMap,barracksMap,wallsMap,towerMap,castleMap, tString = 'Go to Battle'))
    
    
    battle.setDamToDef(30)
    battleMapScreen.addItem(funButton(10,120,100,100,'Do Battle',battle.defDamage,tString='Do Battle'))
    
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
    diceScreen = Screen('diceScreen')
    screenManager.addScreen(diceScreen)
    diceScreen.addItem(diceGroup1)
    diceScreen.addItem(diceGroup2)
    
    winScreen = Screen("winScreen")
    screenManager.addScreen(winScreen)
    winScreen.addItem(textBox(200,250,1000,500,'winText','Winner Winner Chicken Dinner',100,tColor = '17325547'))
    winScreen.addItem(winBox(200,450,1000,500,'winText',(game,),'name',tSize = 30, tColor = '17325547'))
    
    winScreen2 = Screen('winScreen2')
    screenManager.addScreen(winScreen2)
    winScreen2.addItem(textBox(200,250,1000,500,'winText','Winner Winner Chicken Dinner',100,tColor = '17325547'))
    winScreen2.addItem(winBox(200,450,1000,500,'winText',(game,),'name',tSize = 30, tColor = '17325547'))
    
    winScreen3 = Screen('winScreen3')
    screenManager.addScreen(winScreen3)
    winScreen3.addItem(textBox(200,250,1000,500,'winText','Winner Winner Chicken Dinner',100,tColor = '17325547'))
    winScreen3.addItem(winBox(200,450,1000,500,'winText',(game,),'name',tSize = 30, tColor = '17325547'))
    # winScreen2.addItem(textBox(500,500,100,100,'winText','restart',100,tColor = '17325547'))


    startScreen = Screen('startScreen')
    screenManager.addScreen(startScreen)
    startScreen.addItem(img(width/2 - 250,height/2 - 400,500,600,'logo',imgUrl = 'data\Logo.png'))
    startScreen.addItem(linkButton(width/2-50,height - 140,100,50,'startToSetting','settingScreen',screenManager,tString = 'Start'))
    screenManager.currentScreen = startScreen


    settingScreen = Screen('settingScreen')
    screenManager.addScreen(settingScreen)
    leftCollumn = item(0,0,400,height,'settingScreenLeftCollumn')
    settingScreen.addItem(leftCollumn)
    settingScreen.addItem(textBox(400,100,width-400,100,'settingScreenTextBox1', 'Spelmode:', 50))
    settingScreen.addItem(textBox(400,200,width-400,100,'textBox1', 'last one standing', 30))

    settingScreen.addItem(textBox(400,400,width-400,100,'textBox1', 'First player to start',50))
    settingScreen.addItem(textBox(400,500,width-400,100,'textBox1', 'Click the dice',30))
    setupDice1 = setupDice(450,height/2 + 50, 100,100,'setupDice1',1,backgroundColor = color(255,0,0))
    setupDice2 = setupDice(650,height/2 + 50, 100,100,'setupDice2',1,backgroundColor = color(255,255,0))
    setupDice3 = setupDice(850,height/2 + 50, 100,100,'setupDice3',1,backgroundColor = color(0,255,0))
    setupDice4 = setupDice(1050,height/2 + 50, 100,100,'setupDice4',1,backgroundColor = color(0,0,255))
    settingScreenDices = [setupDice1,setupDice2,setupDice3,setupDice4]
    setupDiceGroup1 = setupDiceGroup(100,height/2 + 50, width,100,'setupDiceGroup1',game, *settingScreenDices)
    
    settingScreen.addItem(textBox(0,600,400,50,'amountOfPlayersText','Amount of players:',25, tColor = '#ffffff'))
    settingScreen.addItem(textBox(0,200,400,50,'gameModeText','Game mode:',25, tColor = '#ffffff'))
    settingScreen.addItem(setupDropDown(80,680,250,40,'dropdown1','Chose',game, setupDiceGroup1, '2','3','4'))
    settingScreen.addItem(funDropDown(80,280,250,40,'GameModeDropDown','Last one standing',game.setGameMode,'Last one standing', 'Three castles', 'firstKnockOut'))
    # settingScreen.addItem(varBox(400,200,width-400,80,'gameModeTextBox',(game),game.gameMode, 'gameMode'))
    settingScreen.addItem(setupDiceGroup1)
    settingScreen.addItem(linkButton(width/2-50,height - 140,100,50,'settingToTest','testScreen',screenManager,tString = 'Start'))


    

    #a lot of code for the shopScreen
    shopScreen = Screen('shopScreen')
    screenManager.addScreen(shopScreen)
    
    # Temp links to shopmapscreens
    # shopScreen.addItem(linkButton(10,10,100,100,'linkButton1','shopFarmMapScreen',screenManager, tString = 'Go to farmMap'))
    # shopScreen.addItem(linkButton(10,120,100,100,'linkButton1','shopVillageMapScreen',screenManager, tString = 'Go to villageMap'))
    # shopScreen.addItem(linkButton(10,230,100,100,'linkButton1','shopBarracksMapScreen',screenManager, tString = 'Go to BarracksMap'))
    # shopScreen.addItem(linkButton(10,340,100,100,'linkButton1','shopWallsMapScreen',screenManager, tString = 'Go to WallsMap'))
    # shopScreen.addItem(linkButton(10,450,100,100,'linkButton1','shopTowerMapScreen',screenManager, tString = 'Go to TowerMap'))
    # shopScreen.addItem(linkButton(10,450,100,100,'linkButton1','shopTowerMapScreen',screenManager, tString = 'Go to TowerMap'))
    # shopScreen.addItem(linkButton(10,560,100,100,'linkButton1','shopCastleMapScreen',screenManager, tString = 'Go to CastleMap'))
    
    sideBar = item(width-400,0,400,height,'sideBar')
    sideBar.backgroundColor = color(30)
    shopScreen.addItem(sideBar)
    playersOverview = item(0,height - 500,width-400,500,'playersOverview')
    playersOverview.backgroundColor = color(81)
    shopScreen.addItem(playersOverview)
    currentplayerbox = varBox(30,20,600,100,'currentplayerTextbox', (game,),game.currentPlayer.name ,'name',tSize = 40, tColor = color(0))
    shopScreen.addItem(currentplayerbox)

    #adding all the add buttons
    troopsInput = textInput(width - 275, 30, 60, 60,'attackerInput')
    troopsInput.tColor = '#ffffff'
    shopScreen.addItem(troopsInput)
    shopScreen.addItem(varArgFunButton(width - 90, 30, 80, 40, 'addTroopButton',game.currentPlayer.settroops,1,(game,),'settroops',(troopsInput,)))
    shopScreen.addItem(textBox(width - 90, 30, 80, 40, 'addTroopButtonText', 'add', 20))

    t = textBox(width - 380, 130, 280, 40, 'desertTextbox', 'Villager', 20)
    t.backgroundColor = color(30)
    t.tColor = '#ffffff'
    shopScreen.addItem(t)
    shopScreen.addItem(varFunButton(width - 90, 130, 80, 40, 'addVillagerButton',game.currentPlayer.setvillagers,1,(game.currentPlayer,game),'setvillagers'))
    shopScreen.addItem(textBox(width - 90, 130, 80, 40, 'addVillagerButtonText', 'add', 20))


    t = textBox(width - 380, 1030, 280, 40, 'castleTextbox', 'Castle', 20)
    t.backgroundColor = color(30)
    t.tColor = '#ffffff'
    shopScreen.addItem(t)
    shopScreen.addItem(linkVarFunButton(width - 90, 1030, 80, 40, 'addCastleButton', game.currentPlayer.setcastles,1,(game.currentPlayer,game),'setcastles','shopCastleMapScreen',screenManager))
    shopScreen.addItem(textBox(width - 90, 1030, 80, 40, 'addCastleButtonText', 'add', 20))

    t = textBox(width - 380, 530, 280, 40, 'towerTextbox', 'Tower', 20)
    t.backgroundColor = color(30)
    t.tColor = '#ffffff'
    shopScreen.addItem(t)
    shopScreen.addItem(linkVarFunButton(width - 90, 530, 80, 40, 'addTowerButton', game.currentPlayer.settowers,1,(game.currentPlayer,game), 'settowers','shopTowerMapScreen',screenManager))
    shopScreen.addItem(textBox(width - 90, 530, 80, 40, 'addTowerButtonText', 'add', 20))

    t = textBox(width - 380, 630, 280, 40, 'farmTextbox', 'Farm', 20)
    t.backgroundColor = color(30)
    t.tColor = '#ffffff'
    shopScreen.addItem(t)
    shopScreen.addItem(linkVarFunButton(width - 90, 630, 80, 40, 'addFarmButton',game.currentPlayer.setfarms,1,(game.currentPlayer,game), 'setfarms','shopFarmMapScreen',screenManager))
    shopScreen.addItem(textBox(width - 90, 630, 80, 40, 'addFarmButtonText', 'add', 20))

    t = textBox(width - 380, 730, 280, 40, 'villageTextbox', 'Village', 20)
    t.backgroundColor = color(30)
    t.tColor = '#ffffff'
    shopScreen.addItem(t)
    shopScreen.addItem(linkVarFunButton(width - 90, 730, 80, 40, 'addVillageButton', game.currentPlayer.setvillages,1,(game.currentPlayer,game), 'setvillages','shopVillageMapScreen',screenManager))
    shopScreen.addItem(textBox(width - 90, 730, 80, 40, 'addVillageText', 'add', 20))

    t = textBox(width - 380, 830, 280, 40, 'barracksTextbox', 'Barracks', 20)
    t.backgroundColor = color(30)
    t.tColor = '#ffffff'
    shopScreen.addItem(t)
    shopScreen.addItem(linkVarFunButton(width - 90, 830, 80, 40, 'addBarracksButton', game.currentPlayer.setbarracks,1,(game.currentPlayer,game), 'setbarracks','shopBarracksMapScreen',screenManager))
    shopScreen.addItem(textBox(width - 90, 830, 80, 40, 'addBarracksButtonText', 'add', 20))

    t = textBox(width - 380, 930, 280, 40, 'wallsTextbox', 'Walls', 20)
    t.backgroundColor = color(30)
    t.tColor = '#ffffff'
    shopScreen.addItem(t)
    shopScreen.addItem(linkVarFunButton(width - 90, 930, 80, 40, 'addWallsButton', game.currentPlayer.setwalls,1,(game.currentPlayer,game), 'setwalls','shopWallsMapScreen',screenManager))
    shopScreen.addItem(textBox(width - 90, 930, 80, 40, 'addWallsButtonText', 'add', 20))

    shopScreen.addItem(textBox(800,100,200,30,'currentPlayerCoinsText', 'Coins:', tColor = color(255)))
    shopScreen.addItem(varBox(800,150,200,30,'currentPlayerCoins', (game,) + tuple(game.players),game.currentPlayer.coins,'coins',tSize = 20, tColor = color(255)))
    
    shopScreen.addItem(textBox(40,100,200,30,'currentPlayerSwampText', 'Swamps:',20,color(255)))
    shopScreen.addItem(varBox(250,100,100,30,'varText1',(game,)+tuple(game.players),game.currentPlayer.swamp,'swamp',tSize = 20, tColor = color(255)))

    shopScreen.addItem(textBox(40,140,200,30,'currentPlayerDesertText', 'Deserts:',20,color(255)))
    shopScreen.addItem(varBox(250,140,100,30,'varText1',(game,)+tuple(game.players),game.currentPlayer.desert, 'desert', tSize = 20, tColor = color(255)))

    shopScreen.addItem(textBox(40,180,200,30,'currentPlayerMountainText', 'Mountains:',20,color(255)))
    shopScreen.addItem(varBox(250,180,100,30,'varText1',(game,)+tuple(game.players),game.currentPlayer.mountain, 'mountain', tSize = 20, tColor = color(255)))

    shopScreen.addItem(textBox(40,220,200,30,'currentPlayerForestText', 'Forests:',20,color(255)))
    shopScreen.addItem(varBox(250,220,100,30,'varText1',(game,)+tuple(game.players),game.currentPlayer.forest, 'forest', tSize = 20, tColor = color(255)))

    shopScreen.addItem(textBox(40,260,200,30,'currentPlayerHighlandText', 'Highlands:',20,color(255)))
    shopScreen.addItem(varBox(250,260,100,30,'varText1',(game,)+tuple(game.players),game.currentPlayer.highland, 'highland', tSize = 20, tColor = color(255)))

    shopScreen.addItem(textBox(340,100,200,30,'currentPlayerPalacesText', 'Palaces:',20,color(255)))
    shopScreen.addItem(varBox(550,100,100,30,'varText1',(game,)+tuple(game.players),game.currentPlayer.palaces, 'palaces', tSize = 20, tColor = color(255)))

    shopScreen.addItem(textBox(340,140,200,30,'currentPlayerVillagesText', 'Villages:',20,color(255)))
    shopScreen.addItem(varBox(550,140,100,30,'varText1',(game,)+tuple(game.players),game.currentPlayer.villages, 'villages', tSize = 20, tColor = color(255)))

    shopScreen.addItem(textBox(340,180,200,30,'currentPlayerFarmsText', 'Farms:',20,color(255)))
    shopScreen.addItem(varBox(550,180,100,30,'varText1',(game,)+tuple(game.players),game.currentPlayer.farms, 'farms', tSize = 20, tColor = color(255)))

    shopScreen.addItem(textBox(340,220,200,30,'currentPlayerCastlesText', 'Castles:',20,color(255)))
    shopScreen.addItem(varBox(550,220,100,30,'varText1',(game,)+tuple(game.players),game.currentPlayer.castles, 'castles', tSize = 20, tColor = color(255)))

    shopScreen.addItem(textBox(340,260,200,30,'currentPlayerBarracksText', 'Barracks:',20,color(255)))
    shopScreen.addItem(varBox(550,260,100,30,'varText1',(game,)+tuple(game.players),game.currentPlayer.barracks, 'barracks', tSize = 20, tColor = color(255)))

    shopScreen.addItem(textBox(340,300,200,30,'currentPlayerWallsText', 'Walls:',20,color(255)))
    shopScreen.addItem(varBox(550,300,100,30,'varText1',(game,)+tuple(game.players),game.currentPlayer.walls, 'walls', tSize = 20, tColor = color(255)))

    shopScreen.addItem(textBox(340,340,200,30,'currentPlayerTowersText', 'Towers:',20,color(255)))
    shopScreen.addItem(varBox(550,340,100,30,'varText1',(game,)+tuple(game.players),game.currentPlayer.towers, 'towers', tSize = 20, tColor = color(255)))
    
    shopScreen.addItem(textBox(340,420,200,30,'currentPlayerTowersText', 'Troops:',20,color(255)))
    shopScreen.addItem(varBox(550,420,100,30,'varText1',(game,)+tuple(game.players),game.currentPlayer.towers, 'troops', tSize = 20, tColor = color(255)))
    
    shopScreen.addItem(textBox(340,500,200,30,'currentPlayerTowersText', 'Villagers:',20,color(255)))
    shopScreen.addItem(varBox(550,500,100,30,'varText1',(game,)+tuple(game.players),game.currentPlayer.villagers, 'villagers', tSize = 20, tColor = color(255)))

    shopScreen.addItem(funButton(400, height - 100, 200,50,'nextPlayerButton',game.nextPlayer, tString = 'next player',tColor = color(255), backgroundColor = color(51)))
    shopScreen.addItem(linkButton(400, height - 200, 200,50,'mapButton','mapScreen',screenManager, tString = 'Go to Map',tColor = color(255), backgroundColor = color(51)))
    
    battleSimScreen = Screen('battleSim')
    screenManager.addScreen(battleSimScreen)
    battleSimScreen.addItem(linkButton(10,10,100,100,'linkButton2','mapScreen',screenManager, tString = 'Go to Map'))
    battleSimScreen.addItem(textBox(760,10,400,200,'title', 'Battle Simulator', 60))
    battleSimScreen.addItem(textBox(150,300,100,100,'attacker', 'Attacker', 20))
    battleSimScreen.addItem(textInput(150,375,500,50,'attackerInput'))
    battleSimScreen.addItem(textBox(1670,300,100,100,'troops1', 'Troops', 20))
    battleSimScreen.addItem(textInput(1270,375,500,50,'troopsInput'))
    battleSimScreen.addItem(textBox(150,500,100,100,'defender', 'Defender', 20))
    battleSimScreen.addItem(textInput(150,575,500,50,'defenderInput'))
    battleSimScreen.addItem(textBox(1670,500,100,100,'troops2', 'Troops', 20))
    battleSimScreen.addItem(textInput(1270,575,500,50,'defenderInput'))
    battleSimScreen.addItem(checkbox(1670,650,20,20,'walls',0,battle.buildings,'wall'))
    battleSimScreen.addItem(textBox(1680,645,100,24,'walls', 'Walls', 20))
    battleSimScreen.addItem(checkbox(1670,690,20,20,'tower',0,battle.buildings,'tower'))
    battleSimScreen.addItem(textBox(1680,685,100,24,'tower', 'Tower', 20))
    battleSimScreen.addItem(checkbox(1670,730,20,20,'castle',0,battle.buildings, 'castle'))
    battleSimScreen.addItem(textBox(1680,725,100,24,'castle', 'Castle', 20))
    battleSimScreen.addItem(checkbox(1670,770,20,20,'palace',0,battle.buildings, 'palace'))
    battleSimScreen.addItem(textBox(1680,765,100,24,'palace', 'Palace', 20))
    battleSimScreen.addItem(linkButton(860,880,200,100,'rollButton','diceScreen',screenManager, tString = 'Roll'))
    battleSimScreen.addItem(linkButton(10,120,100,100,'rollButton','battleMapScreen',screenManager, tString = 'BattleMap'))
