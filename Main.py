from tkinter import Tk, Canvas, PhotoImage
import sys, webbrowser
sys.path.append("./modules")

from UI import Menu
import Config, Game


def motion(event):
    """Runs everytime the cursor moves on the tkinter window."""
    coords = ( event.x, event.y )
    game.updateOnMotion(coords)
    playMenu.updateOnMotion(coords)
    mainMenu.updateOnMotion(coords)

def mousePress(event):
    """Runs everytime the left click of the mouse is pressed."""
    game.updateOnPress()
    playMenu.updateOnPress()
    mainMenu.updateOnPress()

def mouseRelease(event):
    """Runs everytime the left click of the mouse is released."""
    playMenu.updateOnRelease()
    mainMenu.updateOnRelease()

#### Variables ####
width, height = 700, 700  # Taille de la fenetre

myTheme = Config.createTheme( Config.themes["Primary"]["Night"],
                             Config.themes["Secondary"]["Gold"] )

#### Set up de la fenetre Tkinter ####
root = Tk()
cv = Canvas(root, width=width, height=height, bg=myTheme["Primary"]["background"])
cv.pack()

#### Creation du Menu principale ####
cv.create_rectangle( width * 3 // 4, 0, width, height, fill=myTheme["Primary"]["game"][0], outline="", tag="UI")
cv.create_rectangle( 0, 0, width, height//5, fill=myTheme["Primary"]["interface"], outline="", tag="UI")

game = Game.Game(root, cv, (10, 150), 400, myTheme)
game.start()

#### Menu jouer  ####
playMenu = Menu(cv, width - 400, height//5 , 200, 100, myTheme["Menu"] )
playMenu.selfDestruct = True

playMenu.addButton("New  Game", game.start)
playMenu.addButton("Load"    , game.load)

#### Menu Principale  ####
mainMenu = Menu(cv, width - 200, height//5 , 200, 100, myTheme["Menu"], [ playMenu ])
mainMenu.addButton( "Play"    , playMenu.start )
mainMenu.addButton( "Save"    , game.save )
mainMenu.addButton( "Help"  , lambda : webbrowser.open('https://github.com/Me-k-01/Projet_Python') )
mainMenu.addButton( "Settings", lambda : print("Comming Soon") )
mainMenu.addButton( "Quit"    , root.destroy )

mainMenu.start()

#### Event sur le canvas  ####
cv.bind('<Motion>', motion)
cv.bind('<ButtonPress-1>', mousePress )
cv.bind('<ButtonRelease-1>', mouseRelease )

root.mainloop()
