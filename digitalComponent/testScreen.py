from screenManagement import *
from items import *
from mapScreen import *

typer = textInput(300,100,1000,100,'textIn1')

def constructTestScreen():
    testScreen = Screen('testScreen')
    screenManager.addScreen(testScreen)
    testScreen.addItem(checkbox(200,200,40,20,'checkbox1',False,'kdfs'))
    testScreen.addItem(linkButton(10,10,100,100,'linkButton1','testScreen2',screenManager))
    testScreen.addItem(textBox(10,10,100,100,'buttonTextBox', ' Goto Screen 2', 20))
    testScreen.addItem(textBox(300,300,1000,1000,'textBox1', 'Screen 1', 100))
    testScreen.addItem(textBox(300,100,1000,100,'textBox3',typer.intext.tString,20))
    testScreen.addItem(gameMap(1000,500,500,500,'Map1',3,3))
    screenManager.currentScreen = testScreen

def constructTestScreen2():
    testScreen2 = Screen('testScreen2')
    screenManager.addScreen(testScreen2)
    testScreen2.addItem(linkButton(10,10,100,100,'linkButton2','testScreen',screenManager))
    testScreen2.addItem(textBox(10,10,100,100,'buttonTextBox', ' Goto Screen 1', 20))
    testScreen2.addItem(textBox(300,300,1000,1000,'textBox2', 'Screen 2', 100))
    testScreen2.addItem(typer)
