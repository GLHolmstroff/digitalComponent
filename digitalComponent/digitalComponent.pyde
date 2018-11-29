from gameManagement import *
from screenManagement import *
from testScreen import *





def setup():
    fullScreen()
    frameRate(35)
    noStroke()
    # Caladea = loadFont('Caladea-Regular-48.vlw')
    # textFont(Caladea)
    constructTestScreen()
    constructTestScreen2()

    

    
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
            
