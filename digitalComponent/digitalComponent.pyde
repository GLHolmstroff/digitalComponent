from gameManagement import *
from screenManagement import *
from Screens import *
from dice import *
from winScreen import *



def setup():
    # global img
    # img = loadImage('background.png')
    fullScreen()
    # print(width,height)
    frameRate(35)
    # noStroke()
    textAlign(CENTER,CENTER)
    setUpGame()

def draw():
    #reset the background
    
    background("#116466")
    # image(img,0,0)
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
